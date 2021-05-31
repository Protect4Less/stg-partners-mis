from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .helper import *
# Create your views here.

def initiate(request, partner_code):
	print(request.POST)

	partner_code = request.GET.get('partner_code',None)

	# This is for generating Payment link
	if partner_code in [1040]:
		payment_link = payment_link_generation(request)
		print(payment_link)
		template_name = 'policy/payment_link_generation.html'
		# context = {'retailer_summary':retailer_summary,'categories_dropdown':categories_dropdown}
		context = {}
		
		return render(request,template_name,context)

	# This is for intserting into PartnerOffline table
	if partner_code in [1000]:
		insert_into_partneroffline(request)
		template_name = 'policy/insert_into_partnercode.html'
		# context = {'retailer_summary':retailer_summary,'categories_dropdown':categories_dropdown}
		context = {}
		# exit()
		return render(request,template_name,context)