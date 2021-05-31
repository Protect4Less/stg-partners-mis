from django.db import models
from django.conf import settings
from django.db import connection, connections
from decouple import config

class DashboardSummaryDAO(object):
	
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def get_dashboard_summary(user_id = '', start_date='', end_date=''):
		sql_condition = ''
		category_table = config('P4L_DB_NAME')+'.category'

		retailer_user_id = DashboardSummaryDAO.get_retailer_user_id(user_id = user_id)

		if retailer_user_id is not 0:
			sql_condition += " ps_mis_user_id IN ("+str(user_id)+","+str(retailer_user_id)+") AND " if user_id !='' else "ps_mis_user_id = 0 AND "
		else:
			sql_condition += "ps_mis_user_id = "+str(user_id)+" AND " if user_id !='' else "ps_mis_user_id = 0 AND "

		sql_condition += "ps_date >= CURDATE() AND " if start_date == '' and end_date == '' else " (ps_date >= '"+start_date+"' AND ps_date < DATE_ADD('"+end_date+"', INTERVAL 1 DAY)) AND "

		sql_condition = sql_condition[:-5]

		print(sql_condition)

		if retailer_user_id is not 0: 
			query = "SELECT \n"\
					"ps_unit,"\
					"SUM(ps_total_acq) total_acquisition,  \n"\
					"SUM(ps_price) total_revenue,\n"\
					"SUM(ps_commisson) ps_commisson, \n"\
					"SUM(ps_master_commisson) ps_master_commisson, \n"\
					"SUM(ps_total_commisson) total_commission \n"\
					"FROM partners_summary \n"\
					"WHERE \n"\
					""+sql_condition+"\n"\
					"GROUP BY 1"
		else:
			query = "SELECT \n"\
					"ps_unit,"\
					"SUM(ps_total_acq) total_acquisition,  \n"\
					"SUM(ps_price) total_revenue,\n"\
					"SUM(ps_commisson) total_commission \n"\
					"FROM partners_summary \n"\
					"WHERE \n"\
					""+sql_condition+"\n"\
					"GROUP BY 1"


		print(query)
		cursor = connection.cursor()
		
		cursor.execute(query)
		columns = [col[0] for col in cursor.description]
		return [
			dict(zip(columns, row))
			for row in cursor.fetchall()
		]

	def get_retailer_user_id(user_id):
		partners_table = config('P4L_DB_NAME')+'.partners'
		cursor = connection.cursor()
		retailer_partner_id = 0
		partners_id_query = "SELECT partners_id from "+partners_table+" WHERE partners_mis_userid ="+str(user_id)

		cursor.execute(partners_id_query)
		partners_id_column = [col[0] for col in cursor.description]

		partners_id_column = [
			dict(zip(partners_id_column, row))
			for row in cursor.fetchall()
		]

		master_partner_id = partners_id_column[0] if len(partners_id_column) > 0 else 0 

		if master_partner_id is not 0:

			partners_mis_userid_query = "SELECT partners_mis_userid from "+partners_table+" WHERE partners_master_id ="+str(master_partner_id['partners_id'])

			print(partners_mis_userid_query)

			cursor.execute(partners_mis_userid_query)
			partners_mis_userid_columns = [col[0] for col in cursor.description]

			partners_mis_userid_columns = [
				dict(zip(partners_mis_userid_columns, row))
				for row in cursor.fetchall()
			]

			retailer_partner_id = partners_mis_userid_columns[0] if len(partners_mis_userid_columns) > 0 else 0

		if retailer_partner_id is not 0:
			retailer_partner_id = retailer_partner_id['partners_mis_userid']
		
		return retailer_partner_id
		


		