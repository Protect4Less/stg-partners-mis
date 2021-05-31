from django.db import models
from django.conf import settings
from django.db import connection
from decouple import config
from dateutil.relativedelta import relativedelta

import datetime
from datetime import datetime

class PartnersDAO(object):
	
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def get_partners(column='',condition=''):
		sql_condition = ""
		if len(condition) > 0:
			for k,v in condition.items():
				if "#" in k:
					column_name, column_condition = k.split("#")
					if(column_condition == "IN"):
						sql_condition += column_name+" "+column_condition+" ("+str(v)+") AND "
					else:	
						sql_condition += column_name+" "+column_condition+" "+str(v)+" AND "
				else:
					sql_condition += k+" "+(" IS NULL " if v is None else " = '"+str(v)+"'")+" AND "

			sql_condition = sql_condition[:-5]
			query = "SELECT * FROM "+config('P4L_DB_NAME')+".`partners` WHERE "+sql_condition
		else:
			query = "SELECT * FROM "+config('P4L_DB_NAME')+".`partners` ORDER BY 1 DESC LIMIT 1000"

		cursor = connection.cursor()
		print(query)
		cursor.execute(query)
		columns = [col[0] for col in cursor.description]
		#print(columns)
		return [
			dict(zip(columns, row))
			for row in cursor.fetchall()
		]


