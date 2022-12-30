import json
from math import ceil
import requests
#ИСПОЛЬЗОВАТЬ ГЕНЕРАТОРЫ ДЛЯ УСКОРЕНИЯ
#Сравнивать айдишники или названия и добавлять новое
#Показать половину товаров/показать всё/указать количество страниц
#ДОБАВИТЬ КНОПКУ СТОП
#ПОставить логгер

def trees():
    print(f"Парсинг ёлок")
    cookies = {
        'disp_react_aa': '2',
        'ggr-widget-test': '1',
        'cookie_accepted': 'true',
        '_ym_uid': '1671996902301922019',
        '_ym_d': '1671996902',
        'iap.uid': '608ad786f51848c18160e73a8761c8ef',
        'aplaut_distinct_id': 'dmJgxheuULpc',
        'tmr_lvid': '652d8ccaf04f2babdb2f7898a6b789de',
        'tmr_lvidTS': '1671996902610',
        'uxs_uid': '3a904f50-848b-11ed-b2e5-dfb29d3438c3',
        'adrcid': 'AUbwCcz7rHU1o-u5LngDbCA',
        'sawOPH': 'true',
        '_gaexp': 'GAX1.2.GZ3bpEk7SZWRKA8-8Sbb2Q.19410.0!AmcF_S-hTZCjLH5fYtcljQ.19406.0',
        '_gid': 'GA1.2.834227449.1672220611',
        'lastConfirmedRegionID': '34',
        '_regionID': '34',
        '_ym_isad': '2',
        'qrator_jsr': '1672338402.853.qLkAttOwTackkdFK-4ggrc4lf52frqect3mlsri259mjakrbb-00',
        'qrator_jsid': '1672338402.853.qLkAttOwTackkdFK-hd0qfnau5c8p0713a648b9hrk50q1v6q',
        'GACookieStorage': 'GA1.2.422718309.1671996902',
        '_dc_gtm_UA-20946020-1': '1',
        '_ga': 'GA1.2.422718309.1671996902',
        '_ga_Z72HLV7H6T': 'GS1.1.1672338406.8.1.1672338499.0.0.0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'disp_react_aa=2; ggr-widget-test=1; cookie_accepted=true; _ym_uid=1671996902301922019; _ym_d=1671996902; iap.uid=608ad786f51848c18160e73a8761c8ef; aplaut_distinct_id=dmJgxheuULpc; tmr_lvid=652d8ccaf04f2babdb2f7898a6b789de; tmr_lvidTS=1671996902610; uxs_uid=3a904f50-848b-11ed-b2e5-dfb29d3438c3; adrcid=AUbwCcz7rHU1o-u5LngDbCA; sawOPH=true; _gaexp=GAX1.2.GZ3bpEk7SZWRKA8-8Sbb2Q.19410.0!AmcF_S-hTZCjLH5fYtcljQ.19406.0; _gid=GA1.2.834227449.1672220611; lastConfirmedRegionID=34; _regionID=34; _ym_isad=2; qrator_jsr=1672338402.853.qLkAttOwTackkdFK-4ggrc4lf52frqect3mlsri259mjakrbb-00; qrator_jsid=1672338402.853.qLkAttOwTackkdFK-hd0qfnau5c8p0713a648b9hrk50q1v6q; GACookieStorage=GA1.2.422718309.1671996902; _dc_gtm_UA-20946020-1=1; _ga=GA1.2.422718309.1671996902; _ga_Z72HLV7H6T=GS1.1.1672338406.8.1.1672338499.0.0.0',
        'Origin': 'https://leroymerlin.ru',
        'Referer': 'https://leroymerlin.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-api-key': 'Yeg8l3zQDwpVNBDTP3q6jM4lQVLW5TTv',
        'x-request-id': 'a645b646b25af029baf76b260784d018',
    }

    json_data = {
        'familyIds': [
            'iskusstvennye-eli-201709_Opus_Family',
        ],
        'limit': 30,
        'regionId': '34',
        'facets': [],
        'suggest': True,
        'offset': 0,
        'customerId': 'GA1.2.834227449.1672220611',
        'parentFamilyId': None,
        'searchMethod': 'DEFAULT',
    }

    response = requests.post('https://api.leroymerlin.ru/hybrid/v1/getProducts', cookies=cookies, headers=headers,
                             json=json_data).json()
    global pages
    pages = ceil(response["totalCount"] / 30)
    for page in range(1, pages + 1):
        json_data = {
            'familyIds': [
                'iskusstvennye-eli-201709_Opus_Family',
            ],
            'limit': 30,
            'regionId': '34',
            'facets': [],
            'suggest': True,
            'offset': page * json_data['limit'],
            'customerId': 'GA1.2.834227449.1672220611',
            'parentFamilyId': None,
            'searchMethod': 'DEFAULT',
        }
        response = requests.post('https://api.leroymerlin.ru/hybrid/v1/getProducts', cookies=cookies, headers=headers,
                                 json=json_data)

        try:
            r = response.json()
            with open("NewYear_Trees.json", "w", encoding="cp1251") as file:
                json.dump(r["content"], file, ensure_ascii=False, indent=4)

            for item in r["content"]:
                if item["price"]["main_price"] != item["price"]["previous_price"] and item["price"]["previous_price"] is not None:
                    delivery = "доступна" if item["eligibility"]["homeDeliveryEligible"] == True else "не доступна"
                    name = item["displayedName"]
                    price = item["price"]["main_price"]
                    link = f"https://leroymerlin.ru{item['productLink']}"
                    yield name, "Цена " + str(price) + "Руб", "Доставка " + delivery, link

        except Exception:
            cookies = {
                'disp_react_aa': '2',
                'ggr-widget-test': '1',
                'cookie_accepted': 'true',
                '_ym_uid': '1671996902301922019',
                '_ym_d': '1671996902',
                'iap.uid': '608ad786f51848c18160e73a8761c8ef',
                'aplaut_distinct_id': 'dmJgxheuULpc',
                'tmr_lvid': '652d8ccaf04f2babdb2f7898a6b789de',
                'tmr_lvidTS': '1671996902610',
                'uxs_uid': '3a904f50-848b-11ed-b2e5-dfb29d3438c3',
                'adrcid': 'AUbwCcz7rHU1o-u5LngDbCA',
                'sawOPH': 'true',
                '_gaexp': 'GAX1.2.GZ3bpEk7SZWRKA8-8Sbb2Q.19410.0!AmcF_S-hTZCjLH5fYtcljQ.19406.0',
                '_gid': 'GA1.2.834227449.1672220611',
                '_ym_isad': '2',
                'lastConfirmedRegionID': '34',
                'GACookieStorage': 'GA1.2.422718309.1671996902',
                'qrator_jsid': '1672233522.550.3L058ZgmRXhyMRde-vdra74oj4h8g7jad64o2j87g3aneml17',
                '_regionID': '34',
                'X-API-Experiments-sub': 'B',
                '_dc_gtm_UA-20946020-1': '1',
                '_ga': 'GA1.2.422718309.1671996902',
                '_ga_Z72HLV7H6T': 'GS1.1.1672233523.6.1.1672233831.0.0.0',
            }
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'ru,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json;charset=UTF-8',
                # 'Cookie': 'disp_react_aa=2; ggr-widget-test=1; cookie_accepted=true; _ym_uid=1671996902301922019; _ym_d=1671996902; iap.uid=608ad786f51848c18160e73a8761c8ef; aplaut_distinct_id=dmJgxheuULpc; tmr_lvid=652d8ccaf04f2babdb2f7898a6b789de; tmr_lvidTS=1671996902610; uxs_uid=3a904f50-848b-11ed-b2e5-dfb29d3438c3; adrcid=AUbwCcz7rHU1o-u5LngDbCA; sawOPH=true; _gaexp=GAX1.2.GZ3bpEk7SZWRKA8-8Sbb2Q.19410.0!AmcF_S-hTZCjLH5fYtcljQ.19406.0; _gid=GA1.2.834227449.1672220611; _ym_isad=2; lastConfirmedRegionID=34; GACookieStorage=GA1.2.422718309.1671996902; qrator_jsid=1672233522.550.3L058ZgmRXhyMRde-vdra74oj4h8g7jad64o2j87g3aneml17; _regionID=34; X-API-Experiments-sub=B; _dc_gtm_UA-20946020-1=1; _ga=GA1.2.422718309.1671996902; _ga_Z72HLV7H6T=GS1.1.1672233523.6.1.1672233831.0.0.0',
                'Origin': 'https://leroymerlin.ru',
                'Referer': 'https://leroymerlin.ru/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
                'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'x-api-key': 'Yeg8l3zQDwpVNBDTP3q6jM4lQVLW5TTv',
                'x-request-id': '703080b5d7a2a84a3e13c7dcfe3f0a93',
            }
            response = requests.post('https://api.leroymerlin.ru/hybrid/v1/getProducts', cookies=cookies, headers=headers,
                                     json=json_data)
            r = response.json()
            for item in r["content"]:
                if item["price"]["main_price"] != item["price"]["previous_price"] and item["price"]["previous_price"] is not None:
                    delivery = "доступна" if item["eligibility"]["homeDeliveryEligible"] == True else "не доступна"
                    name = item["displayedName"]
                    price = item["price"]["main_price"]
                    link = f"https://leroymerlin.ru{item['productLink']}"
                    yield name, "Цена " + str(price) + "Руб", "Доставка " + delivery, link



def girlyandy():

    cookies = {
        'disp_react_aa': '2',
        'ggr-widget-test': '1',
        'cookie_accepted': 'true',
        '_ym_uid': '1671996902301922019',
        '_ym_d': '1671996902',
        'iap.uid': '608ad786f51848c18160e73a8761c8ef',
        'aplaut_distinct_id': 'dmJgxheuULpc',
        'tmr_lvid': '652d8ccaf04f2babdb2f7898a6b789de',
        'tmr_lvidTS': '1671996902610',
        'uxs_uid': '3a904f50-848b-11ed-b2e5-dfb29d3438c3',
        'adrcid': 'AUbwCcz7rHU1o-u5LngDbCA',
        'sawOPH': 'true',
        '_gaexp': 'GAX1.2.GZ3bpEk7SZWRKA8-8Sbb2Q.19410.0!AmcF_S-hTZCjLH5fYtcljQ.19406.0',
        '_gid': 'GA1.2.834227449.1672220611',
        '_ym_isad': '2',
        'lastConfirmedRegionID': '34',
        'GACookieStorage': 'GA1.2.422718309.1671996902',
        '_regionID': '34',
        'X-API-Experiments-sub': 'B',
        'qrator_jsid': '1672233522.550.3L058ZgmRXhyMRde-k9dm40o75spu292jbt3garhj4181rd06',
        '_dc_gtm_UA-20946020-1': '1',
        '_ga': 'GA1.2.422718309.1671996902',
        '_ga_Z72HLV7H6T': 'GS1.1.1672233523.6.1.1672234449.0.0.0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'disp_react_aa=2; ggr-widget-test=1; cookie_accepted=true; _ym_uid=1671996902301922019; _ym_d=1671996902; iap.uid=608ad786f51848c18160e73a8761c8ef; aplaut_distinct_id=dmJgxheuULpc; tmr_lvid=652d8ccaf04f2babdb2f7898a6b789de; tmr_lvidTS=1671996902610; uxs_uid=3a904f50-848b-11ed-b2e5-dfb29d3438c3; adrcid=AUbwCcz7rHU1o-u5LngDbCA; sawOPH=true; _gaexp=GAX1.2.GZ3bpEk7SZWRKA8-8Sbb2Q.19410.0!AmcF_S-hTZCjLH5fYtcljQ.19406.0; _gid=GA1.2.834227449.1672220611; _ym_isad=2; lastConfirmedRegionID=34; GACookieStorage=GA1.2.422718309.1671996902; _regionID=34; X-API-Experiments-sub=B; qrator_jsid=1672233522.550.3L058ZgmRXhyMRde-k9dm40o75spu292jbt3garhj4181rd06; _dc_gtm_UA-20946020-1=1; _ga=GA1.2.422718309.1671996902; _ga_Z72HLV7H6T=GS1.1.1672233523.6.1.1672234449.0.0.0',
        'Origin': 'https://leroymerlin.ru',
        'Referer': 'https://leroymerlin.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-api-key': 'Yeg8l3zQDwpVNBDTP3q6jM4lQVLW5TTv',
        'x-request-id': 'd49bf9c50cf7d9cf9de589999598e01f',
    }

    json_data = {
        'familyIds': [
            'elektricheskie-girlyandy-201709',
        ],
        'limit': 30,
        'regionId': '34',
        'facets': [],
        'suggest': True,
        'offset': 30,
        'customerId': 'GA1.2.834227449.1672220611',
        'parentFamilyId': None,
        'searchMethod': 'DEFAULT',
    }

    response = requests.post('https://api.leroymerlin.ru/hybrid/v1/getProducts', cookies=cookies, headers=headers,
                             json=json_data).json()

    pages = ceil(response["totalCount"] / 30)
    print("Парсинг гирлянд")

    for page in range(1, pages + 1):
        json_data = {
            'familyIds': [
                'elektricheskie-girlyandy-201709',
            ],
            'limit': 30,
            'regionId': '34',
            'facets': [],
            'suggest': True,
            'offset': 30,
            'customerId': 'GA1.2.834227449.1672220611',
            'parentFamilyId': None,
            'searchMethod': 'DEFAULT',
        }
        response = requests.post('https://api.leroymerlin.ru/hybrid/v1/getProducts', cookies=cookies, headers=headers,
                                 json=json_data)

        try:
            r = response.json()

            for item in r["content"]:
                if item["price"]["main_price"] != item["price"]["previous_price"] and item["price"]["previous_price"] is not None:
                    delivery = "доступна" if item["eligibility"]["homeDeliveryEligible"] == True else "не доступна"
                    name = item["displayedName"]
                    price = item["price"]["main_price"]
                    link = f"https://leroymerlin.ru{item['productLink']}"
                    yield name, "Цена " + price + "Руб", "Доставка " + delivery, link

        except Exception:
            cookies = {
                'disp_react_aa': '2',
                'ggr-widget-test': '1',
                'cookie_accepted': 'true',
                '_ym_uid': '1671996902301922019',
                '_ym_d': '1671996902',
                'iap.uid': '608ad786f51848c18160e73a8761c8ef',
                'aplaut_distinct_id': 'dmJgxheuULpc',
                'tmr_lvid': '652d8ccaf04f2babdb2f7898a6b789de',
                'tmr_lvidTS': '1671996902610',
                'uxs_uid': '3a904f50-848b-11ed-b2e5-dfb29d3438c3',
                'adrcid': 'AUbwCcz7rHU1o-u5LngDbCA',
                'sawOPH': 'true',
                '_gaexp': 'GAX1.2.GZ3bpEk7SZWRKA8-8Sbb2Q.19410.0!AmcF_S-hTZCjLH5fYtcljQ.19406.0',
                '_gid': 'GA1.2.834227449.1672220611',
                '_ym_isad': '2',
                'lastConfirmedRegionID': '34',
                'GACookieStorage': 'GA1.2.422718309.1671996902',
                'qrator_jsid': '1672233522.550.3L058ZgmRXhyMRde-vdra74oj4h8g7jad64o2j87g3aneml17',
                '_regionID': '34',
                'X-API-Experiments-sub': 'B',
                '_dc_gtm_UA-20946020-1': '1',
                '_ga': 'GA1.2.422718309.1671996902',
                '_ga_Z72HLV7H6T': 'GS1.1.1672233523.6.1.1672233831.0.0.0',
            }
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'ru,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json;charset=UTF-8',
                # 'Cookie': 'disp_react_aa=2; ggr-widget-test=1; cookie_accepted=true; _ym_uid=1671996902301922019; _ym_d=1671996902; iap.uid=608ad786f51848c18160e73a8761c8ef; aplaut_distinct_id=dmJgxheuULpc; tmr_lvid=652d8ccaf04f2babdb2f7898a6b789de; tmr_lvidTS=1671996902610; uxs_uid=3a904f50-848b-11ed-b2e5-dfb29d3438c3; adrcid=AUbwCcz7rHU1o-u5LngDbCA; sawOPH=true; _gaexp=GAX1.2.GZ3bpEk7SZWRKA8-8Sbb2Q.19410.0!AmcF_S-hTZCjLH5fYtcljQ.19406.0; _gid=GA1.2.834227449.1672220611; _ym_isad=2; lastConfirmedRegionID=34; GACookieStorage=GA1.2.422718309.1671996902; qrator_jsid=1672233522.550.3L058ZgmRXhyMRde-vdra74oj4h8g7jad64o2j87g3aneml17; _regionID=34; X-API-Experiments-sub=B; _dc_gtm_UA-20946020-1=1; _ga=GA1.2.422718309.1671996902; _ga_Z72HLV7H6T=GS1.1.1672233523.6.1.1672233831.0.0.0',
                'Origin': 'https://leroymerlin.ru',
                'Referer': 'https://leroymerlin.ru/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
                'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'x-api-key': 'Yeg8l3zQDwpVNBDTP3q6jM4lQVLW5TTv',
                'x-request-id': '703080b5d7a2a84a3e13c7dcfe3f0a93',
            }
            response = requests.post('https://api.leroymerlin.ru/hybrid/v1/getProducts', cookies=cookies,
                                     headers=headers,
                                     json=json_data)
            r = response.json()
            for item in r["content"]:
                if item["price"]["main_price"] != item["price"]["previous_price"] and item["price"]["previous_price"] is not None:
                    delivery = "доступна" if item["eligibility"]["homeDeliveryEligible"] == True else "не доступна"
                    name = item["displayedName"]
                    price = item["price"]["main_price"]
                    link = f"https://leroymerlin.ru{item['productLink']}"
                    yield name, "Цена " + str(price) + "Руб", "Доставка " + delivery, link



