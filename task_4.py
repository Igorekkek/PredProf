def gencode(name, date):
    '''
    :param name: string название товара
    :param date: string дата поступления
    :return: string промокод для данного товара
    '''
    day, month, year = date.split('.')
    p1 = name[-2:][::-1]
    p2 = month[::-1]
    res = name[:2] + day + p1 + p2
    return res.upper()

with open('products.csv', encoding='utf8') as file:
    # Преобразуем файл в удобный для работы на Python объект
    data = file.readlines()
    for i in range(len(data)):
        data[i] = [obj.strip() for obj in data[i].split(';')]

# Создаём новый файл
with open('product_promo.csv', encoding='utf8', mode='w') as newfile:
    # Добавляем новый столбец
    data[0].append('promocode')
    for i in range(1, len(data)):
        line = data[i]
        data[i].append(gencode(line[1], line[2]))

    # Записываем данные в новый файл
    for line in data:
        newfile.write(';'.join(line) + '\n')