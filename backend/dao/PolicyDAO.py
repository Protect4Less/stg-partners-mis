from django.db import connection
from decouple import config

class PolicyDAO():

	# def insert_partners_generate_payement_link(data):
	# 	inserted_id = ""
	# 	columns_s_value = []
	# 	error = "data are missing" if data == "" else None

	# 	if error is None:
	# 		cursor = connection.cursor()
	# 		column_keys = ""
	# 		column_values = ""
	# 		for k,v in data.items():
	# 			if k:
	# 				column_keys += k+", "
	# 				column_values += "%s,"
	# 				columns_s_value.append(str(v))

	# 		query = "INSERT INTO "+config('P4L_DB_NAME')+".`partners_generate_payement_link` ("+column_keys+") VALUES ("+column_values+")"

	# 		print('partners_generate_payement_link => query', query)
	# 		# cursor.execute(query)
	# 		cursor.execute(query,columns_s_value)
	# 		inserted_id = cursor.lastrowid

	# 	return inserted_id

	def insert_partners_generate_payement_link(data):
		inserted_id = None
		error = "data are missing" if data == "" else None

		if error is None:
			cursor = connection.cursor()
			column_keys = ""
			column_values = ""
			for k,v in data.items():
				if k:
					column_keys += k+", "
					column_values += "'"+str(v)+"', "

			column_keys += "pgpl_addedon, pgpl_updatedon"
			column_values += "NOW(), NOW()"
			query = "INSERT INTO "+config('P4L_DB_NAME')+".`partners_generate_payement_link` ("+column_keys+") VALUES ("+column_values+")"
			print('partners_generate_payement_link => query', query)
			cursor.execute(query)
			
			inserted_id = cursor.lastrowid if cursor.lastrowid != "" and cursor.lastrowid > 0 else inserted_id

		return inserted_id