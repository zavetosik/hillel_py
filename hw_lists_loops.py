
# first task

numbers = [1, 5, 2, 8, 3, 7]

max_num = max(numbers)
print(max_num)

min_num = min(numbers)
print(min_num)

all_num = sum(numbers)
print(all_num)

print("------------------------------------")
# second task

grades = [10, 8, 12, 7, 9]

all_grades = sum(grades)

average = all_grades / len(grades)
for grade in grades:
    if grade > average:
        print(grade)