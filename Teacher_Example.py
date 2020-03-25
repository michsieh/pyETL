from bs4 import BeautifulSoup
from pprint import pprint
import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
url = 'https://place.qyer.com/poi.php?action=list_json'

data_str = """page: 1
type: city
pid: 52
sort: 32
subsort: all
isnominate: -1
haslastm: false
rank: 6"""

data = {r.split(': ')[0] : r.split(': ') for r in data_str.split('\n')}

res =requests.post(url, headers=headers, data=data)
json_data = json.loads(res.text)
# pprint(json_data)

for i in range(0,5) :
    print('page: ', i+1)
    data['page'] = str(i+1)
    res = requests.post(url, headers=headers, data=data)
    json_data = json.loads(res.text)
    print(json_data['data']['list'][0]['cnname'])
    print('gade:', json_data['data']['list'][0]['grade'])
    print('=================================================================================')