import letter
from letter import LETTER_TEMPLATE

name = input("Введіть ваше ім'я та прізвище: ")
date = input("Введіть дату поїздки: ")
persons = int(input("Введіть кількість осіб: "))

price_per_person = 15000

total_price = price_per_person * persons

if persons > 5:
    discount = total_price * 0.05
else:
    discount = 0

final_price = total_price - discount

letter = LETTER_TEMPLATE.format(
    name=name,
    date=date,
    persons=persons,
    price_per_person=price_per_person,
    total_price=int(total_price),
    discount=int(discount),
    final_price=int(final_price)
)

print(letter)