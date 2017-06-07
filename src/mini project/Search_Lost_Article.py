#coding: utf-8
import os
import requests
import src.mylib
import lxml
import lxml.etree
import StringIO
import json
from pymongo import MongoClient


while True:
    s=' 찾고싶은 이동수단 입력(버스:b1,마을버스:b2,지하철1~4호선:s1,지하철5~8호선:s2,코레일:s3,지하철9호선:s4,법인택시:t1,개인택시:t2) : '
    print s.decode('utf-8')
    _wb_code = raw_input()
    if _wb_code not in ['b1','b2','s1','s2','s3','s4','t1','t2']:
        s=' 잘못입력하셨어요'
        print s.decode('utf-8')
    else:
        break

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=src.mylib.getKey(keyPath)
_url='http://openAPI.seoul.go.kr:8088'
_key=str(key['dataseoul'])
_type='xml'
_service='ListLostArticleService'
_start_index=1
_end_index=1000

_api=_url+"/"+_key+"/"+_type+"/"+_service+"/"+str(_start_index)+"/"+str(_end_index)+"/"+_wb_code
data = requests.get(_api).text

tree=lxml.etree.fromstring(data.encode('utf-8'))

client = MongoClient()
db=client['Article']
table=db['myCol']
stds=tree.findall('row')

db.use.Article

for elements in stds:
    db.myCol.insert_one({
        "id": elements[0].text,
        "name": elements[1].text,
        "url": elements[2].text,
        "title": elements[3].text,
        "date": elements[4].text,
        "take_place": elements[5].text,
        "contact": elements[6].text,
        "cate": elements[7].text,
        "position": elements[8].text,
        "get_place": elements[9].text,
        "thing": elements[10].text,
        "status": elements[11].text,
        "code": elements[12].text,
        "image": elements[13].text
    })

s= ' 찾고싶은 물건(지갑,쇼핑백,베낭,핸드폰,가방,서류봉투,옷,책,기타)'
print s.decode('utf-8')
_cate = raw_input()
print _cate.decode('CP949')

for tweet in table.find():
    if tweet['cate'] == _cate.decode('CP949'):
        print "name",tweet['name'],"cate",tweet['cate'],"contact",tweet['contact'],"get place",tweet['get_place'],"take place",tweet['take_place']
    
db.myCol.drop()