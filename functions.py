from utils import get_distance, calculate_summa, get_number_5, print_msg

print_msg()


number_5 = get_number_5()
s = number_5 + 5
print(f"{number_5=}")

result_calculate_summa = calculate_summa(number_1=1, number_2=9.6)
print(result_calculate_summa)
mult = result_calculate_summa * 20
print(mult)

distance1 = get_distance(time_seconds=2, velocity_meters_per_second=2)
print(distance1)

distance2 = get_distance(time_seconds=2.522, velocity_meters_per_second=297.875765)
print(distance2)