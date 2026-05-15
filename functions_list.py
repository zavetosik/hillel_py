
def calc(a: int | float, b: int | float, operation: str = "sum") -> int | float:
    if operation == "sub":
        return a - b
    return a + b

def change_case(text: str, upper:bool = True) -> str:
    return text.upper() if upper else text.lower()

def sum_from_string(numbers:str, separator: str = ",") -> float:
    return sum(float(x) for x in numbers.split(separator))