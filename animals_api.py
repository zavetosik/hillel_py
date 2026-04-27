import requests
from pprint import pprint

url = 'https://script.google.com/macros/s/AKfycbxjMAID2Lv8nzsRa6g1BoqsIJYR07Gg_CgcSRmRn5JfeFZ2HvDq906VhyFBy8MdIcAG4Q/exec'
response = requests.get(url=url, params={})
response_json = response.json()


animals = response_json['animals']

total_care_cost_venomous = 0

for cost in animals:
    if cost['is_venomous'] == "так":
        total_care_cost_venomous += cost['care_cost'] * cost['count']

print(f'{total_care_cost_venomous}')

africa_count = 0

for count_africa in animals:
    if count_africa['continent'] == 'Африка':
        africa_count += count_africa['count']

print(f'{africa_count}')