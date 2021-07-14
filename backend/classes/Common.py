class Common():
    partner_dict = {
        "1032":{
            "prod_id":"1",
            "geo":"UAE",
            "plan_type" : {
                'PEW12M':'12 months EW',
                'PEW24M':'24 months EW',
                'PEW12MPP12M':'12 months EW UAE And India Primary Plus 12 Months'
            },
            "category_data":{
                'Laptops':'Laptop', 'Notebooks':'Notebook', 'Netbooks':'NetBook', 'Telecoms':'Telecom', 'Mobile Phones':'Mobile Phone', 'Smartphones':'Mobile Phone', 'Phablets':'Phablet'
            }
        }
    }

    #Local -> userid : partner_code
    # user_id_partner_code_dict = {
    #     7:'1034',
    #     8:'1032'
    # }

    # Staging
    user_id_partner_code_dict = {
        26:'1034',
        27:'1032',
        28:'1035',
        29:'1040'
    }

    #Production
    # user_id_partner_code_dict = {

    # }
