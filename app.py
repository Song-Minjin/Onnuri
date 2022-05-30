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

@app.route('/allstores', methods=['GET'])
def show_all_stores_page():
    return render_template('/subpage/all_stores.html')
def show_all_stores():
    stores = list(db.stores.find({}, {'_id': False}))
    return jsonify({'all_stores': stores})

@app.route('/map', methods=['GET'])
def show_map_page():
    return render_template('/subpage/by_map.html')

@app.route('/favorites', methods=['GET'])
def show_favorites_page():
    return render_template('/subpage/preparing_page.html')

@app.route('/bymarkets', methods=['GET'])
def show_markets_page():
    return render_template('/subpage/preparing_page.html')

@app.route('/storetypes', methods=['GET'])
def show_store_types_page():
    return render_template('/subpage/preparing_page.html')

@app.route('/guide', methods=['GET'])
def show_guide_page():
    return render_template('/subpage/preparing_page.html')


## API 역할을 하는 부분

@app.route('/abc', methods=['GET'])
def listing():
    stores = list(db.stores.find({}, {'_id': False}))
    return jsonify({'all_stores':stores})


@app.route('/abc', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    return jsonify({'msg': '저장이 완료되었습니다!'})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)