from backend.dao.MasterDAO import MasterDAO
from backend.dao.PolicyDAO import PolicyDAO
from backend.dao.PartnersDAO import *
from backend.classes.Common import *
from backend.classes.InitInfo import InitInfo
from .config import *

def helper_payment_link_generation(request):
    print(request.POST)

    inserted_id = 0

    init_info =  InitInfo.init(request)

    partner_code = init_info['partner_code']

    if request.method == 'POST':
        #{'csrfmiddlewaretoken': ['H8gVuWtefVznsgvPjo3wSA5ip0QyWm6L9X9RSCLXgdor8Gw2SV3qG0t8yvLAn7ih'], 'category': ['1'], 'brand': ['APPLE:4:APPLE'], 'item': ['15720:S2761-3220:iPhone XS Max, 4GB RAM,64GB STORAGE:2879'], 'purchase_month': ['12_24'], 'plan_type': ['yearly'], 'plan_id': ['10001'], 'sales_person_id': ['12'], 'first_name': ['sumit'], 'last_name': ['nayak'], 'mobile_no': ['9838383832'], 'email_id': ['sumitkumar@gmail.com']}
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

        slab_code = ''

        if error is None:
            item_data = item.split(':')
            slab_code = item_data[1]
            item_id = item_data[0]
            brand_data = brand.split(':')
            brand_code = brand_data[0]  
            brand_id = brand_data[1]
            term_type = 'PM' if plan_type == 'monthly' else 'PY' if plan_type == 'yearly' else ""

        if error is None:
            if purchase_month == '0_12':
                price_data = MasterDAO.get_plan(plan_id = plan_id)
                price_data = price_data[0] if len(price_data) > 0 else {}
            else:
                ew_price_data = ew_price_config(prod_id = 1)
                price_data = ew_price_data[plan_type]

        input_data = {
            'pgpl_partner_code': partner_code,
            'pgpl_slab_code': slab_code,
            'pgpl_plan_id':plan_id,
            'pgpl_plan_price': price_data['plan_price'],
            'pgpl_plan_tax': price_data['plan_tax'],
            'pgpl_plan_total_price': price_data['plan_total_price'],
            'pgpl_plan_currency': price_data['plan_unit'],
            'pgpl_category_id': category,
            'pgpl_brand_id': brand_id,
            'pgpl_brand_code': brand_code,
            'pgpl_item_id': item_id,
            'pgpl_purchase_month': purchase_month,
            'pgpl_first_name': first_name, 
            'pgpl_last_name': last_name,
            'pgpl_email': email_id,
            'pgpl_mobile_number': mobile_no,
            'pgpl_term_type': term_type,
            'pgpl_salesperson_id': sales_person_id
        }

        inserted_id = PolicyDAO.insert_partners_generate_payement_link(input_data)

    category_info = get_create_plan_data(prod_id = 1)
    print('category_info:: ',category_info)
    return {'category_info':category_info['category_info'], 'inserted_id': inserted_id}

def helper_insert_into_partneroffline(request):
    print("::POST::",request.POST)
    insertedid = None
    invoice_number = request.POST.get('invoice_number','')
    sku = request.POST.get('sku','')
    location = request.POST.get('location','')
    device = request.POST.get('category','')
    sub_device = request.POST.get('sub_device','')
    brand = request.POST.get('brand','')
    model = request.POST.get('model','')
    purchase_date = request.POST.get('purchase_date','')
    first_name = request.POST.get('first_name','')
    last_name = request.POST.get('last_name','')
    email_id = request.POST.get('email_id','')
    mobile_number = request.POST.get('mobile_number','')
    imei_serial_no = request.POST.get('imei_serial_no','')
    term_type = request.POST.get('term_type','')
    device_value = request.POST.get('device_value','')
    device_currency = request.POST.get('device_currency','')
    try:
        inserted_id = PartnersDAO.insert_partners_offline_policy_data(data= {'popd_partner_code': '1032', 'popd_location':location,'popd_invoice_no':invoice_number, 'popd_device': device, 'popd_sub_device':sub_device, 'popd_brand':brand, 'popd_model':model, 'popd_purchase_month':purchase_date, 'popd_first_name':first_name, 'popd_last_name':last_name, 'popd_email':email_id, 'popd_mobile_number':mobile_number, 'popd_imei_serial_no': imei_serial_no if imei_serial_no is not '' else '', 'popd_term_type':term_type, 'popd_invoice_value':device_value if device_value is not '' else 0.00, 'popd_device_currency':device_currency, 'popd_sku':sku })
        print(":inserted_id:",inserted_id)
    except Exception as e:
        inserted_id = insertedid
    
    return {'inserted_id': inserted_id}
    

def get_create_plan_data(prod_id = None, ctm_id = None, slab_codes = None):
        error = "prod_id is missing" if prod_id is None or prod_id == 0 else None
        create_plan_data = {}
        plan_price_info = {}
        make_item_info = {}
        category_info = {}

        category_data = MasterDAO.get_category(cat_prod_id = prod_id)
        category_ids = ""

        if len(category_data) > 0:
            for category in category_data:
                category_info[category['cat_id']] = {}
                category_info[category['cat_id']]['cat_id'] = category['cat_id']
                category_info[category['cat_id']]['cat_code'] = category['cat_code']
                category_info[category['cat_id']]['cat_name'] = category['cat_name']
                category_ids += str(category['cat_id'])+","

            category_ids = category_ids[:-1]

        if ctm_id is not None and ctm_id == 3:
            category_info = {}
            item_data = MasterDAO.get_item(column = "GROUP_CONCAT(DISTINCT item_cat_id) AS cat_ids", category_ids = category_ids, price_slab = slab_codes)

            if len(item_data) > 0:
                category_ids = item_data[0]['cat_ids']
                category_data = MasterDAO.get_category(cat_id = category_ids)

                if len(category_data) > 0:
                    for category in category_data:
                        category_info[category['cat_id']] = {}
                        category_info[category['cat_id']]['cat_id'] = category['cat_id']
                        category_info[category['cat_id']]['cat_code'] = category['cat_code']
                        category_info[category['cat_id']]['cat_name'] = category['cat_name']

        create_plan_data = {"category_info":category_info,"category_ids":category_ids}
        return create_plan_data

def helper_get_brand_model(category_id = None, ctm_id = None, slab_codes = None):
        error = "category_id is missing" if category_id is None or category_id.strip() == "" else None
        error = error if error is not None else "ctm_id is missing" if ctm_id is None or ctm_id.strip() == "" else error

        make_ids = ""
        make_item_info = {}
        item_info = {}
        make_info = MasterDAO.get_make(category_id=category_id)
        slab_codes = slab_codes if slab_codes != "" and ',' in slab_codes else None

        if error is None and int(ctm_id) == 3:
            make_info = {}
            item_data = MasterDAO.get_item(column = "GROUP_CONCAT(DISTINCT item_make_id) AS make_ids", category_id = category_id, price_slab = slab_codes)

            if len(item_data) > 0:
                make_ids = item_data[0]['make_ids']
                make_info = MasterDAO.get_make(category_id=category_id, make_ids = make_ids)

        if error is None and len(make_info) > 0:
            item_data = {}
            item_data = MasterDAO.get_item(item_make_ids = make_ids, price_slab = slab_codes, category_ids = category_id)

            if len(item_data) > 0:
                for item in item_data:
                    item_key_name = item['item_name']+":"+str(item['item_id'])
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
                    make_key_name = make['make_name']+":"+str(make['make_id'])
                    make_item_info[make_key_name] = {}
                    make_item_info[make_key_name]['make_id'] = make['make_id']
                    make_item_info[make_key_name]['make_code'] = make['make_code']
                    make_item_info[make_key_name]['make_name'] = make['make_name']
                    make_item_info[make_key_name]['item'] = item_info[make['make_id']] if make['make_id'] in item_info else {}

        return make_item_info

def helper_get_item(brand, category_id):

    error = "category_id is missing" if brand is None or brand.strip() == "" else None
    error = error if error is not None else "brand" if brand is None or brand.strip() == "" else error

    item_data = MasterDAO.get_item_all(column='item_id,item_code, item_name, item_price_slab, item_base_value',condition={'item_make_code':brand, 'item_cat_id': category_id, 'item_status':'active'})

    return item_data

def helper_get_plan_price(month_key = None, price_slab = None, category = None, plan_type = None):

    error = None
    error = 'Month Key is Invalid' if month_key in ['',None] else None
    error = error if error else 'Price Slab is Invalid' if price_slab in ['',None] else None
    price_data = {}

    if month_key == '0_12':
        price_data = MasterDAO.get_plan(prod_id = 1, cat_id = category, plan_type = plan_type, plan_slab_code = price_slab, package = 'COMPREHENSIVE', price_type = 'DTOC')
        price_data = price_data[0] if len(price_data) > 0 else {}
    else:
        ew_price_data = ew_price_config(prod_id = 1)
        price_data = ew_price_data[plan_type]

    status = True if error is None else False

    response = {
        "status": ("OK" if status else "NOK"),
        "code": ("200" if status else "201"),
        "message": 'Oops ! Some error occured while processing request. Please contact Protect4Less Technical Team.',
        "messageDesc": error,
        "responseData":{'price_data':price_data}
    }

    return response

def helper_get_partneroffline_data(request,partner_code):
    # partner_code = request.session['partner_code'] if 'partner_code' in request.session else partner_code
    init_info =  InitInfo.init(request)
    partner_code = init_info['partner_code']
    print(":partner_code:",partner_code)
    popd_data = {}
    partners_offline_policy_data = PartnersDAO.get_partners_offline_policy_data(column = "popd_id, popd_invoice_no, popd_sku, popd_device, popd_brand, popd_model, popd_purchase_month, popd_first_name, popd_last_name, popd_email, popd_mobile_number, popd_imei_serial_no, popd_term_type, popd_device_value, popd_device_currency, popd_s_id, popd_up_id, popd_tran_id, popd_policy_no, popd_comment, popd_status",condition={"popd_partner_code":partner_code})

    if len(partners_offline_policy_data) > 0:
        popd_data = partners_offline_policy_data
    return popd_data    

def helper_get_category(partner_code):
    prod_id = Common.partner_dict[partner_code]['prod_id']
    print(":prod_id:",prod_id)
    geo = Common.partner_dict[partner_code]['geo']
    print(":geo:",geo)
    #category_data = MasterDAO.get_category(cat_geo = geo,cat_prod_id = prod_id, cat_status_check = False)
    category_data = Common.partner_dict[partner_code]["category_data"]
    print(":category_data:",category_data)
    return category_data

def helper_plan_type(partner_code):
    partner_dict = Common.partner_dict[partner_code]
    print(":partner_dict:",partner_dict)
    plan_type = partner_dict["plan_type"]
    print(":plan_type:",plan_type)
    return plan_type