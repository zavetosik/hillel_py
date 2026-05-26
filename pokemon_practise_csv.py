with open('pokemon.csv', mode='r', encoding='utf-8') as file:

    file.readline()

    while True:
        line = file.readline()

        if not line:
            break

        data = line.strip().split(',')


        height = data[3]
        identifier = data[1]

        if height == "7":
            print(identifier)