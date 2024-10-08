from backend.dao.MasterDAO import MasterDAO
from backend.dao.PolicyDAO import PolicyDAO
from backend.dao.EmailDAO import EmailDAO
from backend.dao.PartnersDAO import *
from backend.classes.Common import *
from backend.classes.InitInfo import InitInfo
from .config import *


def helper_payment_link_generation(request):
    print(request.POST)

    inserted_id = 0

    init_info = InitInfo.init(request)
    host_url = init_info['host_url']
    partner_code = init_info['partner_code']

    if request.method == 'POST':
        # {'csrfmiddlewaretoken': ['H8gVuWtefVznsgvPjo3wSA5ip0QyWm6L9X9RSCLXgdor8Gw2SV3qG0t8yvLAn7ih'], 'category': ['1'], 'brand': ['APPLE:4:APPLE'], 'item': ['15720:S2761-3220:iPhone XS Max, 4GB RAM,64GB STORAGE:2879'], 'purchase_month': ['12_24'], 'plan_type': ['yearly'], 'plan_id': ['10001'], 'sales_person_id': ['12'], 'first_name': ['sumit'], 'last_name': ['nayak'], 'mobile_no': ['9838383832'], 'email_id': ['sumitkumar@gmail.com']}
        category = request.POST.get('category', None)
        brand = request.POST.get('brand', None)
        item = request.POST.get('item', None)
        purchase_month = request.POST.get('purchase_month', None)
        plan_type = request.POST.get('plan_type', None)
        sales_person_id = request.POST.get('sales_person_id', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        mobile_no = request.POST.get('mobile_no', None)
        email_id = request.POST.get('email_id', None)
        plan_id = request.POST.get('plan_id', None)
        # device_value = request.POST.get('device_value', None)

        # stg Domain
        et_domain = "https://devae.protect4less.com"
        # Prod Domain
        # et_domain = "https://protect4less.ae"

        error = None
        error = 'Invalid category' if category is None else None
        error = error if error is None else 'Invalid brand' if brand is None else None
        error = error if error is None else 'Invalid item' if item is None else None
        error = error if error is None else 'Invalid purchase_month' if purchase_month is None else None
        error = error if error is None else 'Invalid plan_type' if plan_type is None else None
        error = error if error is None else 'Invalid sales_person_id' if sales_person_id is None else None
        error = error if error is None else 'Invalid first_name' if first_name is None else None
        error = error if error is None else 'Invalid last_name' if last_name is None else None
        error = error if error is None else 'Invalid mobile_no' if mobile_no is None else None
        error = error if error is None else 'Invalid email_id' if email_id is None else None
        error = error if error is None else 'Invalid plan_id' if plan_id is None else None

        slab_code, device_cost = '', ''

        if error is None:
            item_data = item.split(':')
            slab_code = item_data[1]
            item_id = item_data[0]
            item_name = item_data[2]
            device_cost = item_data[3]
            brand_data = brand.split(':')
            brand_code = brand_data[0]
            brand_id = brand_data[1]
            term_type = 'PM' if plan_type == 'monthly' else 'PY' if plan_type == 'yearly' else ""

        if error is None:

            # QUIX Partner condition
            if partner_code == '1042':
                device_value = helper_get_devicevalue(device_cost)
                price_data = helper_quix_standard_plan_price(purchase_month, plan_type, device_value)
                plan_id = 10001  # Remove this code once the AED price are inserted inside the DB
                price_data = price_data['responseData']['price_data']
                slab_code = device_value

                '''
                Quix sells only Yearly plans. Standard Plan is PY plan type code. Extended Warranty is PEW12M
                '''
                term_type = price_data['plan_type_code']
            else:
                if purchase_month == '0_12':
                    price_data = MasterDAO.get_plan(plan_id=plan_id)
                    price_data = price_data[0] if len(price_data) > 0 else {}
                else:
                    ew_price_data = ew_price_config(prod_id=1)
                    price_data = ew_price_data[plan_type]

        print('price_data:: ', price_data)

        input_data = {
            'pgpl_partner_code': partner_code,
            'pgpl_slab_code': slab_code,
            'pgpl_plan_id': plan_id,
            'pgpl_plan_price': price_data['plan_price'],
            'pgpl_plan_tax': price_data['plan_tax'],
            'pgpl_plan_total_price': price_data['plan_total_price'],
            'pgpl_plan_currency': price_data['plan_unit'],
            'pgpl_category_id': category,
            'pgpl_brand_id': brand_id,
            'pgpl_brand_code': brand_code,
            'pgpl_item_id': item_id,
            'pgpl_item_name': item_name,
            'pgpl_purchase_month': purchase_month,
            'pgpl_first_name': first_name,
            'pgpl_last_name': last_name,
            'pgpl_email': email_id,
            'pgpl_mobile_number': mobile_no,
            'pgpl_term_type': term_type,
            'pgpl_plan_type': price_data['plan_type'],
            'pgpl_plan_title': price_data['plan_title'],
            'pgpl_salesperson_id': sales_person_id,
            'pgpl_salesperson_email': request.user.email
        }

        inserted_id = PolicyDAO.insert_partners_generate_payement_link(input_data)

        # Send EMail to the Customer of the Payment Link
        EmailDAO.insert_email_tran(data={"et_type": "customer_send_payment_link", "et_email_id": email_id,
                                         "et_subject": "Complete Your P4L Policy Purchase & Get Your Protection Plan",
                                         "et_tl_id": inserted_id, "et_domain": et_domain, "et_status": "pending"})

    category_info = get_create_plan_data(prod_id=1)
    print('category_info:: ', category_info)
    return {'category_info': category_info['category_info'], 'inserted_id': inserted_id, 'host_url': host_url,
            'partner_code': partner_code}


def helper_insert_into_partneroffline(request, partner_code):
    print("\n\n"), print("insert_into_partneroffline \t:", request.POST), print("\n\n")
    insertedid = None
    invoice_number = request.POST.get('invoice_number', '')
    sku = request.POST.get('sku', '')
    location = request.POST.get('location', '')
    device = request.POST.get('category', '')
    device = device.split(':')[1] if device else ''
    sub_device = request.POST.get('sub_device', '')
    brand = request.POST.get('brand', '')
    model = request.POST.get('model', '')
    purchase_date = request.POST.get('purchase_date', '')
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    email_id = request.POST.get('email_id', '')
    mobile_number = request.POST.get('mobile_number', '')
    imei_serial_no = request.POST.get('imei_serial_no', '')
    term_type = request.POST.get('term_type', '')
    device_value = request.POST.get('device_value', '')
    device_currency = request.POST.get('device_currency', '')
    salesperson_email = request.user
    try:
        inserted_id = PartnersDAO.insert_partners_offline_policy_data(
            data={
                'popd_partner_code': partner_code,
                'popd_location': location,
                'popd_invoice_no': invoice_number,
                'popd_device': device,
                'popd_sub_device': sub_device,
                'popd_brand': brand,
                'popd_model': model,
                'popd_purchase_month': purchase_date,
                'popd_first_name': first_name,
                'popd_last_name': last_name,
                'popd_email': email_id,
                'popd_mobile_number': mobile_number,
                'popd_imei_serial_no': imei_serial_no if imei_serial_no is not '' else '',
                'popd_term_type': term_type,
                'popd_invoice_value': device_value if device_value is not '' else 0.00,
                'popd_device_currency': device_currency,
                'popd_sku': sku,
                'popd_salesperson_email': salesperson_email,
            }
        )
        print(":inserted_id:", inserted_id)
    except Exception as e:
        print(f"partner offline insert Error \t::", e)
        inserted_id = insertedid
    return {'inserted_id': inserted_id}


def helper_insert_into_popd_lebanon(request, partner_code):
    print("\n\n"), print("helper_insert_into_popd_lebanon \t:", request.POST), print("\n\n")
    inserted_id = None
    invoice_number = request.POST.get('invoice_number', '')
    sku = request.POST.get('sku', '')
    location = request.POST.get('location', '')
    category_id = request.POST.get('category', '')
    device = helper_get_category(partner_code)[int(category_id)]
    sub_device = request.POST.get('sub_device', '')
    brand = request.POST.get('brand', '')
    model = request.POST.get('model', '')
    purchase_date = request.POST.get('purchase_date', '')
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    email_id = request.POST.get('email_id', '')
    mobile_number = request.POST.get('mobile_number', '')
    imei_serial_no = request.POST.get('imei_serial_no', '')
    term_type = request.POST.get('term_type', '')

    device_value = float(request.POST.get('device_value', 0))

    key = None
    if device == "Mobile Phone":
        device = "Mobile Phones"
        if device_value <= 900:
            key = '900_and_below'
        else:
            key = '901_and_above'

    if device == "Tablet":
        device = "Tablets"
        if device_value <= 500:
            key = '500_and_below'
        elif 501 <= device_value <= 700:
            key = '501_and_700'
        elif 701 <= device_value <= 900:
            key = '7001_and_900'
        else:
            key = '901_and_above'

    if device == "Laptop":
        device = "Laptops"
        if device_value <= 1000:
            key = '1000_and_below'
        elif 1000 <= device_value <= 2000:
            key = '1000_and_1200'
        elif 1201 <= device_value <= 1400:
            key = '1201_and_1400'
        elif 1401 <= device_value <= 1800:
            key = '1401_and_1800'
        elif 1801 <= device_value <= 2300:
            key = '1801_and_2300'
        elif 2301 <= device_value <= 2900:
            key = '2301_and_2900'
        else:
            key = '2901_and_above'

    if device == "Smart Watch":
        if device_value <= 400:
            key = '400_and_below'
        elif 401 <= device_value <= 800:
            key = '401_and_800'
        elif 801 <= device_value <= 1200:
            key = '801_and_1200'
        else:
            key = '1201_and_above'

    if device == "Airpods":
        if device_value <= 500:
            key = '500_and_below'
        else:
            key = '501_and_above'

    plan_price = helper_price(partner_code)[device][term_type][key]
    plan_tax = 0.05 * plan_price
    plan_total_price = plan_price + plan_tax

    device_currency = request.POST.get('device_currency', '')
    salesperson_email = request.user
    try:
        inserted_id = PartnersDAO.insert_partners_offline_policy_data(
            data={
                'popd_partner_code': partner_code,
                'popd_location': location,
                'popd_invoice_no': invoice_number,
                'popd_device': device,
                'popd_sub_device': sub_device,
                'popd_brand': brand,
                'popd_model': model,
                'popd_purchase_month': purchase_date,
                'popd_first_name': first_name,
                'popd_last_name': last_name,
                'popd_email': email_id,
                'popd_mobile_number': mobile_number,
                'popd_imei_serial_no': imei_serial_no if imei_serial_no else '',
                'popd_term_type': term_type,
                'popd_invoice_value': device_value if device_value else 0.00,
                'popd_plan_price': plan_price,
                'popd_plan_tax': plan_tax,
                'popd_plan_total_price': plan_total_price,
                'popd_device_currency': device_currency,
                'popd_sku': sku,
                'popd_salesperson_email': salesperson_email,
            }
        )
        print(":inserted_id:", inserted_id)
    except Exception as e:
        print(f"partner offline insert Error \t::", e)
        inserted_id = inserted_id
    return {'inserted_id': inserted_id}


def helper_insert_into_popd_istyle_oman(request, partner_code):
    print("\n\n"), print("helper_insert_into_popd_istyle_oman \t:", request.POST), print("\n\n")
    inserted_id = None
    invoice_number = request.POST.get('invoice_number', '')
    sku = request.POST.get('sku', '')
    location = request.POST.get('location', '')
    category_id = request.POST.get('category', '')
    # device = helper_get_category(partner_code)[int(category_id)]
    device = category_id.split(':')[1]
    sub_device = request.POST.get('sub_device', '')
    brand = request.POST.get('brand', '')
    model = request.POST.get('model', '')
    purchase_date = request.POST.get('purchase_date', '')
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    email_id = request.POST.get('email_id', '')
    mobile_number = request.POST.get('mobile_number', '')
    imei_serial_no = request.POST.get('imei_serial_no', '')
    term_type = request.POST.get('term_type', '')

    device_value = float(request.POST.get('device_value', 0))

    key = None
    if device == "iPhone":
        if device_value <= 900:
            key = '900_and_below'
        else:
            key = '901_and_above'

    if device == "iPad":
        if device_value <= 500:
            key = '500_and_below'
        elif 501 <= device_value <= 700:
            key = '501_and_700'
        elif 701 <= device_value <= 900:
            key = '7001_and_900'
        else:
            key = '901_and_above'

    if device == "Mac":
        if device_value <= 1000:
            key = '1000_and_below'
        elif 1000 <= device_value <= 2000:
            key = '1000_and_1200'
        elif 1201 <= device_value <= 1400:
            key = '1201_and_1400'
        elif 1401 <= device_value <= 1800:
            key = '1401_and_1800'
        elif 1801 <= device_value <= 2300:
            key = '1801_and_2300'
        elif 2301 <= device_value <= 2900:
            key = '2301_and_2900'
        else:
            key = '2901_and_above'

    if device == "Apple Watch":
        if device_value <= 400:
            key = '400_and_below'
        elif 401 <= device_value <= 800:
            key = '401_and_800'
        elif 801 <= device_value <= 1200:
            key = '801_and_1200'
        else:
            key = '1201_and_above'

    if device == "Airpods":
        if device_value <= 500:
            key = '500_and_below'
        else:
            key = '501_and_above'

    print('device \t:', device)
    print('term_type \t:', term_type)
    print('key \t:', key)
    plan_price = helper_price(partner_code)[device][term_type][key]
    plan_tax = 0.05 * plan_price
    plan_total_price = plan_price + plan_tax
    print('plan_price \t:', plan_price)
    print('plan_tax \t:', plan_tax)
    print('plan_total_price \t:', plan_total_price), print()

    device_currency = request.POST.get('device_currency', '')
    salesperson_email = request.user
    device_dict = {'iPhone': 'Mobile Phones', 'iPad': 'Tablets', 'Mac': 'Laptops', 'Apple Watch': 'Smart Watch', 'Airpods': 'Airpods'}
    try:
        inserted_id = PartnersDAO.insert_partners_offline_policy_data(
            data={
                'popd_partner_code': partner_code,
                'popd_location': location,
                'popd_invoice_no': invoice_number,
                'popd_device': device_dict[device],
                'popd_sub_device': sub_device,
                'popd_brand': brand,
                'popd_model': model,
                'popd_purchase_month': purchase_date,
                'popd_first_name': first_name,
                'popd_last_name': last_name,
                'popd_email': email_id,
                'popd_mobile_number': mobile_number,
                'popd_imei_serial_no': imei_serial_no if imei_serial_no else '',
                'popd_term_type': term_type,
                'popd_invoice_value': device_value if device_value else 0.00,
                'popd_plan_price': plan_price,
                'popd_plan_tax': plan_tax,
                'popd_plan_total_price': plan_total_price,
                'popd_device_currency': device_currency,
                'popd_sku': sku,
                'popd_salesperson_email': salesperson_email,
            }
        )
        print("inserted_id \t:", inserted_id)
    except Exception as e:
        print(f"partner offline insert Error \t::", e)
        inserted_id = inserted_id
    return {'inserted_id': inserted_id}



def helper_insert_into_popd_oman(request, partner_code):
    print("\n\n"), print("insert_into_partneroffline \t:", request.POST), print("\n\n")
    inserted_id = None
    invoice_number = request.POST.get('invoice_number', '')
    sku = request.POST.get('sku', '')
    location = request.POST.get('location', '')
    category_id = request.POST.get('category', '')
    device = helper_get_category(partner_code)[int(category_id)]
    sub_device = request.POST.get('sub_device', '')
    brand = request.POST.get('brand', '')
    model = request.POST.get('model', '')
    purchase_date = request.POST.get('purchase_date', '')
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    email_id = request.POST.get('email_id', '')
    mobile_number = request.POST.get('mobile_number', '')
    imei_serial_no = request.POST.get('imei_serial_no', '')
    term_type = request.POST.get('term_type', '')

    device_value = float(request.POST.get('device_value', 0))

    key = None
    if device == "Iphone":
        device = "Iphones"
        if device_value <= 900:
            key = '900_and_below'
        else:
            key = '901_and_above'

    if device == "Ipad":
        device = "Ipads"
        if device_value <= 500:
            key = '500_and_below'
        elif 501 <= device_value <= 700:
            key = '501_and_700'
        elif 701 <= device_value <= 900:
            key = '7001_and_900'
        else:
            key = '901_and_above'

    if device == "Mac":
        device = "Macs"
        if device_value <= 1000:
            key = '1000_and_below'
        elif 1000 <= device_value <= 2000:
            key = '1000_and_1200'
        elif 1201 <= device_value <= 1400:
            key = '1201_and_1400'
        elif 1401 <= device_value <= 1800:
            key = '1401_and_1800'
        elif 1801 <= device_value <= 2300:
            key = '1801_and_2300'
        elif 2301 <= device_value <= 2900:
            key = '2301_and_2900'
        else:
            key = '2901_and_above'

    if device == "Iwatch":
        if device_value <= 400:
            key = '400_and_below'
        elif 401 <= device_value <= 800:
            key = '401_and_800'
        elif 801 <= device_value <= 1200:
            key = '801_and_1200'
        else:
            key = '1201_and_above'

    if device == "Airpods":
        if device_value <= 500:
            key = '500_and_below'
        else:
            key = '501_and_above'

    plan_price = helper_price(partner_code)[device][term_type][key]
    plan_tax = 0.05 * plan_price
    plan_total_price = plan_price + plan_tax

    device_currency = request.POST.get('device_currency', '')
    salesperson_email = request.user
    try:
        inserted_id = PartnersDAO.insert_partners_offline_policy_data(
            data={
                'popd_partner_code': partner_code,
                'popd_location': location,
                'popd_invoice_no': invoice_number,
                'popd_device': device,
                'popd_sub_device': sub_device,
                'popd_brand': brand,
                'popd_model': model,
                'popd_purchase_month': purchase_date,
                'popd_first_name': first_name,
                'popd_last_name': last_name,
                'popd_email': email_id,
                'popd_mobile_number': mobile_number,
                'popd_imei_serial_no': imei_serial_no if imei_serial_no is not '' else '',
                'popd_term_type': term_type,
                'popd_invoice_value': device_value if device_value is not '' else 0.00,
                'popd_plan_price': plan_price,
                'popd_plan_tax': plan_tax,
                'popd_plan_total_price': plan_total_price,
                'popd_device_currency': device_currency,
                'popd_sku': sku,
                'popd_salesperson_email': salesperson_email,
            }
        )
        print(":inserted_id:", inserted_id)
    except Exception as e:
        print(f"partner offline insert Error \t::", e)
        inserted_id = inserted_id
    return {'inserted_id': inserted_id}


def helper_insert_into_popd_morocco(request, partner_code):
    print("\n\n"), print("insert_into_partneroffline \t:", request.POST), print("\n\n")
    inserted_id = None
    invoice_number = request.POST.get('invoice_number', '')
    sku = request.POST.get('sku', '')
    location = request.POST.get('location', '')
    category_id = request.POST.get('category', '')
    device = helper_get_category(partner_code)[int(category_id)]
    sub_device = request.POST.get('sub_device', '')
    brand = request.POST.get('brand', '')
    model = request.POST.get('model', '')
    purchase_date = request.POST.get('purchase_date', '')
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    email_id = request.POST.get('email_id', '')
    mobile_number = request.POST.get('mobile_number', '')
    imei_serial_no = request.POST.get('imei_serial_no', '')
    term_type = request.POST.get('term_type', '')

    device_value = float(request.POST.get('device_value', 0))

    key = None
    if device == "Iphone":
        device = "Iphones"
        if device_value <= 900:
            key = '900_and_below'
        else:
            key = '901_and_above'

    if device == "Ipad":
        device = "Ipads"
        if device_value <= 500:
            key = '500_and_below'
        elif 501 <= device_value <= 700:
            key = '501_and_700'
        elif 701 <= device_value <= 900:
            key = '7001_and_900'
        else:
            key = '901_and_above'

    if device == "Mac":
        device = "Macs"
        if device_value <= 1000:
            key = '1000_and_below'
        elif 1000 <= device_value <= 2000:
            key = '1000_and_1200'
        elif 1201 <= device_value <= 1400:
            key = '1201_and_1400'
        elif 1401 <= device_value <= 1800:
            key = '1401_and_1800'
        elif 1801 <= device_value <= 2300:
            key = '1801_and_2300'
        elif 2301 <= device_value <= 2900:
            key = '2301_and_2900'
        else:
            key = '2901_and_above'

    if device == "Iwatch":
        if device_value <= 400:
            key = '400_and_below'
        elif 401 <= device_value <= 800:
            key = '401_and_800'
        elif 801 <= device_value <= 1200:
            key = '801_and_1200'
        else:
            key = '1201_and_above'

    if device == "Airpods":
        if device_value <= 500:
            key = '500_and_below'
        else:
            key = '501_and_above'

    plan_price = helper_price(partner_code)[device][term_type][key]
    plan_tax = 0.05 * plan_price
    plan_total_price = plan_price + plan_tax

    device_currency = request.POST.get('device_currency', '')
    salesperson_email = request.user
    try:
        inserted_id = PartnersDAO.insert_partners_offline_policy_data(
            data={
                'popd_partner_code': partner_code,
                'popd_location': location,
                'popd_invoice_no': invoice_number,
                'popd_device': device,
                'popd_sub_device': sub_device,
                'popd_brand': brand,
                'popd_model': model,
                'popd_purchase_month': purchase_date,
                'popd_first_name': first_name,
                'popd_last_name': last_name,
                'popd_email': email_id,
                'popd_mobile_number': mobile_number,
                'popd_imei_serial_no': imei_serial_no if imei_serial_no is not '' else '',
                'popd_term_type': term_type,
                'popd_invoice_value': device_value if device_value is not '' else 0.00,
                'popd_plan_price': plan_price,
                'popd_plan_tax': plan_tax,
                'popd_plan_total_price': plan_total_price,
                'popd_device_currency': device_currency,
                'popd_sku': sku,
                'popd_salesperson_email': salesperson_email,
            }
        )
        print(":inserted_id:", inserted_id)
    except Exception as e:
        print(f"partner offline insert Error \t::", e)
        inserted_id = inserted_id
    return {'inserted_id': inserted_id}


def get_create_plan_data(prod_id=None, ctm_id=None, slab_codes=None):
    error = "prod_id is missing" if prod_id is None or prod_id == 0 else None
    create_plan_data = {}
    plan_price_info = {}
    make_item_info = {}
    category_info = {}

    category_data = MasterDAO.get_category(cat_prod_id=prod_id)
    category_ids = ""

    if len(category_data) > 0:
        for category in category_data:
            category_info[category['cat_id']] = {}
            category_info[category['cat_id']]['cat_id'] = category['cat_id']
            category_info[category['cat_id']]['cat_code'] = category['cat_code']
            category_info[category['cat_id']]['cat_name'] = category['cat_name']
            category_ids += str(category['cat_id']) + ","

        category_ids = category_ids[:-1]

    if ctm_id is not None and ctm_id == 3:
        category_info = {}
        item_data = MasterDAO.get_item(column="GROUP_CONCAT(DISTINCT item_cat_id) AS cat_ids",
                                       category_ids=category_ids, price_slab=slab_codes)

        if len(item_data) > 0:
            category_ids = item_data[0]['cat_ids']
            category_data = MasterDAO.get_category(cat_id=category_ids)

            if len(category_data) > 0:
                for category in category_data:
                    category_info[category['cat_id']] = {}
                    category_info[category['cat_id']]['cat_id'] = category['cat_id']
                    category_info[category['cat_id']]['cat_code'] = category['cat_code']
                    category_info[category['cat_id']]['cat_name'] = category['cat_name']

    create_plan_data = {"category_info": category_info, "category_ids": category_ids}
    return create_plan_data


def helper_get_brand_model(category_id=None, ctm_id=None, slab_codes=None):
    error = "category_id is missing" if category_id is None or category_id.strip() == "" else None
    error = error if error is not None else "ctm_id is missing" if ctm_id is None or ctm_id.strip() == "" else error

    make_ids = ""
    make_item_info = {}
    item_info = {}
    make_info = MasterDAO.get_make(category_id=category_id)
    print('make_info:: ', make_info)
    slab_codes = slab_codes if slab_codes != "" and ',' in slab_codes else None

    if error is None and int(ctm_id) == 3:
        make_info = {}
        item_data = MasterDAO.get_item(column="GROUP_CONCAT(DISTINCT item_make_id) AS make_ids",
                                       category_id=category_id, price_slab=slab_codes)

        if len(item_data) > 0:
            make_ids = item_data[0]['make_ids']
            make_info = MasterDAO.get_make(category_id=category_id, make_ids=make_ids)

    if error is None and len(make_info) > 0:
        item_data = {}
        item_data = MasterDAO.get_item(item_make_ids=make_ids, price_slab=slab_codes, category_ids=category_id)
        print('item_data:: ', item_data)

        if len(item_data) > 0:
            for item in item_data:
                item_key_name = item['item_name'] + ":" + str(item['item_id'])
                item_make_id = item['item_make_id']

                if item_make_id not in item_info:
                    item_info[item_make_id] = {}

                item_info[item_make_id][item_key_name] = {}
                item_info[item_make_id][item_key_name]['item_id'] = item['item_id']
                item_info[item_make_id][item_key_name]['item_code'] = item['item_code']
                item_info[item_make_id][item_key_name]['item_name'] = item['item_name']
                item_info[item_make_id][item_key_name]['item_price_slab'] = item['item_price_slab']
                item_info[item_make_id][item_key_name]['item_cat_code'] = item['item_cat_code']
                item_info[item_make_id][item_key_name]['item_cat_id'] = item['item_cat_id']
                item_info[item_make_id][item_key_name]['item_make_code'] = item['item_make_code']
                item_info[item_make_id][item_key_name]['item_make_id'] = item['item_make_id']

        for make in make_info:
            if make['make_id'] in item_info and len(item_info[make['make_id']]) > 0:
                make_key_name = make['make_name'] + ":" + str(make['make_id'])
                make_item_info[make_key_name] = {}
                make_item_info[make_key_name]['make_id'] = make['make_id']
                make_item_info[make_key_name]['make_code'] = make['make_code']
                make_item_info[make_key_name]['make_name'] = make['make_name']
                make_item_info[make_key_name]['item'] = item_info[make['make_id']] if make[
                                                                                          'make_id'] in item_info else {}

    print('make_item_info::', make_item_info)
    return make_item_info


def helper_get_item(brand, category_id):
    error = "category_id is missing" if brand is None or brand.strip() == "" else None
    error = error if error is not None else "brand" if brand is None or brand.strip() == "" else error

    item_data = MasterDAO.get_item_all(
        column='item_id, item_code, item_name, item_price_slab, item_base_value',
        condition={'item_make_code': brand, 'item_cat_id': category_id, 'item_status': 'active'}
    )
    return item_data


def helper_get_plan_price(month_key=None, price_slab=None, category=None, plan_type=None):
    error = None
    error = 'Month Key is Invalid' if month_key in ['', None] else None
    error = error if error else 'Price Slab is Invalid' if price_slab in ['', None] else None
    price_data = {}

    if month_key == '0_12':
        price_data = MasterDAO.get_plan(prod_id=1, cat_id=category, plan_type=plan_type, plan_slab_code=price_slab,
                                        package='COMPREHENSIVE', price_type='DTOC')
        price_data = price_data[0] if len(price_data) > 0 else {}
    else:
        ew_price_data = ew_price_config(prod_id=1)
        price_data = ew_price_data[plan_type]

    status = True if error is None else False

    response = {
        "status": ("OK" if status else "NOK"),
        "code": ("200" if status else "201"),
        "message": 'Oops ! Some error occured while processing request. Please contact Protect4Less Technical Team.',
        "messageDesc": error,
        "responseData": {'price_data': price_data}
    }

    return response


def helper_get_partneroffline_data(request, partner_code):
    # partner_code = request.session['partner_code'] if 'partner_code' in request.session else partner_code
    init_info = InitInfo.init(request)
    partner_code = init_info['partner_code']
    # print(":partner_code:",partner_code)

    # print('\n==================================================\n')
    # print("init_info ", init_info)
    # print("\npartner_code ", partner_code)
    # print('\n==================================================\n')

    query_condition = {"popd_partner_code": partner_code, }
    if not init_info['is_master_user']: query_condition["popd_salesperson_email"] = init_info['user_email_id']

    print("\n\n"), print("query_condition \t:", query_condition), print("\n\n")
    popd_data = {}
    partners_offline_policy_data = PartnersDAO.get_partners_offline_policy_data(
        column="popd_id, popd_invoice_no, popd_sku, popd_device, popd_brand, popd_model, popd_purchase_month, popd_first_name, popd_last_name, popd_email, popd_mobile_number, popd_imei_serial_no, popd_term_type, popd_device_value, popd_device_currency, popd_s_id, popd_up_id, popd_tran_id, popd_policy_no, popd_comment, popd_status",
        condition=query_condition,
        order_col='popd_addedon',
        order_by='DESC'
    )

    if len(partners_offline_policy_data) > 0:
        popd_data = partners_offline_policy_data
    return popd_data


def helper_get_partners_generate_payement_link_data(request, partner_code):
    init_info = InitInfo.init(request)
    partner_code = init_info['partner_code']
    print(":partner_code:", partner_code)
    popd_data = {}

    # This is for the Master User who can see all his sales person entries
    condition_query = {"pgpl_partner_code": partner_code}

    # This will get only those entries which are created by the respective sales person.
    if not init_info['is_master_user']:
        condition_query = {"pgpl_partner_code": partner_code, 'pgpl_salesperson_email': request.user.email}

    partners_offline_policy_data = PartnersDAO.get_partners_generate_payement_link_data(condition=condition_query,
                                                                                        order_col='pgpl_addedon',
                                                                                        order_by='DESC')

    if len(partners_offline_policy_data) > 0:
        popd_data = partners_offline_policy_data
    return popd_data


def helper_get_category(partner_code):
    prod_id = Common.partner_dict[partner_code]['prod_id']
    geo = Common.partner_dict[partner_code]['geo']
    # category_data = MasterDAO.get_category(cat_geo = geo,cat_prod_id = prod_id, cat_status_check = False)
    category_data = Common.partner_dict[partner_code]["category_data"]
    return category_data


def helper_plan_type(partner_code):
    return Common.partner_dict[partner_code]["plan_types"]


def helper_price(partner_code):
    partner_dict = Common.partner_dict[partner_code]
    plan_prices = partner_dict["price"]
    return plan_prices


def helper_get_bsquaredwifi_data(request, partner_code):
    # partner_code = request.session['partner_code'] if 'partner_code' in request.session else partner_code
    init_info = InitInfo.init(request)
    partner_code = init_info['partner_code']
    print(":partner_code:", partner_code)
    popd_data = {}
    bsquaredwifi_policy_data = PartnersDAO.get_bsquaredwifi_policy_data(
        column="bw_id, bw_invoice_no, bw_sku, bw_device, bw_brand, bw_model, bw_purchase_month, bw_first_name, bw_last_name, bw_email, bw_mobile_number, bw_imei_serial_no, bw_term_type, bw_device_value, bw_device_currency, bw_s_id, bw_up_id, bw_tran_id, bw_policy_no, bw_comment, bw_status",
        condition={"bw_partner_code": partner_code}, order_col='bw_addedon', order_by='DESC')

    if len(bsquaredwifi_policy_data) > 0:
        bw_data = bsquaredwifi_policy_data
        return bw_data
    else:
        return "{}"


def helper_quix_standard_plan_price(month_key, plan_type, price_slab):
    print('month_key:: ', month_key)
    print('plan_type:: ', plan_type)
    print('device_value:: ', price_slab)
    error = None
    status = False
    price_data = {}
    quix_plan_config = {
        'standard_plan': {
            '0_12': {
                'below_1000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 125, 'plan_actual_price': 125, 'plan_unit': 'AED',
                               'plan_tax': 6.25, 'plan_total_price': 131.25, }
                },
                'between_1000_2000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 250, 'plan_actual_price': 250, 'plan_unit': 'AED',
                               'plan_tax': 12.50, 'plan_total_price': 262.50, }
                },
                'between_2000_3000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 374, 'plan_actual_price': 374, 'plan_unit': 'AED',
                               'plan_tax': 18.70, 'plan_total_price': 392.70, }
                },
                'between_3000_4000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 499, 'plan_actual_price': 499, 'plan_unit': 'AED',
                               'plan_tax': 24.95, 'plan_total_price': 523.95, }
                },
                'between_4000_5000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 624, 'plan_actual_price': 624, 'plan_unit': 'AED',
                               'plan_tax': 31.20, 'plan_total_price': 655.20, }
                },
                'above_5000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 936, 'plan_actual_price': 936, 'plan_unit': 'AED',
                               'plan_tax': 46.80, 'plan_total_price': 982.80, }
                }
            },
            '12_24': {
                'below_1000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 125, 'plan_actual_price': 125, 'plan_unit': 'AED',
                               'plan_tax': 6.25, 'plan_total_price': 131.25, }
                },
                'between_1000_2000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 250, 'plan_actual_price': 250, 'plan_unit': 'AED',
                               'plan_tax': 12.50, 'plan_total_price': 262.50, }
                },
                'between_2000_3000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 374, 'plan_actual_price': 374, 'plan_unit': 'AED',
                               'plan_tax': 18.70, 'plan_total_price': 392.70, }
                },
                'between_3000_4000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 499, 'plan_actual_price': 499, 'plan_unit': 'AED',
                               'plan_tax': 24.95, 'plan_total_price': 523.95, }
                },
                'between_4000_5000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 624, 'plan_actual_price': 624, 'plan_unit': 'AED',
                               'plan_tax': 31.20, 'plan_total_price': 655.20, }
                },
                'above_5000': {
                    'yearly': {'plan_type': 'yearly', 'plan_title': 'Yearly', 'plan_type_code': 'PY',
                               'plan_discount': 0, 'plan_price': 936, 'plan_actual_price': 936, 'plan_unit': 'AED',
                               'plan_tax': 46.80, 'plan_total_price': 982.80, }
                }
            }
        },
        'ew_only': {
            '0_12': {
                'below_1000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 81.90, 'plan_actual_price': 117, 'plan_unit': 'AED',
                               'plan_tax': 4.10, 'plan_total_price': 86, }
                },
                'between_1000_2000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 113.75, 'plan_actual_price': 162.5,
                               'plan_unit': 'AED', 'plan_tax': 5.69, 'plan_total_price': 119.44, }
                },
                'between_2000_3000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 159.25, 'plan_actual_price': 227.5,
                               'plan_unit': 'AED', 'plan_tax': 7.96, 'plan_total_price': 167.21, }
                },
                'between_3000_4000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 182, 'plan_actual_price': 260, 'plan_unit': 'AED',
                               'plan_tax': 9.10, 'plan_total_price': 191.10, }
                },
                'between_4000_5000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 227.50, 'plan_actual_price': 325.0,
                               'plan_unit': 'AED', 'plan_tax': 11.38, 'plan_total_price': 238.88, }
                },
                'above_5000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 318.50, 'plan_actual_price': 455, 'plan_unit': 'AED',
                               'plan_tax': 15.93, 'plan_total_price': 334.43, }
                },
            },
            '12_24': {
                'below_1000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 81.90, 'plan_actual_price': 117, 'plan_unit': 'AED',
                               'plan_tax': 4.10, 'plan_total_price': 86, }
                },
                'between_1000_2000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 81.90, 'plan_actual_price': 117, 'plan_unit': 'AED',
                               'plan_tax': 4.10, 'plan_total_price': 86, }
                },
                'between_2000_3000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 81.90, 'plan_actual_price': 117, 'plan_unit': 'AED',
                               'plan_tax': 4.10, 'plan_total_price': 86, }
                },
                'between_3000_4000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 91, 'plan_actual_price': 130, 'plan_unit': 'AED',
                               'plan_tax': 4.55, 'plan_total_price': 95.55, }
                },
                'between_4000_5000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 113.75, 'plan_actual_price': 162.5,
                               'plan_unit': 'AED', 'plan_tax': 5.69, 'plan_total_price': 119.44, }
                },
                'above_5000': {
                    'yearly': {'plan_type': '12 months EW', 'plan_title': '12 months EW', 'plan_type_code': 'PEW12M',
                               'plan_discount': 30, 'plan_price': 159.25, 'plan_actual_price': 227.5,
                               'plan_unit': 'AED', 'plan_tax': 7.96, 'plan_total_price': 167.21, }
                },
            }
        }
    }

    try:
        price_data = quix_plan_config[plan_type][month_key][price_slab]['yearly']
        status = True
    except Exception as e:
        error = e
        status = False

    response = {
        "status": ("OK" if status else "NOK"),
        "code": ("200" if status else "201"),
        "message": 'Oops ! Some error occured while processing request. Please contact Protect4Less Technical Team.',
        "messageDesc": error,
        "responseData": {'price_data': price_data}
    }

    return response


def helper_get_devicevalue(device_cost):
    device_cost = float(device_cost)
    print('device_cost:: ', device_cost)
    if device_cost < 1000:
        return 'below_1000'
    elif device_cost >= 1000 and device_cost < 2000:
        return 'between_1000_2000'
    elif device_cost >= 2000 and device_cost < 3000:
        return 'between_2000_3000'
    elif device_cost >= 3000 and device_cost < 4000:
        return 'between_3000_4000'
    elif device_cost >= 4000 and device_cost < 5000:
        return 'between_4000_5000'
    elif device_cost >= 5000:
        return 'above_5000'
    return True


def custom_list_view(partner_code):
    query = 'Select popd_id, popd_invoice_no, popd_policy_no, popd_term_type, up_policy_starton, up_policy_endon, popd_sub_device, popd_brand, popd_model, popd_imei_serial_no, popd_purchase_month, popd_first_name, popd_last_name, popd_email, popd_mobile_number, popd_comment, up_policy_status_name FROM ' + config(
        'P4L_DB_NAME') + '.`partners_offline_policy_data`, ' + config(
        'P4L_DB_NAME') + '.`policy_userpolicy` WHERE ' + config(
        'P4L_DB_NAME') + '.`partners_offline_policy_data`.popd_policy_no = ' + config(
        'P4L_DB_NAME') + '.`policy_userpolicy`.up_policy_no and ' + config(
        'P4L_DB_NAME') + '.`partners_offline_policy_data`.popd_partner_code = ' + partner_code + ' and ' + config(
        'P4L_DB_NAME') + '.`partners_offline_policy_data`.popd_status = "done" order by popd_addedon desc;'
    cursor = connection.cursor()
    cursor.execute(query)
    # print("\n\n"), print("partneroffline_data query \t:", query), print("\n\n")
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]