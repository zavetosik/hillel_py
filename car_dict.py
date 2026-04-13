from pprint import pprint

# car info
car_data = {
    "model": "Toyota RAV4 Hybrid 2025",
    "price_uah": 1800000,
    "engine_volume": 2.5,
    "weight_kg": 2150,
    "max_speed_kmh": 180,
    "fuel_per_100km": 5.6,
    "interior_features": [
        "Шкіряне оздоблення салону",
        "Двозонний клімат-контроль",
        "Мультимедійна система з сенсорним екраном",
    ],
    "trunk": {
        "volume": 580,
        "volume_folded": 1690
    }
}
# car add info
car_data["max_trailer_weight"] = 1650

#car get info

car_model = car_data.get("model")


car_price = car_data.get("price_uah")


interior = car_data.get("interior_features")
first_feature = interior[0]

trunk_data = car_data.get("trunk")
fold_trank = trunk_data.get("volume_folded")


insurance = car_price * 0.005
car_data["insurance_payment"] = insurance

# 200km
fuel_consumption = car_data.get("fuel_per_100km", 0)
fuel_needed = (fuel_consumption / 100) * 200
fuel_price = 93
trip_cost = fuel_needed * fuel_price

pprint(car_data, indent=4, width=40)
print(trip_cost)
