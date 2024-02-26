with open('products.csv', encoding='utf8') as file:
    # Преобразуем файл в удобный для работы на Python объект
    data = file.readlines()
    for i in range(len(data)):
        data[i] = [obj.strip() for obj in data[i].split(';')]

# ввод категории
category = input()
while category != 'молоко':
    res_id = -1 # индекс минимального товара

    # поиск товара соответствующей категории
    for i in range(1, len(data)):
        line = data[i]
        if line[0] == category:
            if res_id == -1 or float(line[3]) < float(data[res_id][3]):
                res_id = i

    if res_id == -1:
        print('Такой категории не существует в нашей БД')
    else:
        print(f'В категории: {data[res_id][0]} товар: {data[res_id][1]} был куплен {data[res_id][-1]} раз')
    category = input()