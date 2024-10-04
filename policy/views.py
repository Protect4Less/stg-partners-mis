import csv
import io
import json

from backend.classes.InitInfo import InitInfo
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from policy.helper import *


class InitiatePolicyLebanon(View):

    def get(self, request):

        init_info = InitInfo.init(request)
        partner_code = init_info['partner_code']
        if partner_code:
            request.session['partner_code'] = partner_code
            self.partner_code = partner_code
        template_name = 'policy/lebanon_insert_popd_form.html'

        category_dropdown = helper_get_category(partner_code)
        print()
        print("category_dropdown \t:", category_dropdown)
        print()
        plan_type_dropdown = helper_plan_type(partner_code)

        context = {
            "category_dropdown": category_dropdown,
            "plan_type_dropdown": plan_type_dropdown,
            'partner_code': partner_code,
            'partner_location': init_info['partner_location'] if init_info['partner_location'] else "",
        }

        return render(request, template_name, context)

    def post(self, request):

        partner_code = request.session.get('partner_code')
        inserted_id = helper_insert_into_popd_lebanon(request, partner_code)
        if inserted_id is not None or inserted_id != "":
            messages.success(request, 'You have successfully submitted the record. We will process your Policy record shortly To check the latest update please check Policy List.')
            return redirect('policy:listings')
        else:
            messages.error(request, 'Oops! Something went wrong while processing the data. Please contact Protect4Less Technical Team.')

        context = {}
        template_name = 'policy/lebanon_insert_popd_form.html'
        return render(request, template_name, context)
    


class InitiatePolicyOman(View):

    def get(self, request):

        init_info = InitInfo.init(request)
        partner_code = init_info['partner_code']
        if partner_code:
            request.session['partner_code'] = partner_code
            self.partner_code = partner_code
        template_name = 'policy/lebanon_insert_popd_form.html'

        category_dropdown = helper_get_category(partner_code)
        print()
        print("category_dropdown \t:", category_dropdown)
        print()
        plan_type_dropdown = helper_plan_type(partner_code)

        context = {
            "category_dropdown": category_dropdown,
            "plan_type_dropdown": plan_type_dropdown,
            'partner_code': partner_code,
            'partner_location': init_info['partner_location'] if init_info['partner_location'] else "",
        }

        return render(request, template_name, context)

    def post(self, request):

        partner_code = request.session.get('partner_code')
        inserted_id = helper_insert_into_popd_oman(request, partner_code)
        if inserted_id is not None or inserted_id != "":
            messages.success(request, 'You have successfully submitted the record. We will process your Policy record shortly To check the latest update please check Policy List.')
            return redirect('policy:listings')
        else:
            messages.error(request, 'Oops! Something went wrong while processing the data. Please contact Protect4Less Technical Team.')

        context = {}
        template_name = 'policy/lebanon_insert_popd_form.html'
        return render(request, template_name, context)
    

class InitiatePolicyMorocco(View):

    def get(self, request):

        init_info = InitInfo.init(request)
        partner_code = init_info['partner_code']

        if partner_code:
            request.session['partner_code'] = partner_code
            self.partner_code = partner_code

        # if partner_code == '1081':
        #     partner_location = 'Oman'
        # elif partner_code == '1080':
        #     partner_location = 'Morocco'
        # else:
        #     partner_location = 'Unknown'
            
        template_name = 'policy/morocco_insert_popd_form.html'

        category_dropdown = helper_get_category(partner_code)
        print()
        print("category_dropdown \t:", category_dropdown)
        print()
        plan_type_dropdown = helper_plan_type(partner_code)

        context = {
            "category_dropdown": category_dropdown,
            "plan_type_dropdown": plan_type_dropdown,
            'partner_code': partner_code,
            # 'partner_location': partner_location,
            'partner_location': init_info['partner_location'] if init_info['partner_location'] else "",
        }

        return render(request, template_name, context)

    def post(self, request):

        partner_code = request.session.get('partner_code')
        inserted_id = helper_insert_into_popd_morocco(request, partner_code)
        if inserted_id is not None or inserted_id != "":
            messages.success(request, 'You have successfully submitted the record. We will process your Policy record shortly To check the latest update please check Policy List.')
            return redirect('policy:listings')
        else:
            messages.error(request, 'Oops! Something went wrong while processing the data. Please contact Protect4Less Technical Team.')

        context = {}
        template_name = 'policy/morocco_insert_popd_form.html'
        return render(request, template_name, context)
    

def initiate(request):
    # print(request.session['partner_code'])
    # print(type(request.session['partner_code']))

    init_info = InitInfo.init(request)
    partner_code = init_info['partner_code']
    # partner_code = request.session['partner_code'] if 'partner_code' in request.session else None

    # This is for generating Payment link
    if partner_code in ['1034', '1035', '1042']:
        context = helper_payment_link_generation(request)
        # print(payment_link)
        template_name = 'policy/payment_link_generation.html'
        # context = {'retailer_summary':retailer_summary,'categories_dropdown':categories_dropdown}
        # context = {}
        return render(request, template_name, context)

    # This is for inserting into Partner Offline table
    if partner_code != "" and partner_code in ['1032', '1071']:
        if request.method == 'POST':
            inserted_id = helper_insert_into_partneroffline(request, partner_code)
            if inserted_id is not None or inserted_id != "":
                messages.success(request, 'You have successfully submitted the record. We will process your Policy record shortly To check the latest update please check Policy List.')
                return redirect('policy:listings')
            else:
                messages.error(request, 'Oops! Something went wrong while processing the data. Please contact Protect4Less Technical Team.')

        template_name = 'policy/insert_into_partneroffline.html'
        category_dropdown = helper_get_category(partner_code)
        plan_type_dropdown = helper_plan_type(partner_code)
        context = {
            "category_dropdown": category_dropdown,
            "plan_type_dropdown": plan_type_dropdown,
            'partner_code': partner_code,
            'partner_location': init_info['partner_location'] if init_info['partner_location'] else "",
        }
        return render(request, template_name, context)

    return redirect('dashboard:dashboard')


@csrf_exempt
def get_brand_model_ajax(request):
    print(request.POST)
    cat_id = request.POST.get('id', None)
    ctm_id = request.POST.get('ctm_id', None)
    slab_codes = request.POST.get('slab_codes', None)

    make_item_info = {}
    error = "Invalid request" if request.method != "POST" else None
    error = error if error is not None else "Category Id is missing" if cat_id is None or cat_id.strip() == "" else error

    if error is None:
    #cat_id = str(cat_id)
        make_item_info = helper_get_brand_model(category_id = cat_id, ctm_id = ctm_id, slab_codes = slab_codes)
    # print(make_item_info)
    return JsonResponse(make_item_info)


@csrf_exempt
def get_model_ajax(request):
    error = None
    response_data, brand = {}, {}

    error = 'Invalid Request Type' if not request.POST else None
    error = error if error else 'Request is not Ajax Type' if not request.is_ajax else None

    category_id = request.POST.get('category_id', None)
    brand = request.POST.get('brand', None)

    error = "No brand selected" if brand is None or brand == '' else None
    print('error:: ', error)

    model = None
    if error is None:
        model = helper_get_item(brand=brand, category_id=category_id)
        # print('models :: ', model)
        error = error if error is not None else "No data found" if len(model) == 0 else None

    if error is None:
        # response_data = model
        partner_code = request.session.get('partner_code', None)

        if partner_code and int(category_id) == 22:
            seperated_models_to_send = []
            seperated_models = ["iPhone SE", "iPhone 11", "iPhone 12", "iPhone 13", "iPhone 14", "iPhone 15"]
            for s_model in seperated_models:
                for d_dict in model:
                    for k, v in d_dict.items():
                        if k == 'item_name':
                            if s_model.lower() in v.lower() and model not in seperated_models_to_send:
                                seperated_models_to_send.append(d_dict)
            response_data = seperated_models_to_send
        else:
            response_data = model
    status = True if error is None else False

    response = {
        "status": ("OK" if status else "NOK"),
        "code": ("200" if status else "201"),
        "message": error,
        "messageDesc": "",
        "responseData": response_data,
        # "partner_code": partner_code,
    }
    return JsonResponse(response)


@csrf_exempt
def get_plan_price_ajax(request):

    init_info =  InitInfo.init(request)
    partner_code = init_info['partner_code']

    error = None
    item_data = request.POST.get('item_data',None)
    plan_type = request.POST.get('plan_type',None)
    category = request.POST.get('category',None)
    purchase_month = request.POST.get('purchase_month',None)
    device_value = request.POST.get('device_value',None)

    error = 'Invalid Request Type' if not request.POST else None
    error = error if error else 'Request is not Ajax Type' if not request.is_ajax else None

    print('item_data::', item_data)
    print('plan_type::', plan_type)
    print('category::', category)
    print('purchase_month::', purchase_month)
    print('device_value::', device_value)


    item_price = 0.00
    error = 'Invalid Item' if item_data is None else None
    error = error if error else 'Purchase Month is Invalid' if purchase_month is None else None
    error = error if error else 'Category is Invalid' if category is None else None
    error = error if error else 'Plan Type is Invalid' if plan_type is None else None

    item_data_arr = item_data.split(':')

    price_slab = helper_get_devicevalue(item_data_arr[3])
    month_key = purchase_month
    
    if partner_code == "1042":
        # This is Specific only for QUIX partner
        # QUIX will only sell Mobile Phone
        item_price_data = helper_quix_standard_plan_price(month_key = month_key, plan_type = plan_type, price_slab = price_slab )
    else:
         #This is the default pricing we get getting
        item_price_data = helper_get_plan_price(month_key = month_key, price_slab = price_slab, category = category, plan_type = plan_type )

    print('item_price_data:: ', item_price_data)

    error = item_price_data['messageDesc'] if not item_price_data['status'] else None

    item_price = item_price_data['responseData']['price_data'] if error is None else {}

    status = True if error is None else False

    response = {
        "status": ("OK" if status else "NOK"),
        "code": ("200" if status else "201"),
        "message": 'Oops ! Some error occured while processing request. Please contact Protect4Less Technical Team.',
        "messageDesc": error,
        "responseData":{'item_price':item_price}
    }

    return JsonResponse(response)


def listings(request):
    print("\n\n"), print("request.user EmailID \t::", request.user), print("\n\n")
    # This is for inserting into PartnerOffline table
    # print("sess==",request.session['partner_code'])
    # print(type(request.session['partner_code']))
    init_info = InitInfo.init(request)

    print('init_info:: ', init_info)
    partner_code = init_info['partner_code']
    print("\n\n"), print("Listing page partner_code \t::", partner_code), print("\n\n")
    is_payment_link_generation_partner = init_info['is_payment_link_generation_partner']

    # print('\n==================================================\n')
    # print("is_payment_link_generation_partner ", is_payment_link_generation_partner)
    # print('\n==================================================\n')

    # try:
    #     # partner_code = request.session['partner_code'] if 'partner_code' in request.session else None

    # except Exception as e:
    #     partner_code = ""
    #     raise Exception("partner_code not found!")

    # if partner_code !="" and partner_code in ['1032','1044']:

    # This code is for Payment Link Generation Partner
    if is_payment_link_generation_partner:
        template_name = 'policy/listing_partners_generate_payement_link.html'
        payement_link_data = helper_get_partners_generate_payement_link_data(request, partner_code)
        print('payement_link_data==', payement_link_data)
        context = {'payement_link_data': payement_link_data, 'partner_code': partner_code,
                   'host_url': init_info['host_url']}
        return render(request, template_name, context)

    if partner_code != "" and is_payment_link_generation_partner is False:
        template_name = 'policy/listings_partneroffline.html'
        partneroffline_data = custom_list_view(partner_code)
        # print('partneroffline_data==', partneroffline_data)
        context = {'partneroffline_data': partneroffline_data, 'partner_code': partner_code}
        return render(request, template_name, context)


@csrf_exempt
def cat_name_id_ajax(request):
    print("request.POST in cat_name_id_ajax", request.POST)
    cat_name = request.POST.get('name', None)
    print("cat_name cat_name_id_ajax", cat_name)
    
    # Extra Check Added for cat_name if string comes with':'
    cat_name = cat_name.split(':')[0] if cat_name and ':' in cat_name else cat_name
    print("Update Cat_Name", cat_name)

    category_data = {}
    error = "Invalid request" if request.method != "POST" else None
    error = error if error is not None else "Category Name is missing" if cat_name is None or cat_name.strip() == "" else error

    if error is None:
        category_data = MasterDAO.get_category(cat_name=cat_name, cat_status_check=False)
        if len(category_data) > 0:
            category_data = category_data[0]
    return JsonResponse(category_data)


@csrf_exempt
def bulk_upload(request):

    sku_plan_type = {
        'AC000':{
            'plan_desc': "Accidental Below AED 750",
            'plan_type': "PM",
            'plan_price': "3.72",
            'plan_tax': "0.00",
            'plan_total_price': "3.72",
        },
        'AC001':{
            'plan_desc': "Accidental AED 750 - AED 1500",
            'plan_type': "PM",
            'plan_price': "7.45",
            'plan_tax': "0.00",
            'plan_total_price': "7.45",
        },
        'EW000':{
            'plan_desc': "Extended Warranty Below AED 750",
            'plan_type': "PM",
            'plan_price': "1.05",
            'plan_tax': "0.00",
            'plan_total_price': "1.05",
        },
        'EW001':{
            'plan_desc': "Extended Warranty AED 750 - AED 1500",
            'plan_type': "PM",
            'plan_price': "2.10",
            'plan_tax': "0.00",
            'plan_total_price': "2.10",
        },
        'BDACEW000':{
            'plan_desc': "Bundle Accidental + Extended Warranty Below AED 750 ",
            'plan_type': "PM",
            'plan_price': "4.69",
            'plan_tax': "0.00",
            'plan_total_price': "4.69",
        },
        'BDACEW001':{
            'plan_desc': "BBundle Accidental + Extended Warranty AED 750 - AED 1500",
            'plan_type': "PM",
            'plan_price': "9.39",
            'plan_tax': "0.00",
            'plan_total_price': "9.39",
        }
    }

    if len(request.FILES) > 0:

        csv_file = request.FILES['fileToUpload']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload csv file')
            print("\n\n\n\n111111")
            return redirect('policy:bulk-upload')
            print("\n\n\n\n2222222")

        file_data = csv_file.read().decode("utf-8" ,  errors='ignore')

        lines = file_data.split("\n")
        csvData = {}
        cnt = 0
        cnt_uploaded_data = 0
        for line in lines:

            if line != "":
                if cnt != 0:

                    fields = line.split(",")
                    print("\n\n\nfields", fields)


                    insertedid = None
                    sku = fields[0]

                    location = fields[1]
                    device = fields[2]
                    sub_device = fields[3]
                    brand = fields[4]
                    model = fields[5]
                    device_name = fields[6]
                    purchase_momnth = fields[7]
                    policy_start_date = fields[8]
                    ew_start_date = fields[9]
                    first_name = fields[10]
                    last_name = fields[11]
                    email_id = fields[12]
                    mobile_number = fields[13]
                    imei_serial_no = fields[14]
                    term_type = fields[15]

                    if sku in sku_plan_type:
                        plan_desc = sku_plan_type[sku]['plan_desc']
                        plan_type = sku_plan_type[sku]['plan_type']
                        plan_price = sku_plan_type[sku]['plan_price']
                        plan_tax = sku_plan_type[sku]['plan_tax']
                        plan_total_price =  sku_plan_type[sku]['plan_total_price']

                        data= {'bw_partner_code': '1034', 'bw_location':location,'bw_device': device, 'bw_sub_device':sub_device, 'bw_brand':brand, 'bw_model':model, 'bw_purchase_month':purchase_momnth, "bw_policy_start_date":policy_start_date, "bw_ew_start_date":ew_start_date, 'bw_first_name':first_name, 'bw_last_name':last_name, 'bw_email':email_id, 'bw_mobile_number':mobile_number, 'bw_imei_serial_no': imei_serial_no if imei_serial_no is not '' else '', 'bw_term_type':term_type,'bw_device_currency':"AED", 'bw_sku':sku, 'bw_plan_price':plan_price, 'bw_plan_tax':plan_tax, 'bw_plan_total_price':plan_total_price, 'bw_sku':sku , 'bw_plan_type' : plan_type , "bw_device_name" : device_name  }

                        inserted_id = PartnersDAO.insert_bsquaredwifi_offline_policy_data(data)
                    else:
                        messages.error(request, sku+' SKU Not available')


                    cnt_uploaded_data =  cnt_uploaded_data + 1

            cnt = cnt + 1

        messages.success(request, str(cnt_uploaded_data)+ ' Data successfully uploaded')

    context = {}
    partner_code = '1034'
    bsquaredwifi_data = helper_get_bsquaredwifi_data(request,partner_code)
    print('bsquaredwifi_data==',bsquaredwifi_data)
    context = {'bsquaredwifi_data':bsquaredwifi_data, 'partner_code':partner_code}
    template_name = 'policy/bulk_upload_bsquaredwifi.html'
    return render(request,template_name,context)


def download_report(request):
    init_info = InitInfo.init(request)
    partner_code = init_info['partner_code']

    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    print("start_date \t:", start_date)
    print("end_date \t:", end_date)

    context = {'partner_code': partner_code}
    return render(request, 'policy/download_report.html', context)