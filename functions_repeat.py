
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']


def get_average(number_1: int | float, number_2: int | float, number_3: int | float) -> float:
    average_result = (number_1 + number_2 + number_3) / 3
    return round(average_result, 2)



def get_check(number_check: int | float) -> bool:
    check_result = number_check % 2 == 0 and number_check > 10
    return check_result

def count_vowels(text_vowels: str) -> int | float:
    count_result = 0

    for char in text_vowels:
        if char in vowels:
            count_result += 1

    return count_result



