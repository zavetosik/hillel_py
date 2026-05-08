import json
import requests


PDF_URL  = 'https://github.com/progit/progit2/releases/download/2.1.449/progit.pdf'
JSON_URL = 'http://api.open-notify.org/astros.json'

#pdf
response = requests.get(PDF_URL)

with open('progit.pdf', mode='bw') as file:
    file.write(response.content)

#JSON
response = requests.get(JSON_URL)

data = response.json()

with open('astros.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

