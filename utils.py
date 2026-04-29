def get_distance(time_seconds: int | float, velocity_meters_per_second: int | float) -> float:
    distance = time_seconds * velocity_meters_per_second * 1.0
    distance = round(distance, 2)
    return distance


def print_msg() -> None:
    print('Welcome')
    print('message')
    # return
    # return None


def get_number_5() -> int:  # int float str list dict None
    print('function get_number_5 was called')
    number_5_to_give = 5
    return number_5_to_give


def foo():
    return


def calculate_summa(number_1: int | float, number_2: int | float) -> float:
    result = number_1 + number_2
    return result * 1.0

