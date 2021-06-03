
def ew_price_config(prod_id):
	ew_price =  {
		1:{
			'monthly':{
				'plan_id': 10001,
				'plan_type': 'monthly', 
				'plan_title': 'Monthly', 
				'plan_type_code': 'PM', 
				'plan_discount': 20 ,
				'plan_price':10, 
				'plan_unit':'AED', 
				'plan_tax':0.00, 
				'plan_total_price':10,
				'plan_actual_price':12.50

			},
			'yearly':{
				'plan_id': 10001,
				'plan_type': 'yearly', 
				'plan_title': 'Yearly', 
				'plan_type_code': 'PY',
				'plan_discount': 33,
				'plan_price':100, 
				'plan_unit':'AED', 
				'plan_tax':0.00, 
				'plan_total_price':100, 
				'plan_actual_price':150
			}
		}
	}
	return ew_price[prod_id]