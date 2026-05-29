from typing import Callable


# print
#
# some = print


# print(id(some   ))
# print(id(print   ))
#
# some(86878678)
# some(some)


# def base_foo():
#     print('base_foo was called')
#
#
#
# def foo(some_param):
#     print(some_param, 8888)
#     some_param()
#
#
# foo(base_foo)

def call_callable_function(func: Callable):

    def wrapper(*args, **kwargs):
        print('sandbox before')
        print(args)

        result = func(*args, **kwargs)  # 4, number_2=8

        print('sandbox after')
        return result

    return wrapper


@call_callable_function
def add_numbers(number_1: int, number_2: int):

    return number_1 + number_2
#
#
# apples = 3
# pears = 23
# fruits = add_numbers(number_1=apples, number_2=pears)

@call_callable_function
def print_string():
    print('111111,sdgjfdsfgjhdsjgdsjhgjds')
    print('222222,sdgjfdsfgjhdsjgdsjhgjds')


@call_callable_function
def print_string3():
    print('33333333,sdgjfdsfgjhdsjgdsjhgjds')





# print(id(print_string))
# print_string()

# print(print_string)

# print_string = call_callable_function(print_string)
# print_string3 = call_callable_function(print_string3)
# add_numbers = call_callable_function(add_numbers)

# print('----------------------')
# print(print_string)
print_string()
print_string3()
print_string3()

res = add_numbers(4, number_2=8)
# print(res)

