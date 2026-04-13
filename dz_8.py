# Завдання 1
numbers = [3, 7, 2, 9, 4, 6, 1, 8]

even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

doubled_even = [n * 2 for n in even_numbers]

if 8 in doubled_even:
    doubled_even.remove(8)

print(doubled_even)

# Завдання 2
words = ["apple", "banana", "kiwi", "pear", "banana", "plum"]

unique_words = []
for w in words:
    if w not in unique_words:
        unique_words.append(w)

long_words = [w for w in unique_words if len(w) > 4]

upper_words = [w.upper() for w in long_words]

print("BANANA" in upper_words)
print(upper_words)