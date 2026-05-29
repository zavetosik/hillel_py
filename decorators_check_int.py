from typing import Callable
from functools import wraps

def decorator_check_int(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == int:
            result += 10
        return result
    return wrapper


@decorator_check_int
def add_numbers(number_1: int | float, number_2: int | float) -> int | float:
    result = number_1 + number_2
    return result


res_1 = add_numbers(25, 15)
print(res_1)

res_2 = add_numbers(10.6894, 6.747)
print(res_2)