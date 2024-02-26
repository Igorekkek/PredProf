with open('products.csv', encoding='utf8') as file:
    # Преобразуем файл в удобный для работы на Python объект
    data = file.readlines()
    for i in range(len(data)):
        data[i] = [obj.strip() for obj in data[i].split(';')]

    # Добавляем столбец total
    data[0].append('total')
    for i in range(1, len(data)):
        line = data[i]
        data[i].append(str(float(line[3]) * float(line[4])));

    # Считает сумму продаж по закускам
    result_price = 0
    for i in range(1, len(data)):
        line = data[i]
        if line[0] == 'Закуски':
            result_price += float(line[-1])
    print('итоговая сумма по категории Закуски =', result_price)

# Записываем изменённые данные в новый файл
with open('products_new.csv', encoding='utf8', mode='w') as newfile:
    for line in data:
        newfile.write(';'.join(line) + '\n')

