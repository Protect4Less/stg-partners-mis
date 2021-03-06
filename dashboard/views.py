from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from backend.dao.DashboardSummaryDAO import DashboardSummaryDAO
from backend.classes.InitInfo import InitInfo

def logout_view(request):
	logout(request)
	return redirect("/")

@login_required(login_url='/login')
def dashboard(request):
	# return redirect('sales:statistics')
	start_date,end_date = '',''
	init_info =  InitInfo.init(request)
	partner_code = init_info['partner_code']

	#Quix Promoter USer redirect to Payment Link Generation Page
	print(request.user.id)
	if request.user.id == 36:
		return redirect('policy:initiate')

	if request.method == 'POST':
		start_date = request.POST.get("startDate",'')
		end_date = request.POST.get("endDate",'')

	dashboard_summary_data = DashboardSummaryDAO.get_dashboard_summary(user_id = request.user.id,start_date = start_date, end_date = end_date)

	retailer_mis_user_id = DashboardSummaryDAO.get_retailer_user_id(user_id = request.user.id)

	print(dashboard_summary_data)
	template_name = 'dashboard/dashboard.html'
	context = {'dashboard_summary_data':dashboard_summary_data,'retailer_mis_user_id':retailer_mis_user_id, 'partner_code':partner_code}
	return render(request,template_name,context)
