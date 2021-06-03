from backend.dao.PartnersDAO import *

def payment_link_generation(request):
    pass

def insert_into_partneroffline(request):
    print("::POST::",request.POST)
    invoice_number = request.POST.get('invoice_number','')
    sku = request.POST.get('sku','')
    location = request.POST.get('location','')
    device = request.POST.get('device','')
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

    inserted_id = PartnersDAO.insert_partners_offline_policy_data(data= {'popd_partner_code': '1032', 'popd_invoice_no':invoice_number, 'popd_device': device, 'popd_sub_device':sub_device, 'popd_brand':brand, 'popd_model':model, 'popd_purchase_month':purchase_date, 'popd_first_name':first_name, 'popd_last_name':last_name, 'popd_email':email_id, 'popd_mobile_number':mobile_number, 'popd_imei_serial_no': imei_serial_no if imei_serial_no is not '' else '', 'popd_term_type':term_type, 'popd_invoice_value':device_value if device_value is not '' else 0.00, 'popd_device_currency':device_currency, 'popd_sku':sku })
    print(":inserted_id:",inserted_id)
    

def get_partneroffline_data(request):
    pass