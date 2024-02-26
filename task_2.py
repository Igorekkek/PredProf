with open('products.csv', encoding='utf8') as file:
    # Преобразуем файл в удобный для работы на Python объект
    data = file.readlines()
    for i in range(len(data)):
        data[i] = [obj.strip() for obj in data[i].split(';')]

    # Сортируем по категории
    for i in range(1, len(data)):
        minelem = -1
        for j in range(i + 1, len(data)):
            if minelem == -1 or data[j][0] < data[minelem][0]:
                minelem = j
        data[i], data[minelem] = data[minelem], data[i]

    firstcat = data[1][0] # первая категорие
    mostex = -1 # индекс ниболее дорогово продукта из категории firstcat
    for i in range(1, len(data)):
        line = data[i]
        if firstcat == line[0]:
            if mostex == -1 or float(data[mostex][3]) < float(line[3]):
                mostex = i
        else:
            break

    print(f'В категории: {firstcat} самый дорогой товар: {data[mostex][1]} его цена за единицу товара составляет {data[mostex][3]}')
