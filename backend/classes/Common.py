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
    user_id_partner_code_dict = {
        7:'1034',
        8:'1032',
        36:'1044'

    }

    #Staging
    # user_id_partner_code_dict = {
    #     26:'1042',
    #     27:'1032',
    #     28:'1035',
    #     29:'1034',
    #     35:'1042'
    # }

    master_user_partner_code_dict = {
        35:'1042'
    }

    # user_id_partner_code_dict = {        
    #     27:'1032',
    #     28:'1035',
    #     29:'1034',
    #     30:'1035',
    #     26:'1042'
    # }

    #Production
    # user_id_partner_code_dict = {

    # }
