from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .helper import *
# Create your views here.

def initiate(request):
    # print(request.session['partner_code'])
    # print(type(request.session['partner_code']))

    partner_code = request.session['partner_code'] if 'partner_code' in request.session else None
    print(partner_code)
    # This is for generating Payment link
    if partner_code in ['1034']:
        context = helper_payment_link_generation(request)
        # print(payment_link)
        template_name = 'policy/payment_link_generation.html'
        # context = {'retailer_summary':retailer_summary,'categories_dropdown':categories_dropdown}
        # context = {}
        
        return render(request,template_name,context)

    # This is for intserting into PartnerOffline table
    if partner_code in ['1032']:
        if request.method == 'POST':
            inserted_id = helper_insert_into_partneroffline(request)
            if inserted_id is not None or inserted_id != "":
                return redirect('policy:listings')
        template_name = 'policy/insert_into_partneroffline.html'
        category_dropdown = helper_get_category(partner_code)
        print(":category_dropdown:",category_dropdown)
        plan_type_dropdown = helper_plan_type(partner_code)
        print(":plan_type_dropdown:",plan_type_dropdown)
        context = {"category_dropdown":category_dropdown, "plan_type_dropdown":plan_type_dropdown}
        return render(request,template_name,context)

    exit()
    # return redirect('dashboard:logout')

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
    response_data,brand = {},{}

    error = 'Invalid Request Type' if not request.POST else None
    error = error if error else 'Request is not Ajax Type' if not request.is_ajax else None

    category_id = request.POST.get('category_id',None)
    brand = request.POST.get('brand',None)

    error  = "No brand selected" if brand is None or brand  == '' else None

    print('error:: ',error)

    if error is None:
        model = helper_get_item(brand = brand, category_id = category_id )
        print('model:: ', model)
        error = error if error is not None else "No data found" if len(model) == 0 else None
    
    if error is None:
        response_data = model

    status = True if error is None else False

    response = {
        "status": ("OK" if status else "NOK"),
        "code": ("200" if status else "201"),
        "message": error,
        "messageDesc": "",
        "responseData":response_data,
    }
    return JsonResponse(response)

@csrf_exempt
def get_plan_price_ajax(request):
    error = None
    item_data = request.POST.get('item_data',None)
    plan_type = request.POST.get('plan_type',None)
    category = request.POST.get('category',None)
    purchase_month = request.POST.get('purchase_month',None)

    error = 'Invalid Request Type' if not request.POST else None
    error = error if error else 'Request is not Ajax Type' if not request.is_ajax else None

    print('item_data::', item_data)
    print('purchase_month::', plan_type)
    print('purchase_month::', category)
    print('purchase_month::', purchase_month)

    item_price = 0.00
    error = 'Invalid Item' if item_data is None else None
    error = error if error else 'Purchase Month is Invalid' if purchase_month is None else None
    error = error if error else 'Category is Invalid' if category is None else None
    error = error if error else 'Plan Type is Invalid' if plan_type is None else None

    item_data_arr = item_data.split(':')

    price_slab = item_data_arr[1]
    month_key = purchase_month

    item_price_data = helper_get_plan_price(month_key = month_key, price_slab = price_slab, category = category, plan_type = plan_type )
    
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
    # This is for intserting into PartnerOffline table
    print(request.session['partner_code'])
    print(type(request.session['partner_code']))

    partner_code = request.session['partner_code'] if 'partner_code' in request.session else None
    if partner_code in ['1032']:
        template_name = 'policy/listings_partneroffline.html'
        partneroffline_data = helper_get_partneroffline_data(partner_code)
        print('partneroffline_data==',partneroffline_data)
        context = {'partneroffline_data':partneroffline_data}
        return render(request,template_name,context)


@csrf_exempt
def get_cat_id_ajax(request):
    print(request.POST)
    cat_name = request.POST.get('name', None)

    category_data = {}
    error = "Invalid request" if request.method != "POST" else None
    error = error if error is not None else "Category Name is missing" if cat_name is None or cat_name.strip() == "" else error

    if error is None:
        category_data = MasterDAO.get_category(cat_name = cat_name, cat_status_check = False)
        if len(category_data) > 0:
            category_data = category_data[0]
    return JsonResponse(category_data)