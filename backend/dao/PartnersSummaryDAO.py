from django.db import models
from django.conf import settings
from django.db import connection, connections
from decouple import config
from backend.dao.DashboardSummaryDAO import DashboardSummaryDAO


class PartnersSummaryDAO(object):
	
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def get_retailer_summary(user_id = '', category_id = '', plan = '', start_date='', end_date=''):
		sql_condition = ''

		retailer_user_id = DashboardSummaryDAO.get_retailer_user_id(user_id = user_id)

		category_table = config('P4L_DB_NAME')+'.category'

		if retailer_user_id > 0:
			sql_condition += "ps_mis_user_id IN ("+str(user_id)+","+str(retailer_user_id)+") AND " if user_id !='' else "ps_mis_user_id = 0 AND "
		else:
			sql_condition += "ps_mis_user_id = "+str(user_id)+" AND " if user_id !='' else "ps_mis_user_id = 0 AND "

		sql_condition += "ps_cat_id = "+str(category_id)+" AND " if category_id !='' else ""

		sql_condition += "ps_plan = '"+plan+"' AND " if plan !='' else ""



		sql_condition += "ps_date >= CURDATE() AND " if start_date == '' and end_date == '' else " (ps_date >= '"+start_date+"' AND ps_date < DATE_ADD('"+end_date+"', INTERVAL 1 DAY)) AND "

		sql_condition = sql_condition[:-5]

		if retailer_user_id > 0:
			query = "SELECT \n"\
				"DATE(ps_date) ps_date, \n"\
				"(SELECT cat_name from "+category_table+" WHERE cat_id = ps_cat_id) ps_category, \n"\
				"ps_make, \n"\
				"ps_model, \n"\
				"ps_geo, \n"\
				"ps_plan, \n"\
				"ps_unit, \n"\
				"ps_price, \n"\
				"ps_promocode, \n"\
				"ps_master_commission_percentage, \n"\
				"ps_commission_percentage, \n"\
				"SUM(ps_master_commisson) ps_master_commisson, \n"\
				"SUM(ps_commisson) ps_commisson, \n"\
				"SUM(ps_total_commisson) ps_total_commisson, \n"\
				"SUM(ps_total_acq) ps_total_acq, \n"\
				"SUM(ps_total_ren) ps_total_ren, \n"\
				"SUM(ps_total_revenue) ps_total_rev \n"\
				"FROM partners_summary \n"\
				"WHERE \n"\
				""+sql_condition+"\n"\
				"GROUP BY 1,2,3,4,5,6,7,8,9,10,11  \n"\
				"ORDER BY 1 DESC "
		else:
			query = "SELECT \n"\
				"DATE(ps_date) ps_date, \n"\
				"(SELECT cat_name from "+category_table+" WHERE cat_id = ps_cat_id) ps_category, \n"\
				"ps_make, \n"\
				"ps_model, \n"\
				"ps_geo, \n"\
				"ps_plan, \n"\
				"ps_unit, \n"\
				"ps_price, \n"\
				"ps_promocode, \n"\
				"ps_commission_percentage, \n"\
				"SUM(ps_total_acq) ps_total_acq, \n"\
				"SUM(ps_total_ren) ps_total_ren, \n"\
				"SUM(ps_total_revenue) ps_total_rev, \n"\
				"SUM(ps_commisson) ps_commisson\n"\
				"FROM partners_summary \n"\
				"WHERE \n"\
				""+sql_condition+"\n"\
				"GROUP BY 1,2,3,4,5,6,7,8,9,10  \n"\
				"ORDER BY 1 DESC "
		print(query)
		cursor = connection.cursor()
		
		cursor.execute(query)
		columns = [col[0] for col in cursor.description]
		return [
			dict(zip(columns, row))
			for row in cursor.fetchall()
		]

	def get_monthly_summary(user_id = '', category_id = '', plan = '', start_date='', end_date=''):
		sql_condition = ''
		category_table = config('P4L_DB_NAME')+'.category'

		sql_condition += "ps_mis_user_id = "+str(user_id)+" AND " if user_id !='' else "ps_mis_user_id = 0 AND "

		sql_condition += "ps_cat_id = "+str(category_id)+" AND " if category_id !='' else ""

		sql_condition += "ps_plan = '"+plan+"' AND " if plan !='' else ""



		sql_condition += "ps_date >= CURDATE() AND " if start_date == '' and end_date == '' else " (ps_date >= '"+start_date+"' AND ps_date < DATE_ADD('"+end_date+"', INTERVAL 1 DAY)) AND "

		sql_condition = sql_condition[:-5]
		query = "SELECT \n"\
			"DATE(ps_date) ps_date, \n"\
			"(SELECT cat_name from "+category_table+" WHERE cat_id = ps_cat_id) ps_category, \n"\
			"ps_make, \n"\
			"ps_model, \n"\
			"ps_geo, \n"\
			"ps_plan, \n"\
			"ps_unit, \n"\
			"ps_price, \n"\
			"ps_commission_percentage, \n"\
			"SUM(ps_total_acq) ps_total_acq, \n"\
			"SUM(ps_total_ren) ps_total_ren, \n"\
			"SUM(ps_total_revenue) ps_total_revenue, \n"\
			"SUM(ps_price) ps_total_rev, \n"\
			"SUM(ps_total_commisson) ps_total_commisson\n"\
			"FROM partners_summary \n"\
			"WHERE \n"\
			""+sql_condition+"\n"\
			"GROUP BY 1,2,3,4,5,6,7,8,9  \n"\
			"ORDER BY 1 DESC "
		print(query)
		cursor = connection.cursor()
		
		cursor.execute(query)
		columns = [col[0] for col in cursor.description]
		return [
			dict(zip(columns, row))
			for row in cursor.fetchall()
		]


	def get_category(column='',condition=''):
		# from django.db import connections
		with connections['p4l'].cursor() as cursor:

			sql_condition = ''
			
			for k,v in condition.items():
				if "#" in k:
					column_name, column_condition = k.split("#")
					sql_condition += column_name+" "+column_condition+" "+str(v)+" AND "
				else:
					sql_condition += k+" "+(" IS NULL " if v is None else " = '"+str(v)+"'")+" AND "
			
			sql_condition = sql_condition[:-5]
			# cursor = connections.cursor()
			query = "SELECT * FROM `category` WHERE "+sql_condition
			print(query)
			cursor.execute(query)
			columns = [col[0] for col in cursor.description]
			return [
				dict(zip(columns, row))
				for row in cursor.fetchall()
			]
		


		