

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
                'PPWGPI12M': '12 months PW GCC Plus India',
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
        "1079": {
            "prod_id": "5",
            "geo": "USA",
            "plan_type": {
                'PEW12M': '12 months EW',
                'PEW24M': '24 months EW',
                'PEW36M': '36 months EW',
            },
            "category_data": {
                22: 'Mobile Phone',
                25: 'Tablet',
                24: 'Smart Watch',
                21: 'Laptop',
                'Airpods': 'Airpods',
            },
            "price": {
                "Mobile Phones": {
                    "12 months EW": {"900_and_below": 25, "901_and_above": 35},
                    "24 months EW": {"900_and_below": 39, "901_and_above": 55},
                    "36 months EW": {"900_and_below": 59, "901_and_above": 83}
                },
                "Tablets": {
                    "12 months EW": {"500_and_below": 13, "501_and_700": 18, "7001_and_900": 23, "901_and_above": 33},
                    "24 months EW": {"500_and_below": 21, "501_and_700": 30, "7001_and_900": 38, "901_and_above": 55},
                    "36 months EW": {"500_and_below": 27, "501_and_700": 39, "7001_and_900": 50, "901_and_above": 71}
                },
                "Laptops": {
                    "12 months EW": {"1000_and_below": 23, "1000_and_1200": 28, "1201_and_1400": 33, "1401_and_1800": 39, "1801_and_2300": 50, "2301_and_2900": 68, "2901_and_above": 90},
                    "24 months EW": {"1000_and_below": 32, "1000_and_1200": 39, "1201_and_1400": 46, "1401_and_1800": 54, "1801_and_2300": 70, "2301_and_2900": 95, "2901_and_above": 125},
                    "36 months EW": {"1000_and_below": 50, "1000_and_1200": 55, "1201_and_1400": 72, "1401_and_1800": 80, "1801_and_2300": 100, "2301_and_2900": 130, "2901_and_above": 155},
                },
                "Smart Watch": {
                    "12 months EW": {"400_and_below": 10, "401_and_800": 11, "801_and_1200": 22, "1201_and_above": 30},
                    "24 months EW": {"400_and_below": 15, "401_and_800": 17, "801_and_1200": 36, "1201_and_above": 48},
                    "36 months EW": {"400_and_below": 20, "401_and_800": 27, "801_and_1200": 50, "1201_and_above": 65},
                },
                "Airpods": {
                    "12 months EW": {"500_and_below": 19, "501_and_above": 49},
                    "24 months EW": {"500_and_below": 19, "501_and_above": 49},
                    "36 months EW": {"500_and_below": 19, "501_and_above": 49},
                },
            }
        },
        "1081": {
            "prod_id": "5",
            "geo": "Oman",
            "plan_type": {
                'PEW12M': '12 months EW',
                'PEW24M': '24 months EW',
                'PEW36M': '36 months EW',
            },
            "category_data": {
                22: 'Iphone',
                25: 'Ipad',
                24: 'IWatch',
                21: 'Mac',
                'Airpods': 'Airpods',
            },
            "price": {
                "Iphone": {
                    "12 months EW": {"900_and_below": 25, "901_and_above": 35},
                    "24 months EW": {"900_and_below": 39, "901_and_above": 55},
                    "36 months EW": {"900_and_below": 59, "901_and_above": 83}
                },
                "Ipad": {
                    "12 months EW": {"500_and_below": 13, "501_and_700": 18, "7001_and_900": 23, "901_and_above": 33},
                    "24 months EW": {"500_and_below": 21, "501_and_700": 30, "7001_and_900": 38, "901_and_above": 55},
                    "36 months EW": {"500_and_below": 27, "501_and_700": 39, "7001_and_900": 50, "901_and_above": 71}
                },
                "Mac": {
                    "12 months EW": {"1000_and_below": 23, "1000_and_1200": 28, "1201_and_1400": 33, "1401_and_1800": 39, "1801_and_2300": 50, "2301_and_2900": 68, "2901_and_above": 90},
                    "24 months EW": {"1000_and_below": 32, "1000_and_1200": 39, "1201_and_1400": 46, "1401_and_1800": 54, "1801_and_2300": 70, "2301_and_2900": 95, "2901_and_above": 125},
                    "36 months EW": {"1000_and_below": 50, "1000_and_1200": 55, "1201_and_1400": 72, "1401_and_1800": 80, "1801_and_2300": 100, "2301_and_2900": 130, "2901_and_above": 155},
                },
                "IWatch": {
                    "12 months EW": {"400_and_below": 10, "401_and_800": 11, "801_and_1200": 22, "1201_and_above": 30},
                    "24 months EW": {"400_and_below": 15, "401_and_800": 17, "801_and_1200": 36, "1201_and_above": 48},
                    "36 months EW": {"400_and_below": 20, "401_and_800": 27, "801_and_1200": 50, "1201_and_above": 65},
                },
                "Airpods": {
                    "12 months EW": {"500_and_below": 19, "501_and_above": 49},
                    "24 months EW": {"500_and_below": 19, "501_and_above": 49},
                    "36 months EW": {"500_and_below": 19, "501_and_above": 49},
                },
            }
        },
        "1080": {
            "prod_id": "5",
            "geo": "Morocco",
            "plan_type": {
                'PEW12M': '12 months EW',
                'PEW24M': '24 months EW',
                'PEW36M': '36 months EW',
            },
            "category_data": {
                22: 'Iphone',
                25: 'Ipad',
                24: 'IWatch',
                21: 'Mac',
                'Airpods': 'Airpods',
            },
            "price": {
                "Iphone": {
                    "12 months EW": {"900_and_below": 25, "901_and_above": 35},
                    "24 months EW": {"900_and_below": 39, "901_and_above": 55},
                    "36 months EW": {"900_and_below": 59, "901_and_above": 83}
                },
                "Ipad": {
                    "12 months EW": {"500_and_below": 13, "501_and_700": 18, "7001_and_900": 23, "901_and_above": 33},
                    "24 months EW": {"500_and_below": 21, "501_and_700": 30, "7001_and_900": 38, "901_and_above": 55},
                    "36 months EW": {"500_and_below": 27, "501_and_700": 39, "7001_and_900": 50, "901_and_above": 71}
                },
                "Mac": {
                    "12 months EW": {"1000_and_below": 23, "1000_and_1200": 28, "1201_and_1400": 33, "1401_and_1800": 39, "1801_and_2300": 50, "2301_and_2900": 68, "2901_and_above": 90},
                    "24 months EW": {"1000_and_below": 32, "1000_and_1200": 39, "1201_and_1400": 46, "1401_and_1800": 54, "1801_and_2300": 70, "2301_and_2900": 95, "2901_and_above": 125},
                    "36 months EW": {"1000_and_below": 50, "1000_and_1200": 55, "1201_and_1400": 72, "1401_and_1800": 80, "1801_and_2300": 100, "2301_and_2900": 130, "2901_and_above": 155},
                },
                "IWatch": {
                    "12 months EW": {"400_and_below": 10, "401_and_800": 11, "801_and_1200": 22, "1201_and_above": 30},
                    "24 months EW": {"400_and_below": 15, "401_and_800": 17, "801_and_1200": 36, "1201_and_above": 48},
                    "36 months EW": {"400_and_below": 20, "401_and_800": 27, "801_and_1200": 50, "1201_and_above": 65},
                },
                "Airpods": {
                    "12 months EW": {"500_and_below": 19, "501_and_above": 49},
                    "24 months EW": {"500_and_below": 19, "501_and_above": 49},
                    "36 months EW": {"500_and_below": 19, "501_and_above": 49},
                },
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
