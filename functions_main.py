from functions_list import calc, change_case, sum_from_string

print(calc(10, 5))
print(change_case("hello"))
print(sum_from_string("1,2,3"))

print(calc(a=10, b=5, operation="sub"))
print(change_case(text="Hello", upper=False))
print(sum_from_string(numbers="1;2;3", separator=";"))

params1 = {"a": 7, "b": 3, "operation": "sum"}
params2 = {"text": "world", "upper": True}
params3 = {"numbers": "4,5,6", "separator": ","}

print(calc(**params1))
print(change_case(**params2))
print(sum_from_string(**params3))