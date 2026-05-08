with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:

    # пропускаємо заголовок
    file.readline()

    while True:
        line = file.readline()

        if not line:
            break

        data = line.strip().split(';')

        # перевірка кількості колонок
        if len(data) <= 8:
            continue

        iso_country = data[5]
        name = data[2]

        if iso_country == 'UA':
            print(name)