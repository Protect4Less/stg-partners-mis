

class Common:
    partner_dict = {
        "1032": {
            "prod_id": "1",
            "geo": "UAE",
            "plan_type": {
                'PEW12M': '12 months EW',
                'PEW24M': '24 months EW',
                'PEW12MPP12M': '12 months EW UAE And India Primary Plus 12 Months'
            },
            "category_data": {
                'Mobile Phones': 'Mobile Phone', 'Smartphones': 'Mobile Phone',
                'Notebooks': 'Notebook', 'Netbooks': 'NetBook', 'Telecoms': 'Telecom',
                'Laptops': 'Laptop', 'Phablets': 'Phablet'
            }
        },
        "1041": {
            "prod_id": "1",
            "geo": "UAE",
            "plan_type": {
                'PEW12M': '12 months EW',
                'PEW24M': '24 months EW',
                'PAD12MEW12M': '1st Year AD + 12 Months EW',
                'PAD24MEW12M': '2 Years AD + 12 Months EW',
                'PAD12M': '12 months AD',
            },
            "category_data": {
                'Laptops': 'Laptop',
                'Notebooks': 'Notebook',
                'Netbooks': 'Netbook',
                'Telecoms': 'Telecom',
                'Mobile Phones': 'Mobile Phone',
                'Smartphones': 'Mobile Phone',
                'Phablets': 'Phablet',
                'Consumer Electronics': 'Consumer Electronics',
                'Home Appliances - Non-Portable': 'Home Appliances',
                'Desktops': 'Desktop',
                'Printers': 'Printer',
                'Scanners': 'Scanner',
                'Tablets': 'Tablet',
                'White Goods': 'White Goods',
                'Smartwatches': 'Smart Watch',
            }
        },
        "1071": {
            "prod_id": "1",
            "geo": "UAE",
            "plan_type": {
                'PPW12M': '12 months PW',
                'PEW12M': '12 months EW',
                'PEW24M': '24 months EW',
                'PAD12M': '12 months AD',
                'PAD24M': '24 months AD',
                'PAD24MEW12M': '2 Years AD + 12 Months EW',
                'PPWGPI12M': '12 months PW GGC Plus India',
                'PEWGPI12M': '12 months EW GCC Plus India',
                'PEWGPI24M': '24 months EW GCC Plus India',
            },
            "category_data": {
                'Mobile Phones': 'Mobile Phone',
                'Tablets': 'Tablet',
                'Smart Watch': 'Smart Watch',
                'Laptops': 'Laptop',
            }
        },
    }

    # Local -> userid : partner_code
    user_id_partner_code_dict = {
        7: '1034',
        8: '1032',
        36: '1044'

    }

    # Staging
    # user_id_partner_code_dict = {
    #     26:'1042',
    #     27:'1032',
    #     28:'1035',
    #     29:'1034',
    #     35:'1042'
    # }

    master_user_partner_code_dict = {
        35: '1042'
    }

    # user_id_partner_code_dict = {        
    #     27:'1032',
    #     28:'1035',
    #     29:'1034',
    #     30:'1035',
    #     26:'1042'
    # }

    # Production
    # user_id_partner_code_dict = {

    # }

    payment_link_generation_partners = ['1042']

    # host_url = 'http://127.0.0.1:8000'
    host_url = 'https://devae.protect4less.com'
    # host_url = 'https://protect4less.ae'
