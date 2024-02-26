with open('products.csv', encoding='utf8') as file:
    # Преобразуем файл в удобный для работы на Python объект
    data = file.readlines()
    for i in range(len(data)):
        data[i] = [obj.strip() for obj in data[i].split(';')]

# хеш таблица, ключ - категория, значение - кол-во товаров этой категории
d = dict()

# подсчёт всех значений
for i in range(1, len(data)):
    line = data[i]
    d[line[0]] = d.get(line[0], 0) + float(line[-1])

# поиск 10 наименее продаваемфых категорий
items = list(d.items())
items.sort(key=lambda x : float(x[-1]))
for i in range(10):
    print(f'{items[i][0]}, {items[i][1]}.')