from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


from pymongo import MongoClient

client = MongoClient('mongodb://minjin:onnuri@54.180.149.99', 27017)
db = client.stores

import requests

# 1. requests 모듈로 데이터 다운받기
url = "https://api.odcloud.kr/api/15091227/v1/uddi:7bb1c1cc-e981-4c40-8aa4-98faca6ac4e5?page=32&perPage=5000&serviceKey=9IPRj2vLkz61h4nyu7t%2Fddu%2B0LZpU99syl48WGu21Y03O497XULBUGf3OypwwwiYUacDVgS%2FLBNA2Bf3lGvcmw%3D%3D"
response = requests.get(url)
parseResponse = response.json() #json 문자열을 파이썬 오브젝트(딕셔너리)로 변경

# 2. 데이터 정제하기

page = parseResponse['page']
perPage = parseResponse['perPage']
total_count = parseResponse['totalCount']


#def update_DB(url):
#    pages = total_count // perPage + 1
#    for page in range(pages+1):
#        cur_page_url = url.replace('page=1','page={}'.format(page)).replace('perPage=5000', 'perPage={}'.format(perPage))
#        url = cur_page_url
#        add_to_DB()

#def add_to_DB():
#
stores = parseResponse['data']
for store in stores:
    market_name = store['시장명']
    store_name = store['점포명']
    if store['주소'] is not None:
        raw_city = store['주소'].split(' ')[0]
        city = raw_city.rstrip('특별시''광역시''특별자치시''시')
        city = city.replace('북도', '북')
        city = city.replace('남도', '남')
        city = city.replace('충청', '충')
        city = city.replace('경상','경')
        city = city.replace('전라', '전')
    else: city = None
    detail_address = store['주소']
    store_type = store['취급품목']
    print(city, "|", market_name, "|", store_name, "|", store_type, "|", detail_address)
    store_list = {'지역': city, '시장명': market_name, '점포명': store_name, '취급품목': store_type, '주소': detail_address}
    db.stores.insert_one(store_list)

