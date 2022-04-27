from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbsparta

import requests

# 1. requests 모듈로 데이터 다운받기
url = "https://api.odcloud.kr/api/15091227/v1/uddi:7bb1c1cc-e981-4c40-8aa4-98faca6ac4e5?page=1&perPage=5000&serviceKey=9IPRj2vLkz61h4nyu7t%2Fddu%2B0LZpU99syl48WGu21Y03O497XULBUGf3OypwwwiYUacDVgS%2FLBNA2Bf3lGvcmw%3D%3D"
response = requests.get(url)
parseResponse = response.json() #json 문자열을 파이썬 오브젝트(딕셔너리)로 변경

# 2. 데이터 정제하기

def change_API_page(url, page, total_count):
    cnt = total_count / page + 1
    for i in range(cnt):
        open_page()
        add_to_DB()

def open_page():
    return "https://api.odcloud.kr/api/15091227/v1/uddi:7bb1c1cc-e981-4c40-8aa4-98faca6ac4e5?page=1&perPage=5000&serviceKey=9IPRj2vLkz61h4nyu7t%2Fddu%2B0LZpU99syl48WGu21Y03O497XULBUGf3OypwwwiYUacDVgS%2FLBNA2Bf3lGvcmw%3D%3D"

def add_to_DB():
    stores = parseResponse['data']
    store_list = []
    for store in stores:
        market_name = store['시장명']
        store_name = store['점포명']
        city, detail_address = store['주소'].split(' ')
        store_type = store['취급품목']
        print(market_name, store_name, city, detail_address, store_type)

add_to_DB()