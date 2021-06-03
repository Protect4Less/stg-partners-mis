from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .helper import *
# Create your views here.

def initiate(request):
    print(request.session['partner_code'])
    print(type(request.session['partner_code']))

    partner_code = request.session['partner_code'] if 'partner_code' in request.session else None

    # This is for generating Payment link
    if partner_code in ['1040']:
        payment_link = payment_link_generation(request)
        print(payment_link)
        template_name = 'policy/payment_link_generation.html'
        # context = {'retailer_summary':retailer_summary,'categories_dropdown':categories_dropdown}
        context = {}
        
        return render(request,template_name,context)

    # This is for intserting into PartnerOffline table
    if partner_code in ['1032']:
        if request.method == 'POST':
            insert_into_partneroffline(request)
        template_name = 'policy/insert_into_partneroffline.html'
        context = {}
        return render(request,template_name,context)

def listings(request):
    # This is for intserting into PartnerOffline table
    print(request.session['partner_code'])
    print(type(request.session['partner_code']))

    partner_code = request.session['partner_code'] if 'partner_code' in request.session else None
    if partner_code in ['1032']:
        template_name = 'policy/listings_partneroffline.html'
        partneroffline_data = get_partneroffline_data(request)
        context = {'partneroffline_data':partneroffline_data}
        return render(request,template_name,context)