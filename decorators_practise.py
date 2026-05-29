from typing import Callable
from datetime import datetime
from functools import wraps


def decorator_template_no_params(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


def logs_decorator(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('logs_decorator before')

        result = func(*args, **kwargs)
        with open(f'logs_{func.__name__}.csv', mode='a', encoding='utf-8') as log_file:
            log_file.write(f"{datetime.now()};{func.__name__};{args};{kwargs};{result}\n")

        print('logs_decorator after')
        return result

    return wrapper


def decorator_round_result(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator_round_result before')

        result = func(*args, **kwargs)
        if type(result) in (int, float):
            result = round(result, 1)
        print('decorator_round_result after')
        return result

    return wrapper

admin_login = '123'
admin_password = '123'


def decorator_admin_permission(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator_admin_permission before')
        input_admin_login = input('LOGIN: ')
        input_admin_password = input('PASSWORD: ')

        if input_admin_login == admin_login and input_admin_password == admin_password:
            result = func(*args, **kwargs)
            print('decorator_admin_permission after')
            return result

        return {'status': "not allowed"}

    return wrapper


@decorator_round_result
def return_str() -> str:
    return 'jsdgvjdfgjvgdfjg'


@decorator_admin_permission
@logs_decorator
@decorator_round_result
def add_numbers(number_1: float, number_2: float) -> float:
    print('add_numbers was called')
    result = number_1 + number_2
    return result


@logs_decorator
@decorator_round_result
def multiply_numbers(number_1: float, number_2: float) -> float:
    result = number_1 * number_2
    return result


@decorator_round_result
def divide_numbers(number_1: float, number_2: float) -> float:
    if number_2 == 0:
        return 0.0
    result = number_1 / number_2
    return result


res_1 = add_numbers(4.989767, 56.98)
print(res_1)

# res_2 = multiply_numbers(4.989767, 56.98)
# print(res_2)
#
# res_3 = divide_numbers(4.989767, 56.98)
# print(res_3)
# res_4 = return_str()
# print(res_4)
#
print(add_numbers)