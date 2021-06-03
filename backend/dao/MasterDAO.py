from django.db import models
from django.conf import settings
from django.db import connection
from decouple import config
from dateutil.relativedelta import relativedelta

import datetime
from datetime import datetime



# logger = logging.getLogger(__name__)

class MasterDAO():
	def get_category(cat_id = None, cat_geo = None, cat_prod_id = None, cat_code = None, cat_name = None, cat_status_check = True):
			cursor = connection.cursor()
			cat_qry = "SELECT cat_id,cat_p_id,cat_geo,cat_code,cat_name FROM "+config('P4L_DB_NAME')+".`category` WHERE "

			cat_qry += 	" `cat_status` IN ('active')" if cat_status_check is True else " `cat_status` IN ('active','inactive')"

			if cat_id is not None:
				cat_qry += " AND cat_id IN ("+str(cat_id)+")"

			if cat_geo is not None:
				cat_qry += " AND cat_geo = '"+str(cat_geo)+"'"

			if cat_prod_id is not None:
				cat_qry += " AND cat_p_id = '"+str(cat_prod_id)+"'"

			if cat_code is not None:
				cat_qry += " AND cat_code = '"+str(cat_code)+"'"

			if cat_name is not None:
				cat_qry += " AND cat_name = '"+str(cat_name)+"'"

			cat_qry += ' ORDER BY cat_sequence'
			print(cat_qry)
			# logger.debug(cat_qry)
			cursor.execute(cat_qry)
			columns = [col[0] for col in cursor.description]
			return [
				dict(zip(columns, row))
				for row in cursor.fetchall()
			]

	def get_make(make_code = None, make_id = None, country_code = None, category_id = None, make_name_like = None, category_ids = None, make_ids = None, make_status_check = True):
			cursor = connection.cursor()

			make_query = "SELECT make_id,make_cat_id,make_code,make_name FROM "+config('P4L_DB_NAME')+".`make` WHERE "

			
			make_query += " `make_status`= 'active'" if make_status_check is True else " `make_status` IN ('active','inactive') "

			if make_code is not None and make_code != "":
				make_query += " AND `make_code`= '"+make_code+"'"

			if make_id is not None and make_id != "":
				make_query += " AND `make_id`= "+make_id

			if category_id is not None and category_id != "":
				make_query += " AND `make_cat_id`= "+str(category_id)

			if make_name_like is not None and make_name_like != "":
				make_query += " AND `make_name` LIKE '"+str(make_name_like)+"%'"

			if category_ids is not None and category_ids != "":
				make_query += " AND `make_cat_id` IN ("+str(category_ids)+")"

			if make_ids is not None and make_ids != "":
				make_query += " AND `make_id` IN ("+str(make_ids)+")"

			make_query += ' ORDER BY  CASE WHEN make_sequence in (1,2,3,4,5,6,7,8,9,10,11) THEN make_sequence ELSE 2000 END, make_name ASC'

			print(make_query)
			cursor.execute(make_query)
			columns = [col[0] for col in cursor.description]
			return [
				dict(zip(columns, row))
				for row in cursor.fetchall()
			]


	def get_item(item_make_id = None, item_code = None, item_id = None, category_id = None, item_name_like = None, item_cat_code = None, item_make_code = None, category_ids = None, price_slab = None, column = None, item_make_ids = None, item_status = True, item_name = None):
		cursor = connection.cursor()
		column = column if column is not None and column != "" else 'item_id, item_code, item_name, item_price_slab, item_cat_code, item_cat_id, item_make_code, item_make_id'

		if item_status is True:
			item_qry = "SELECT "+column+" FROM "+config('P4L_DB_NAME')+".`item` WHERE `item_status` IN ('active')"
		else:
			item_qry = "SELECT "+column+" FROM "+config('P4L_DB_NAME')+".`item` WHERE `item_status` IN ('active','inactive')"

		if category_id is not None and category_id != "":
			item_qry += " AND item_cat_id = "+str(category_id)

		if item_make_id is not None and item_make_id != "":
			item_qry += " AND item_make_id = "+str(item_make_id)+""

		if item_code is not None and item_code != "":
			item_qry += " AND item_code = '"+str(item_code)+"'"

		if item_id is not None and item_id != "":
			item_qry += " AND item_id = "+str(item_id)

		if item_name_like is not None and item_name_like != "":
			item_qry += " AND item_name LIKE '%"+str(item_name_like)+"%'"

		if item_cat_code is not None and item_cat_code != "":
			item_qry += " AND item_cat_code = '"+str(item_cat_code)+"'"

		if item_make_code is not None and item_make_code != "":
			item_qry += " AND item_make_code = '"+str(item_make_code)+"'"

		if category_ids is not None and category_ids != "":
			item_qry += " AND item_cat_id IN ("+category_ids+")"

		if price_slab is not None and price_slab != "":
			item_qry += " AND item_price_slab IN ("+price_slab+")"

		if item_make_ids is not None and item_make_ids != "":
			item_qry += " AND item_make_id IN ("+item_make_ids+")"

		if item_name is not None and item_name != "":
			item_qry += " AND item_name = '"+str(item_name)+"'"

		item_qry += ' ORDER BY item_name'

		print(item_qry)
		cursor.execute(item_qry)
		columns = [col[0] for col in cursor.description]
		return [
			dict(zip(columns, row))
			for row in cursor.fetchall()
		]


	def get_item_all(column='',condition=''):
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
			query = "SELECT * FROM "+config('P4L_DB_NAME')+".`item` WHERE "+sql_condition
		else:
			query = "SELECT * FROM "+config('P4L_DB_NAME')+".`item`"

		cursor = connection.cursor()
		print(query)
		cursor.execute(query)
		columns = [col[0] for col in cursor.description]
		#print(columns)
		return [
			dict(zip(columns, row))
			for row in cursor.fetchall()
		]

	def get_plan(prod_id = None, cat_id = None, plan_type = None, order_by = None, plan_id = None, plan_slab_code = None, package = None, price_type = None, ctm_id = None, ctm_ids = None, price_types = None, plan_type_code = None):
		cursor = connection.cursor()

		plan_query = "SELECT plan_id, plan_prod_id, plan_cat_id, plan_package, plan_actual_price ,plan_price_type, plan_slab_code, plan_ctm_id, plan_type, plan_title, plan_type_code, plan_playstore_id, plan_duration, plan_price, plan_tax, plan_total_price, plan_unit, plan_discount, plan_usd_price FROM "+config('P4L_DB_NAME')+".`plan` WHERE plan_status = 'active'"

		if prod_id != "" and prod_id is not None:
			plan_query += " AND plan_prod_id = "+str(prod_id)

		if cat_id != "" and cat_id is not None:
			plan_query += " AND plan_cat_id = "+str(cat_id)

		if package != "" and package is not None:
			plan_query += " AND plan_package = '"+package+"'"

		if price_type != "" and price_type is not None:
			plan_query += " AND plan_price_type = '"+price_type+"'"

		if price_types != "" and price_types is not None:
			plan_query += " AND plan_price_type IN ("+price_types+")"

		if plan_type_code != "" and plan_type_code is not None:
			plan_query += " AND plan_type_code = '"+plan_type_code+"'"

		if plan_type != "" and plan_type is not None:
			plan_query += " AND plan_type IN ('"+str(plan_type)+"')"

		if plan_slab_code != "" and plan_slab_code is not None:
			plan_query += " AND plan_slab_code = '"+str(plan_slab_code)+"'"

		if plan_id != "" and plan_id is not None:
			plan_query += " AND plan_id = "+str(plan_id)

		if ctm_id != "" and ctm_id is not None:
			plan_query += " AND FIND_IN_SET("+ctm_id+", plan_ctm_id)"

		if ctm_ids != "" and ctm_ids is not None:
			plan_query += " AND plan_ctm_id = '"+ctm_ids+"'"

		if order_by is not None:
			plan_query += ' '+order_by

		print(plan_query)
		cursor.execute(plan_query)
		columns = [col[0] for col in cursor.description]
		return [
			dict(zip(columns, row))
			for row in cursor.fetchall()
		]