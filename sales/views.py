from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backend.dao.PartnersSummaryDAO import PartnersSummaryDAO
from backend.dao.DashboardSummaryDAO import DashboardSummaryDAO

# Create your views here.
# @login_required(login_url='/login')
# def statistics(request):
# 	print(request.POST)
# 	start_date,category_id,plan,end_date = '','','',''

# 	categories_dropdown = PartnersSummaryDAO.get_category(column = 'cat_id,cat_name',condition={'cat_status':'active','cat_p_id':1})
		
# 	if request.method == 'POST':
# 		category_id = request.POST.get("category",'')
# 		plan =  request.POST.get("plan",'')
# 		start_date = request.POST.get("startDate",'')
# 		end_date = request.POST.get("endDate",'')

# 	retailer_summary = PartnersSummaryDAO.get_retailer_summary(user_id = request.user.id, category_id = category_id, plan = plan,start_date = start_date, end_date = end_date)

# 	retailer_mis_user_id = DashboardSummaryDAO.get_retailer_user_id(user_id = request.user.id)

# 	template_name = 'sales/statistics.html'
# 	context = {'retailer_summary':retailer_summary,'categories_dropdown':categories_dropdown,'retailer_mis_user_id':retailer_mis_user_id}
# 	print(context)
# 	return render(request,template_name,context)

@login_required(login_url='/login')
def statistics(request):
	print('\n\n\n\n-----', request.POST , '\n\n\n----')
	start_date,category_id,plan,end_date = '','','',''

	categories_dropdown = PartnersSummaryDAO.get_category(column = 'cat_id,cat_name',condition={'cat_status':'active','cat_p_id':1})
	retailer_mis_user_id = DashboardSummaryDAO.get_retailer_user_id(user_id = request.user.id)
	print(retailer_mis_user_id)
	if request.method == 'POST':
		category_id = request.POST.get("category",'')
		plan =  request.POST.get("plan",'')
		start_date = request.POST.get("startDate",'')
		end_date = request.POST.get("endDate",'')

	if request.POST.get("sbtDownload",'') == '':
		print('########### Search ########')
		retailer_summary = PartnersSummaryDAO.get_retailer_summary(user_id = request.user.id, category_id = category_id, plan = plan,start_date = start_date, end_date = end_date)
	else:
		print('########### Download ########')
		retailer_summary = PartnersSummaryDAO.get_retailer_summary(user_id = request.user.id, category_id = '', plan = '',start_date = start_date, end_date = end_date)

		import csv
		from django.http import HttpResponse
		import os
		from django.conf import settings


		if retailer_mis_user_id > 0:
			csv_columns = ['ps_geo', 'ps_date','ps_category','ps_make','ps_model','ps_plan','ps_price','ps_master_commission_percentage','ps_commission_percentage','ps_master_commisson','ps_commisson','ps_total_acq','ps_total_ren','ps_total_rev','ps_total_commisson']
		else:
			csv_columns = ['ps_geo', 'ps_date','ps_category','ps_make','ps_model','ps_plan','ps_price','ps_commission_percentage','ps_commisson','ps_total_acq','ps_total_ren','ps_total_rev']

		if retailer_mis_user_id > 0:
			csv_header = ['Country','Date','Device','Brand','Model','Plan','Price','Master Commission%','Retailer Commission%','Master Commission','Retailer Commission','Plans Sold','Total Revenue','Total Commission']
		else:
			csv_header = ['Country','Date','Device','Brand','Model','Plan','Price','Commission%','Commission','Plans Sold','Total Revenue']

		dict_data = retailer_summary
		file_path = "media/sales_report/Sales_report_{}-{}.csv".format(start_date, end_date)
		try:

			with open(file_path, 'w', newline='') as csvfile:
				w = csv.writer(csvfile)
				writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
				w.writerow(csv_header)
				#writer.writeheader()
				for data in dict_data:

					custom_data = {}
					custom_data['ps_geo'] = data['ps_geo']
					custom_data['ps_date'] =  data['ps_date']
					custom_data['ps_category'] =  data['ps_category']
					custom_data['ps_make'] =  data['ps_make']
					custom_data['ps_model'] =  data['ps_model']
					custom_data['ps_plan'] =  data['ps_plan']
					custom_data['ps_price'] = data['ps_unit'] +' '+ str(data['ps_price'])

					if retailer_mis_user_id > 0:
						custom_data['ps_master_commission_percentage'] =  data['ps_master_commission_percentage']


					custom_data['ps_commission_percentage'] =  data['ps_commission_percentage']

					if retailer_mis_user_id > 0:
						custom_data['ps_master_commisson'] =  data['ps_unit'] +' '+ str(data['ps_master_commisson'])

					custom_data['ps_commisson'] =  data['ps_unit'] +' '+ str(data['ps_commisson'])
					custom_data['ps_total_acq'] =  data['ps_total_acq']
					custom_data['ps_total_ren'] =  data['ps_total_ren']

					custom_data['ps_total_rev'] = data['ps_unit'] +' '+ str(data['ps_total_rev'])

					if retailer_mis_user_id > 0:
						custom_data['ps_total_commisson'] =  data['ps_unit'] +' '+ str(data['ps_total_commisson'])
					writer.writerow(custom_data)

				csvfile.close()

				
			if os.path.exists(file_path):
				f = open(file_path, 'r')
				response = HttpResponse(f, content_type='text/csv')
				response['Content-Disposition'] = 'attachment; filename='+ os.path.basename(file_path)
				return response

			'''if os.path.exists(file_path):
				with open(file_path, 'r') as fh:
					print('---\n\n\n', fh.read(), '\n\n\n-------')
					data = fh.read()
					response = HttpResponse(data, content_type="application/force-download")
					response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
					return response'''


		except IOError:
			print("----\n\n\n", IOError, "\n\n\n\n------")

	



	template_name = 'sales/statistics.html'
	context = {'retailer_summary':retailer_summary,'categories_dropdown':categories_dropdown,'retailer_mis_user_id':retailer_mis_user_id}
	#print(context)
	# exit()
	return render(request,template_name,context)

# Create your views here.
@login_required(login_url='/login')
def monthly_summary(request):
	print(request.POST)
	start_date,category_id,plan,end_date = '','','',''

	categories_dropdown = PartnersSummaryDAO.get_monthly_summary(column = 'cat_id,cat_name',condition={'cat_status':'active'})
		
	if request.method == 'POST':
		category_id = request.POST.get("category",'')
		plan =  request.POST.get("plan",'')
		start_date = request.POST.get("startDate",'')
		end_date = request.POST.get("endDate",'')

	retailer_summary = PartnersSummaryDAO.get_retailer_summary(user_id = request.user.id, category_id = category_id, plan = plan,start_date = start_date, end_date = end_date)

	template_name = 'sales/statistics.html'
	context = {'retailer_summary':retailer_summary,'categories_dropdown':categories_dropdown}
	print(context)
	# exit()
	return render(request,template_name,context)