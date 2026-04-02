# input()

from pywebio.output import put_markdown, put_text, put_image
from pywebio.input import input, slider, select, radio

import prices
import pictures

# Header
put_markdown("# ⛰ Реєстрація на шкільну поїздку")
put_markdown("---")

# menu

put_markdown("## 🚧 Меню:")

put_image(pictures.PICTURE_TRAIN)
put_text(f"🚆1 людина = {prices.PRICE_TRAIN} грн (в обидві сторони)")

put_image(pictures.PICTURE_BUS, width="472")
put_text(f"""1 автобус = 40 місць
ціна = {prices.PRICE_BUS} грн за автобус (за всю поїздку)
""")

# Order

put_markdown("## 📋 Замовлення:")

quantity_students = input("Скільки учнів буде у поїздці?", type="number", min=1, value=1)
quantity_teachers = input("Скільки вчителів буде у поїздці?", type="number", min=1, value=1)
transport = radio(
    "Оберіть транспорт:",
    options=[
        "🚌 Автобус",
        "🚆 Поїзд"
    ]
)

days = slider("Скільки днів поїздка?", min_value=1, max_value=14, value=1)

# Calculation
people = quantity_students + quantity_teachers

transport_cost = 0
buses = 0

if transport == "🚆 Поїзд":
    transport_cost = people * prices.PRICE_TRAIN

if transport == "🚌 Автобус":
    buses = (people + 39) // 40   # округлення вверх
    transport_cost = buses * prices.PRICE_BUS

living_cost = people * days * 400

total_cost = transport_cost + living_cost

discount = 0
if people > 30:
    discount = total_cost * 0.1

final_cost = total_cost - discount

# Final
put_markdown("## 📊 Результат:")

put_markdown(f"👥 Людей: {people}")

if transport == "🚌 Автобус":
    put_markdown(f"🚌 Автобусів: {buses}")

put_markdown(f"🚆 Транспорт: {transport_cost} грн")
put_markdown(f"🏨 Проживання: {living_cost} грн")

if discount > 0:
    put_markdown(f"💸 Знижка: {round(discount, 2)} грн")

put_markdown(f"## 💰 До сплати: {round(final_cost, 2)} грн")





