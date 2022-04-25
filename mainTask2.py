# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_int = 4
my_float = 1.3
my_str = "Hello my neighbours"
my_list = ['a', '2']
my_tuple = ('f', '3')
my_dict = {'city': 'Moscow', 'country': 'Russia'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')

# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
my_list = input('Enter the numbers - ').split()
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)

# Вар 01
my_list = list(input('Enter the numbers without space = '))

idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1

my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
print('Изменённый список: ', my_list)

# Вар 02
user_list = input('Enter the numbers with space - ').split()
for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))
print(user_list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
season_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'outumn', 'outumn', 'outumn']
season_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer', 9: 'outumn',
               10: 'outumn', 11: 'outumn', 12: 'winter'}
month = int(input('Enter the number of month '))
if month in season_dict:
    #print(season_list[month - 1])
    print(season_dict[month])
else:
    print('Does not exist')

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
# Вар 1
my_string = input('Введите строку из нескольих слов через пробел: ').split()
for i, word in enumerate(my_string, 1):
    print(f'{i} {word[:10]}')

# Вар 2
s = input('Enter the numbers with space ').split()
for i, word in enumerate(s, 1):
    print(i, word) if len(word) <= 10 else print(i, word[:10])

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде.

rating = [7, 5, 3, 3, 2]
for _ in range(3):
    i = int(input('Введите новый элемент рейтинга в виде натуралього числа: '))
    flag = False
    for j in range(len(rating)):
         if rating[j] < i:
             rating.insert(j, i)
             flag = True
             break
    if not flag:
        rating.append(i)
    print(*rating)


# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
#
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
i = 1
goods = []
n = int(input('Сколько наименований товаров хотите ввести? '))
for _ in range(n):
    name = input('Товар: ')
    price = int(input('Цена: '))
    quantity = int(input('Кол - во: '))
    measure = input('ед. изм.: ')
    goods.append((i, {'название': name, 'цена': price, 'кол-во': quantity, 'ед. изм.': measure}))
    i += 1
print(goods)
goods_dict = {'название': [], 'цена': [], 'кол-во': [], 'ед. изм.': []}
for good in goods:
    goods_dict['название'].append(good[1]['название'])
    goods_dict['цена'].append(good[1]['цена'])
    goods_dict['кол-во'].append(good[1]['кол-во'])
    if good[1]['ед. изм.'] not in goods_dict['ед. изм.']:
        goods_dict['ед. изм.'].append(good[1]['ед. изм.'])
print(goods_dict)

