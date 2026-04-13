from pprint import pprint

login = 'admin'
password = '123'
another_key = "key"

list_ = []
number = 66.9
test_dict = {'data': 123}

admin_data = {
    "login": "admin",
    "password": password,
    # another_key: another_key,
    "name": "Андрій",
    "hobbies": ['soccer', 'darts'],
    "age": 49,
    "address": {
        "city": "Одеса",
        'street': "Перша",
        'house': None
    },
    "is_married": True,
    "salary_usd": 3_000,
}

# print(type(number))

# get data

admin_age = admin_data['age']
print(admin_age)

pprint(admin_data, indent=4, width=40)

admin_wife_name = admin_data.get("wife_name")
print(admin_wife_name)

admin_salary_uds = admin_data.get("salary_usd", 1000)  # None => False
print(admin_salary_uds)
grn_to_usd_rate = 43.72
admin_salary_grn = round(admin_salary_uds * grn_to_usd_rate, 2)
print(admin_salary_grn)


admin_hobbies = admin_data.get('hobbies', [])
has_admin_hobbies = bool(admin_hobbies)
has_admin_hobbies = len(admin_hobbies) >= 1

if admin_hobbies:
    print(admin_hobbies)
    first_hobby = admin_hobbies[0]
    print(first_hobby)

admin_city = admin_data.get('city')