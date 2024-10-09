

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
            "geo": "USA",
            "category_data": {
                '22:iPhone': 'iPhone',
                '25:iPad': 'iPad',
                '24:Apple Watch': 'Apple Watch',
                '21:Mac': 'Mac',
                'Airpods:Airpods': 'Airpods',
            },
            "plan_types": {
                'iPhone': [
                    "12 months ADS",
                    "24 months ADS",
                    "24 months ADS + 12 months EW",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "12 months AD",
                    "24 months AD",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "24 months AD + 12 months EW (VIP)"
                ],
                'iPad': [
                    "12 months AD",
                    "24 months AD",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "24 months AD + 12 months EW (VIP)",
                ],
                'Apple Watch': [
                    "12 months AD",
                    "24 months AD",
                    "36 months AD",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "36 months AD + 24 Months EW",
                    "36 months AD + 36 months EW",
                    "36 months AD + 24 months EW(VIP)"
                ],
                'Mac': [
                    "12 months AD",
                    "24 months AD",
                    "36 months AD",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "36 months AD + 24 Months EW",
                    "36 months AD + 36 months EW",
                    "36 months AD + 24 months EW(VIP)"
                ],
                'Airpods': [
                    "2 Years AD + 12 Months EW"
                ],
            },
            "price": {
                "iPhone": {
                    "12 months ADS": {"900_and_below": 41, "901_and_above": 49},
                    "24 months ADS": {"900_and_below": 51, "901_and_above": 66},
                    "24 months ADS + 12 months EW": {"900_and_below": 81, "901_and_above": 111},
                    "12 months EW": {"900_and_below": 25, "901_and_above": 35},
                    "24 months EW": {"900_and_below": 39, "901_and_above": 55},
                    "36 months EW": {"900_and_below": 59, "901_and_above": 83},
                    "12 months AD": {"900_and_below": 57, "901_and_above": 78},
                    "24 months AD": {"900_and_below": 61, "901_and_above": 86},
                    "1st Year AD + 12 Months EW": {"900_and_below": 65, "901_and_above": 91},
                    "2 Years AD + 12 Months EW": {"900_and_below": 86, "901_and_above": 121 },
                    "2 Years AD + 24 Months EW": {"900_and_below": 100, "901_and_above": 141},
                    "24 months AD + 36 months EW": {"900_and_below": 120, "901_and_above": 169},
                    "24 months AD + 12 months EW (VIP)": {"900_and_below": 105, "901_and_above": 145}
                },
                "iPad": {
                    "12 months AD": {"500_and_below": 31, "501_and_700": 41, "701_and_900": 53, "901_and_above": 73},
                    "24 months AD": {"500_and_below": 34, "501_and_700": 48, "701_and_900": 61, "901_and_above": 85},
                    "12 months EW": {"500_and_below": 13, "501_and_700": 18, "701_and_900": 23, "901_and_above": 33},
                    "24 months EW": {"500_and_below": 21, "501_and_700": 30, "701_and_900": 38, "901_and_above": 55},
                    "36 months EW": {"500_and_below": 27, "501_and_700": 39, "701_and_900": 50, "901_and_above": 71},
                    "1st Year AD + 12 Months EW": {"500_and_below": 36, "501_and_700": 51, "701_and_900": 67, "901_and_above": 91},
                    "2 Years AD + 12 Months EW": {"500_and_below": 42, "501_and_700": 59, "701_and_900": 77, "901_and_above": 108},
                    "2 Years AD + 24 Months EW": {"500_and_below": 52, "501_and_700": 73, "701_and_900": 95, "901_and_above": 136},
                    "24 months AD + 36 months EW": {"500_and_below": 58, "501_and_700": 82, "701_and_900": 106, "901_and_above": 145},
                    "24 months AD + 12 months EW (VIP)": {"500_and_below": 55, "501_and_700": 63, "701_and_900": 98, "901_and_above": 117}
                },
                "Mac": {
                    "12 months AD": {"1000_and_below": 41, "1001_and_1200": 50, "1201_and_1400": 59, "1401_and_1800": 70, "1801_and_2300": 90, "2301_and_2900": 121, "2901_and_above": 165},
                    "24 months AD": {"1000_and_below": 50, "1001_and_1200": 61, "1201_and_1400": 72, "1401_and_1800": 85, "1801_and_2300": 110, "2301_and_2900": 148, "2901_and_above": 199},
                    "36 months AD": {"1000_and_below": 64, "1001_and_1200": 78, "1201_and_1400": 92, "1401_and_1800": 109, "1801_and_2300": 141, "2301_and_2900": 189, "2901_and_above": 255},
                    "12 months EW": {"1000_and_below": 23, "1001_and_1200": 28, "1201_and_1400": 33, "1401_and_1800": 39, "1801_and_2300": 50, "2301_and_2900": 68, "2901_and_above": 90},
                    "24 months EW": {"1000_and_below": 32, "1001_and_1200": 39, "1201_and_1400": 46, "1401_and_1800": 54, "1801_and_2300": 70, "2301_and_2900": 95, "2901_and_above": 125},
                    "36 months EW": {"1000_and_below": 50, "1001_and_1200": 55, "1201_and_1400": 72, "1401_and_1800": 80, "1801_and_2300": 100, "2301_and_2900": 130, "2901_and_above": 155},
                    "1st Year AD + 12 Months EW": {"1000_and_below": 66, "1001_and_1200": 74, "1201_and_1400": 90, "1401_and_1800": 98, "1801_and_2300": 136, "2301_and_2900": 210, "2901_and_above": 262},
                    "2 Years AD + 12 Months EW": {"1000_and_below": 74, "1001_and_1200": 87, "1201_and_1400": 104, "1401_and_1800": 120, "1801_and_2300": 153, "2301_and_2900": 238, "2901_and_above": 278},
                    "2 Years AD + 24 Months EW": {"1000_and_below": 90, "1001_and_1200": 98, "1201_and_1400": 115, "1401_and_1800": 131, "1801_and_2300": 164, "2301_and_2900": 242, "2901_and_above": 289},
                    "24 months AD + 36 months EW": {"1000_and_below": 114, "1001_and_1200": 109, "1201_and_1400": 125, "1401_and_1800": 142, "1801_and_2300": 174, "2301_and_2900": 253, "2901_and_above": 319},
                    "36 months AD + 24 Months EW": {"1000_and_below": 90, "1001_and_1200": 112, "1201_and_1400": 128, "1401_and_1800": 144, "1801_and_2300": 177, "2301_and_2900": 256, "2901_and_above": 321},
                    "36 months AD + 36 months EW": {"1000_and_below": 114, "1001_and_1200": 123, "1201_and_1400": 139, "1401_and_1800": 155, "1801_and_2300": 188, "2301_and_2900": 267, "2901_and_above": 351},
                    "36 months AD + 24 months EW (VIP)": {"1000_and_below": 99, "1001_and_1200": 124, "1201_and_1400": 144, "1401_and_1800": 161, "1801_and_2300": 199, "2301_and_2900": 291, "2901_and_above": 362},
                },
                "Apple Watch": {
                    "12 months AD": {"400_and_below": 15, "401_and_800": 16, "801_and_1200": 30, "1201_and_above": 44},
                    "24 months AD": {"400_and_below": 20, "401_and_800": 22, "801_and_1200": 38, "1201_and_above": 58},
                    "36 months AD": {"400_and_below": 26, "401_and_800": 32, "801_and_1200": 47, "1201_and_above": 65},
                    "12 months EW": {"400_and_below": 10, "401_and_800": 11, "801_and_1200": 22, "1201_and_above": 30},
                    "24 months EW": {"400_and_below": 15, "401_and_800": 17, "801_and_1200": 36, "1201_and_above": 48},
                    "36 months EW": {"400_and_below": 20, "401_and_800": 27, "801_and_1200": 50, "1201_and_above": 65},
                    "1st Year AD + 12 Months EW": {"400_and_below": 25, "401_and_800": 27, "801_and_1200": 52, "1201_and_above": 74},
                    "2 Years AD + 12 Months EW": {"400_and_below": 30, "401_and_800": 33, "801_and_1200": 60, "1201_and_above": 82},
                    "2 Years AD + 24 Months EW": {"400_and_below": 37, "401_and_800": 40, "801_and_1200": 67, "1201_and_above": 89},
                    "24 months AD + 36 months EW": {"400_and_below": 44, "401_and_800": 46, "801_and_1200": 74, "1201_and_above": 95},
                    "36 months AD + 24 Months EW": {"400_and_below": 41, "401_and_800": 49, "801_and_1200": 79, "1201_and_above": 95},
                    "36 months AD + 36 months EW": {"400_and_below": 49, "401_and_800": 57, "801_and_1200": 87, "1201_and_above": 106},
                    "36 months AD + 24 months EW (VIP)": {"400_and_below": 33, "401_and_800": 36, "801_and_1200": 68, "1201_and_above": 104},
                },
                "Airpods": {
                    "2 Years AD + 12 Months EW": {"500_and_below": 19, "501_and_above": 49}
                },
            }
        },
        "1080": {
            "prod_id": "5",
            "geo": "USA",
            "category_data": {
                '22:iPhone': 'iPhone',
                '25:iPad': 'iPad',
                '24:Apple Watch': 'Apple Watch',
                '21:Mac': 'Mac',
                'Airpods:Airpods': 'Airpods',
            },
            "plan_types": {
                'iPhone': [
                    "12 months ADS",
                    "24 months ADS",
                    "24 months ADS + 12 months EW",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "12 months AD",
                    "24 months AD",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "24 months AD + 12 months EW (VIP)"
                ],
                'iPad': [
                    "12 months AD",
                    "24 months AD",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "24 months AD + 12 months EW (VIP)",
                ],
                'Apple Watch': [
                    "12 months AD",
                    "24 months AD",
                    "36 months AD",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "36 months AD + 24 Months EW",
                    "36 months AD + 36 months EW",
                    "36 months AD + 24 months EW(VIP)"
                ],
                'Mac': [
                    "12 months AD",
                    "24 months AD",
                    "36 months AD",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "36 months AD + 24 Months EW",
                    "36 months AD + 36 months EW",
                    "36 months AD + 24 months EW(VIP)"
                ],
                'Airpods': [
                    "2 Years AD + 12 Months EW"
                ],
            },
            "price": {
                "iPhone": {
                    "12 months ADS": {"900_and_below": 41, "901_and_above": 49},
                    "24 months ADS": {"900_and_below": 51, "901_and_above": 66},
                    "24 months ADS + 12 months EW": {"900_and_below": 81, "901_and_above": 111},
                    "12 months EW": {"900_and_below": 25, "901_and_above": 35},
                    "24 months EW": {"900_and_below": 39, "901_and_above": 55},
                    "36 months EW": {"900_and_below": 59, "901_and_above": 83},
                    "12 months AD": {"900_and_below": 57, "901_and_above": 78},
                    "24 months AD": {"900_and_below": 61, "901_and_above": 86},
                    "1st Year AD + 12 Months EW": {"900_and_below": 65, "901_and_above": 91},
                    "2 Years AD + 12 Months EW": {"900_and_below": 86, "901_and_above": 121 },
                    "2 Years AD + 24 Months EW": {"900_and_below": 100, "901_and_above": 141},
                    "24 months AD + 36 months EW": {"900_and_below": 120, "901_and_above": 169},
                    "24 months AD + 12 months EW (VIP)": {"900_and_below": 105, "901_and_above": 145}
                },
                "iPad": {
                    "12 months AD": {"500_and_below": 31, "501_and_700": 41, "701_and_900": 53, "901_and_above": 73},
                    "24 months AD": {"500_and_below": 34, "501_and_700": 48, "701_and_900": 61, "901_and_above": 85},
                    "12 months EW": {"500_and_below": 13, "501_and_700": 18, "701_and_900": 23, "901_and_above": 33},
                    "24 months EW": {"500_and_below": 21, "501_and_700": 30, "701_and_900": 38, "901_and_above": 55},
                    "36 months EW": {"500_and_below": 27, "501_and_700": 39, "701_and_900": 50, "901_and_above": 71},
                    "1st Year AD + 12 Months EW": {"500_and_below": 36, "501_and_700": 51, "701_and_900": 67, "901_and_above": 91},
                    "2 Years AD + 12 Months EW": {"500_and_below": 42, "501_and_700": 59, "701_and_900": 77, "901_and_above": 108},
                    "2 Years AD + 24 Months EW": {"500_and_below": 52, "501_and_700": 73, "701_and_900": 95, "901_and_above": 136},
                    "24 months AD + 36 months EW": {"500_and_below": 58, "501_and_700": 82, "701_and_900": 106, "901_and_above": 145},
                    "24 months AD + 12 months EW (VIP)": {"500_and_below": 55, "501_and_700": 63, "701_and_900": 98, "901_and_above": 117}
                },
                "Mac": {
                    "12 months AD": {"1000_and_below": 41, "1001_and_1200": 50, "1201_and_1400": 59, "1401_and_1800": 70, "1801_and_2300": 90, "2301_and_2900": 121, "2901_and_above": 165},
                    "24 months AD": {"1000_and_below": 50, "1001_and_1200": 61, "1201_and_1400": 72, "1401_and_1800": 85, "1801_and_2300": 110, "2301_and_2900": 148, "2901_and_above": 199},
                    "36 months AD": {"1000_and_below": 64, "1001_and_1200": 78, "1201_and_1400": 92, "1401_and_1800": 109, "1801_and_2300": 141, "2301_and_2900": 189, "2901_and_above": 255},
                    "12 months EW": {"1000_and_below": 23, "1001_and_1200": 28, "1201_and_1400": 33, "1401_and_1800": 39, "1801_and_2300": 50, "2301_and_2900": 68, "2901_and_above": 90},
                    "24 months EW": {"1000_and_below": 32, "1001_and_1200": 39, "1201_and_1400": 46, "1401_and_1800": 54, "1801_and_2300": 70, "2301_and_2900": 95, "2901_and_above": 125},
                    "36 months EW": {"1000_and_below": 50, "1001_and_1200": 55, "1201_and_1400": 72, "1401_and_1800": 80, "1801_and_2300": 100, "2301_and_2900": 130, "2901_and_above": 155},
                    "1st Year AD + 12 Months EW": {"1000_and_below": 66, "1001_and_1200": 74, "1201_and_1400": 90, "1401_and_1800": 98, "1801_and_2300": 136, "2301_and_2900": 210, "2901_and_above": 262},
                    "2 Years AD + 12 Months EW": {"1000_and_below": 74, "1001_and_1200": 87, "1201_and_1400": 104, "1401_and_1800": 120, "1801_and_2300": 153, "2301_and_2900": 238, "2901_and_above": 278},
                    "2 Years AD + 24 Months EW": {"1000_and_below": 90, "1001_and_1200": 98, "1201_and_1400": 115, "1401_and_1800": 131, "1801_and_2300": 164, "2301_and_2900": 242, "2901_and_above": 289},
                    "24 months AD + 36 months EW": {"1000_and_below": 114, "1001_and_1200": 109, "1201_and_1400": 125, "1401_and_1800": 142, "1801_and_2300": 174, "2301_and_2900": 253, "2901_and_above": 319},
                    "36 months AD + 24 Months EW": {"1000_and_below": 90, "1001_and_1200": 112, "1201_and_1400": 128, "1401_and_1800": 144, "1801_and_2300": 177, "2301_and_2900": 256, "2901_and_above": 321},
                    "36 months AD + 36 months EW": {"1000_and_below": 114, "1001_and_1200": 123, "1201_and_1400": 139, "1401_and_1800": 155, "1801_and_2300": 188, "2301_and_2900": 267, "2901_and_above": 351},
                    "36 months AD + 24 months EW (VIP)": {"1000_and_below": 99, "1001_and_1200": 124, "1201_and_1400": 144, "1401_and_1800": 161, "1801_and_2300": 199, "2301_and_2900": 291, "2901_and_above": 362},
                },
                "Apple Watch": {
                    "12 months AD": {"400_and_below": 15, "401_and_800": 16, "801_and_1200": 30, "1201_and_above": 44},
                    "24 months AD": {"400_and_below": 20, "401_and_800": 22, "801_and_1200": 38, "1201_and_above": 58},
                    "36 months AD": {"400_and_below": 26, "401_and_800": 32, "801_and_1200": 47, "1201_and_above": 65},
                    "12 months EW": {"400_and_below": 10, "401_and_800": 11, "801_and_1200": 22, "1201_and_above": 30},
                    "24 months EW": {"400_and_below": 15, "401_and_800": 17, "801_and_1200": 36, "1201_and_above": 48},
                    "36 months EW": {"400_and_below": 20, "401_and_800": 27, "801_and_1200": 50, "1201_and_above": 65},
                    "1st Year AD + 12 Months EW": {"400_and_below": 25, "401_and_800": 27, "801_and_1200": 52, "1201_and_above": 74},
                    "2 Years AD + 12 Months EW": {"400_and_below": 30, "401_and_800": 33, "801_and_1200": 60, "1201_and_above": 82},
                    "2 Years AD + 24 Months EW": {"400_and_below": 37, "401_and_800": 40, "801_and_1200": 67, "1201_and_above": 89},
                    "24 months AD + 36 months EW": {"400_and_below": 44, "401_and_800": 46, "801_and_1200": 74, "1201_and_above": 95},
                    "36 months AD + 24 Months EW": {"400_and_below": 41, "401_and_800": 49, "801_and_1200": 79, "1201_and_above": 95},
                    "36 months AD + 36 months EW": {"400_and_below": 49, "401_and_800": 57, "801_and_1200": 87, "1201_and_above": 106},
                    "36 months AD + 24 months EW (VIP)": {"400_and_below": 33, "401_and_800": 36, "801_and_1200": 68, "1201_and_above": 104},
                },
                "Airpods": {
                    "2 Years AD + 12 Months EW": {"500_and_below": 19, "501_and_above": 49}
                },
            }
        },
        "1085": {
            "prod_id": "5",
            "geo": "USA",
            "category_data": {
                '22:iPhone': 'iPhone',
                '25:iPad': 'iPad',
                '24:Apple Watch': 'Apple Watch',
                '21:Mac': 'Mac',
                'Airpods:Airpods': 'Airpods',
            },
            "plan_types": {
                'iPhone': [
                    "12 months ADS",
                    "24 months ADS",
                    "24 months ADS + 12 months EW",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "12 months AD",
                    "24 months AD",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "24 months AD + 12 months EW (VIP)"
                ],
                'iPad': [
                    "12 months AD",
                    "24 months AD",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "24 months AD + 12 months EW (VIP)",
                ],
                'Apple Watch': [
                    "12 months AD",
                    "24 months AD",
                    "36 months AD",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "36 months AD + 24 Months EW",
                    "36 months AD + 36 months EW",
                    "36 months AD + 24 months EW(VIP)"
                ],
                'Mac': [
                    "12 months AD",
                    "24 months AD",
                    "36 months AD",
                    "12 months EW",
                    "24 months EW",
                    "36 months EW",
                    "1st Year AD + 12 Months EW",
                    "2 Years AD + 12 Months EW",
                    "2 Years AD + 24 Months EW",
                    "24 months AD + 36 months EW",
                    "36 months AD + 24 Months EW",
                    "36 months AD + 36 months EW",
                    "36 months AD + 24 months EW(VIP)"
                ],
                'Airpods': [
                    "2 Years AD + 12 Months EW"
                ],
            },
            "price": {
                "iPhone": {
                    "12 months ADS": {"900_and_below": 41, "901_and_above": 49},
                    "24 months ADS": {"900_and_below": 51, "901_and_above": 66},
                    "24 months ADS + 12 months EW": {"900_and_below": 81, "901_and_above": 111},
                    "12 months EW": {"900_and_below": 25, "901_and_above": 35},
                    "24 months EW": {"900_and_below": 39, "901_and_above": 55},
                    "36 months EW": {"900_and_below": 59, "901_and_above": 83},
                    "12 months AD": {"900_and_below": 57, "901_and_above": 78},
                    "24 months AD": {"900_and_below": 61, "901_and_above": 86},
                    "1st Year AD + 12 Months EW": {"900_and_below": 65, "901_and_above": 91},
                    "2 Years AD + 12 Months EW": {"900_and_below": 86, "901_and_above": 121 },
                    "2 Years AD + 24 Months EW": {"900_and_below": 100, "901_and_above": 141},
                    "24 months AD + 36 months EW": {"900_and_below": 120, "901_and_above": 169},
                    "24 months AD + 12 months EW (VIP)": {"900_and_below": 105, "901_and_above": 145}
                },
                "iPad": {
                    "12 months AD": {"500_and_below": 31, "501_and_700": 41, "701_and_900": 53, "901_and_above": 73},
                    "24 months AD": {"500_and_below": 34, "501_and_700": 48, "701_and_900": 61, "901_and_above": 85},
                    "12 months EW": {"500_and_below": 13, "501_and_700": 18, "701_and_900": 23, "901_and_above": 33},
                    "24 months EW": {"500_and_below": 21, "501_and_700": 30, "701_and_900": 38, "901_and_above": 55},
                    "36 months EW": {"500_and_below": 27, "501_and_700": 39, "701_and_900": 50, "901_and_above": 71},
                    "1st Year AD + 12 Months EW": {"500_and_below": 36, "501_and_700": 51, "701_and_900": 67, "901_and_above": 91},
                    "2 Years AD + 12 Months EW": {"500_and_below": 42, "501_and_700": 59, "701_and_900": 77, "901_and_above": 108},
                    "2 Years AD + 24 Months EW": {"500_and_below": 52, "501_and_700": 73, "701_and_900": 95, "901_and_above": 136},
                    "24 months AD + 36 months EW": {"500_and_below": 58, "501_and_700": 82, "701_and_900": 106, "901_and_above": 145},
                    "24 months AD + 12 months EW (VIP)": {"500_and_below": 55, "501_and_700": 63, "701_and_900": 98, "901_and_above": 117}
                },
                "Mac": {
                    "12 months AD": {"1000_and_below": 41, "1001_and_1200": 50, "1201_and_1400": 59, "1401_and_1800": 70, "1801_and_2300": 90, "2301_and_2900": 121, "2901_and_above": 165},
                    "24 months AD": {"1000_and_below": 50, "1001_and_1200": 61, "1201_and_1400": 72, "1401_and_1800": 85, "1801_and_2300": 110, "2301_and_2900": 148, "2901_and_above": 199},
                    "36 months AD": {"1000_and_below": 64, "1001_and_1200": 78, "1201_and_1400": 92, "1401_and_1800": 109, "1801_and_2300": 141, "2301_and_2900": 189, "2901_and_above": 255},
                    "12 months EW": {"1000_and_below": 23, "1001_and_1200": 28, "1201_and_1400": 33, "1401_and_1800": 39, "1801_and_2300": 50, "2301_and_2900": 68, "2901_and_above": 90},
                    "24 months EW": {"1000_and_below": 32, "1001_and_1200": 39, "1201_and_1400": 46, "1401_and_1800": 54, "1801_and_2300": 70, "2301_and_2900": 95, "2901_and_above": 125},
                    "36 months EW": {"1000_and_below": 50, "1001_and_1200": 55, "1201_and_1400": 72, "1401_and_1800": 80, "1801_and_2300": 100, "2301_and_2900": 130, "2901_and_above": 155},
                    "1st Year AD + 12 Months EW": {"1000_and_below": 66, "1001_and_1200": 74, "1201_and_1400": 90, "1401_and_1800": 98, "1801_and_2300": 136, "2301_and_2900": 210, "2901_and_above": 262},
                    "2 Years AD + 12 Months EW": {"1000_and_below": 74, "1001_and_1200": 87, "1201_and_1400": 104, "1401_and_1800": 120, "1801_and_2300": 153, "2301_and_2900": 238, "2901_and_above": 278},
                    "2 Years AD + 24 Months EW": {"1000_and_below": 90, "1001_and_1200": 98, "1201_and_1400": 115, "1401_and_1800": 131, "1801_and_2300": 164, "2301_and_2900": 242, "2901_and_above": 289},
                    "24 months AD + 36 months EW": {"1000_and_below": 114, "1001_and_1200": 109, "1201_and_1400": 125, "1401_and_1800": 142, "1801_and_2300": 174, "2301_and_2900": 253, "2901_and_above": 319},
                    "36 months AD + 24 Months EW": {"1000_and_below": 90, "1001_and_1200": 112, "1201_and_1400": 128, "1401_and_1800": 144, "1801_and_2300": 177, "2301_and_2900": 256, "2901_and_above": 321},
                    "36 months AD + 36 months EW": {"1000_and_below": 114, "1001_and_1200": 123, "1201_and_1400": 139, "1401_and_1800": 155, "1801_and_2300": 188, "2301_and_2900": 267, "2901_and_above": 351},
                    "36 months AD + 24 months EW (VIP)": {"1000_and_below": 99, "1001_and_1200": 124, "1201_and_1400": 144, "1401_and_1800": 161, "1801_and_2300": 199, "2301_and_2900": 291, "2901_and_above": 362},
                },
                "Apple Watch": {
                    "12 months AD": {"400_and_below": 15, "401_and_800": 16, "801_and_1200": 30, "1201_and_above": 44},
                    "24 months AD": {"400_and_below": 20, "401_and_800": 22, "801_and_1200": 38, "1201_and_above": 58},
                    "36 months AD": {"400_and_below": 26, "401_and_800": 32, "801_and_1200": 47, "1201_and_above": 65},
                    "12 months EW": {"400_and_below": 10, "401_and_800": 11, "801_and_1200": 22, "1201_and_above": 30},
                    "24 months EW": {"400_and_below": 15, "401_and_800": 17, "801_and_1200": 36, "1201_and_above": 48},
                    "36 months EW": {"400_and_below": 20, "401_and_800": 27, "801_and_1200": 50, "1201_and_above": 65},
                    "1st Year AD + 12 Months EW": {"400_and_below": 25, "401_and_800": 27, "801_and_1200": 52, "1201_and_above": 74},
                    "2 Years AD + 12 Months EW": {"400_and_below": 30, "401_and_800": 33, "801_and_1200": 60, "1201_and_above": 82},
                    "2 Years AD + 24 Months EW": {"400_and_below": 37, "401_and_800": 40, "801_and_1200": 67, "1201_and_above": 89},
                    "24 months AD + 36 months EW": {"400_and_below": 44, "401_and_800": 46, "801_and_1200": 74, "1201_and_above": 95},
                    "36 months AD + 24 Months EW": {"400_and_below": 41, "401_and_800": 49, "801_and_1200": 79, "1201_and_above": 95},
                    "36 months AD + 36 months EW": {"400_and_below": 49, "401_and_800": 57, "801_and_1200": 87, "1201_and_above": 106},
                    "36 months AD + 24 months EW (VIP)": {"400_and_below": 33, "401_and_800": 36, "801_and_1200": 68, "1201_and_above": 104},
                },
                "Airpods": {
                    "2 Years AD + 12 Months EW": {"500_and_below": 19, "501_and_above": 49}
                },
            }
        }
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
