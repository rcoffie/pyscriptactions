import requests 
import json 
import os 
import io 


response = requests.get("https://changelog.qgis.org/en/qgis/members/json/")

data = json.loads(response.text)


if not os.path.exists('data'):
    os.makedirs('data')


with io.open('data/data.json', 'w', encoding='utf=8') as f:
    f.write(json.dumps(data, ensure_ascii=False))