from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stores', methods=['GET'])
def listing():
    stores = list(db.stores.find({}, {'_id': False}))
    return jsonify({'all_stores':stores})

# https://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListKeyPopup.do?cpage=1&county_cd=02010&shop_table=SJTT.MKT_PAPER_SHOP&city_cd=02&txtKey=A.MARKET_NAME&txtParam=%EA%B4%91%EC%9E%A5%EC%8B%9C%EC%9E%A5
# https://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListKeyPopup.do?cpage=1&county_cd=02010&shop_table=SJTT.MKT_PAPER_SHOP&city_cd=02&txtKey=A.MARKET_NAME&txtParam=%EB%8F%99%EB%8C%80%EB%AC%B8%EB%AC%B8%EA%B5%AC%EC%99%84%EA%B5%AC%EA%B1%B0%EB%A6%AC_%EB%8F%99%EB%8C%80%EB%AC%B8%EB%AC%B8%EA%B5%AC%EC%99%84%EA%B5%AC%EB%8F%84%EB%A7%A4
# https://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListKeyPopup.do?cpage=1&county_cd=31010&shop_table=SJTT.MKT_PAPER_SHOP&city_cd=31&txtKey=A.MARKET_NAME&txtParam=%EA%B5%AC%EB%A7%A4%ED%83%84%EC%8B%9C%EC%9E%A5


## API 역할을 하는 부분
@app.route('/stores', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']




    doc = {
        'title':og_title,
        'image':og_image,
        'description':og_description,
        'url': url_receive,
        'comment':comment_receive
    }

    db.articles.insert_one(doc)
    return jsonify({'msg': '저장이 완료되었습니다!'})
















if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)