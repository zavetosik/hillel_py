
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']


def average(a: int | float, b: int | float, c: int | float) -> float:
    average_result = (a + b + c) / 3
    return average_result.__round__(2)



def foo(something) -> bool:
    foo_result = something % 2 == 0 and something > 10
    return foo_result

def foov2(text: str) -> int:
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

