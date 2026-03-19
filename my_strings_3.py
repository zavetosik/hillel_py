import messages

# from messages import MSG_INPUT_BREAD_QUANTITY

bread_quantity = input(messages.MSG_INPUT_BREAD_QUANTITY).strip().lstrip("0")
print(bread_quantity)

is_correct_bread_quantity = bread_quantity.isdigit()
print(is_correct_bread_quantity)
true = True
false = False

if is_correct_bread_quantity:
    print(messages.MSG_CORRECT_INPUT)
else:
    print(messages.MSG_INCORRECT_INPUT)

print(messages.MSG_FINISH)
