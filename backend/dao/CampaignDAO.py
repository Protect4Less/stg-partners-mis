from django.db import models
from django.conf import settings
from django.db import connection

class CampaignDAO(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def get_campaign_stats(column='',condition=''):
		'''
		sql_update_column = ""
		sql_condition = ""
		row = None
		
		error = "condition data are missing" if condition == "" else None

		if error is None:

			for k,v in condition.items():
				sql_condition += k+" "+(" IS NULL " if v is None else " = '"+str(v)+"'")+" AND "

			sql_condition = sql_condition[:-5]

			cursor = connection.cursor()
			cursor.execute("SELECT * FROM `transaction_log` WHERE "+sql_condition)

			columns = [col[0] for col in cursor.description]
			row =  [
				dict(zip(columns, row))
				for row in cursor.fetchall()
			]
		'''
		row = [
			{"cmp_id": 1001, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "visits": 10110, "unique_visits": 454, "msisdn_count": 45, "unique_msisdn": 40, "telco": "ETISALAT", "call_to_action": 30, "success": 20, "pending": 5, "failed": 5, "call_to_action_percentage": 50, "policy_purchase_count": 10, "cost": 15, "cr": 25, "revenue": "800 AED", "pb_sent": 10, "cpa": 80 },
			{"cmp_id": 1002, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "visits": 1550, "unique_visits": 454, "msisdn_count": 45, "unique_msisdn": 40, "telco": "ETISALAT", "call_to_action": 30, "success": 20, "pending": 5, "failed": 5, "call_to_action_percentage": 50, "policy_purchase_count": 10, "cost": 15, "cr": 25, "revenue": "800 AED", "pb_sent": 10, "cpa": 80 }, 
			{"cmp_id": 1003, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "visits": 13410, "unique_visits": 454, "msisdn_count": 45, "unique_msisdn": 40, "telco": "ETISALAT", "call_to_action": 30, "success": 20, "pending": 5, "failed": 5, "call_to_action_percentage": 50, "policy_purchase_count": 10, "cost": 15, "cr": 25, "revenue": "800 AED", "pb_sent": 10, "cpa": 80 }, 
			{"cmp_id": 1004, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "visits": 10510, "unique_visits": 454, "msisdn_count": 45, "unique_msisdn": 40, "telco": "ETISALAT", "call_to_action": 30, "success": 20, "pending": 5, "failed": 5, "call_to_action_percentage": 50, "policy_purchase_count": 10, "cost": 15, "cr": 25, "revenue": "800 AED", "pb_sent": 10, "cpa": 80 },
			{"cmp_id": 1005, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "visits": 157410, "unique_visits": 454, "msisdn_count": 45, "unique_msisdn": 40, "telco": "ETISALAT", "call_to_action": 30, "success": 20, "pending": 5, "failed": 5, "call_to_action_percentage": 50, "policy_purchase_count": 10, "cost": 15, "cr": 25, "revenue": "800 AED", "pb_sent": 10, "cpa": 80 },
			{"cmp_id": 1006, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "visits": 10230, "unique_visits": 454, "msisdn_count": 45, "unique_msisdn": 40, "telco": "ETISALAT", "call_to_action": 30, "success": 20, "pending": 5, "failed": 5, "call_to_action_percentage": 50, "policy_purchase_count": 10, "cost": 15, "cr": 25, "revenue": "800 AED", "pb_sent": 10, "cpa": 80 },
			{"cmp_id": 1007, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "visits": 1070, "unique_visits": 454, "msisdn_count": 45, "unique_msisdn": 40, "telco": "ETISALAT", "call_to_action": 30, "success": 20, "pending": 5, "failed": 5, "call_to_action_percentage": 50, "policy_purchase_count": 10, "cost": 15, "cr": 25, "revenue": "800 AED", "pb_sent": 10, "cpa": 80 },
			{"cmp_id": 1008, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "visits": 101310, "unique_visits": 454, "msisdn_count": 45, "unique_msisdn": 40, "telco": "ETISALAT", "call_to_action": 30, "success": 20, "pending": 5, "failed": 5, "call_to_action_percentage": 50, "policy_purchase_count": 10, "cost": 15, "cr": 25, "revenue": "800 AED", "pb_sent": 10, "cpa": 80 },
			{"cmp_id": 1009, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "visits": 1610, "unique_visits": 454, "msisdn_count": 45, "unique_msisdn": 40, "telco": "ETISALAT", "call_to_action": 30, "success": 20, "pending": 5, "failed": 5, "call_to_action_percentage": 50, "policy_purchase_count": 10, "cost": 15, "cr": 25, "revenue": "800 AED", "pb_sent": 10, "cpa": 80 },
			{"cmp_id": 1010, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "visits": 175110, "unique_visits": 454, "msisdn_count": 45, "unique_msisdn": 40, "telco": "ETISALAT", "call_to_action": 30, "success": 20, "pending": 5, "failed": 5, "call_to_action_percentage": 50, "policy_purchase_count": 10, "cost": 15, "cr": 25, "revenue": "800 AED", "pb_sent": 10, "cpa": 80 },
			{"cmp_id": 1011, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "visits": 101310, "unique_visits": 454, "msisdn_count": 45, "unique_msisdn": 40, "telco": "ETISALAT", "call_to_action": 30, "success": 20, "pending": 5, "failed": 5, "call_to_action_percentage": 50, "policy_purchase_count": 10, "cost": 15, "cr": 25, "revenue": "800 AED", "pb_sent": 10, "cpa": 80 }
			]
		
		return row


	def get_campaign_list(column='',condition=''):
		'''
		sql_update_column = ""
		sql_condition = ""
		row = None
		
		error = "condition data are missing" if condition == "" else None

		if error is None:

			for k,v in condition.items():
				sql_condition += k+" "+(" IS NULL " if v is None else " = '"+str(v)+"'")+" AND "

			sql_condition = sql_condition[:-5]

			cursor = connection.cursor()
			cursor.execute("SELECT * FROM `transaction_log` WHERE "+sql_condition)

			columns = [col[0] for col in cursor.description]
			row =  [
				dict(zip(columns, row))
				for row in cursor.fetchall()
			]
		'''
		row = [
			{"cmp_id": 1001, "country": "UAE", "adnetwork": "TMT Default", "plan": "Daily", "category": "PHONE", "cpa": 80 },
			{"cmp_id": 1002, "country": "KW", "adnetwork": "TMT Default", "plan": "Weekly", "category": "Tablet", "cpa": 20 },
			{"cmp_id": 1003, "country": "QA", "adnetwork": "TMT Default", "plan": "Daily", "category": "Tablet", "cpa": 10 },
			{"cmp_id": 1004, "country": "BW", "adnetwork": "TMT Default", "plan": "Weekly", "category": "PHONE", "cpa": 70 }
		]
		
		return row

		