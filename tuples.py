

user = {
    'name': 'Alex',
    'age': 15
}

for key in user:
    print(key)


user.update(weight=56, city='Odesa')
print(user)

keys = user.keys()
print(keys)
values = user.values()
print(values)

for value in user.values():
    print(value)

items = user.items()
print(items)

some_list = [5,]
print(some_list)

# notes = (3, 3, 6, 8, 5)
notes = 3,
# c = notes.count(3)
# print(c)
print(notes)
for note in notes:
    print(note)


some_tuple = ('name', 'Alex')
key, value = some_tuple
print(key, value)
print(some_tuple)


name, surname, age, *other = 'Alex', 'Trump', 66, # 'tennis', 667
print(f'{other=}')


for key, value  in user.items():
    print(key, value)
    if key == 'age':
        print('Age in keys')
