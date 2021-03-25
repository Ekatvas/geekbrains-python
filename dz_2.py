# 1 Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
list_1=[1, '2', 3.3, None, True]
for i in list_1:
    print(type(i))

# # 2 Для списка реализовать обмен значений соседних элементов, т.е.
# # Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# # При нечетном количестве элементов последний сохранить на своем месте.
# # Для заполнения списка элементов необходимо использовать функцию input().
# list_2=[]
# for i in range(int(input('Введите кол-во элементов списка: '))):
#     list_2.append(int(input()))
# for i in range(0, len(list_2), 2):
#     if i!=len(list_2)-1:
#         list_2[i], list_2[i+1] = list_2[i+1], list_2[i]
# print(list_2)

# # 3 Пользователь вводит месяц в виде целого числа от 1 до 12.
# # Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# # Напишите решения через list и через dict.
#
# seasons_list = ['winter', 'spring', 'summer', 'autumn']
# seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
# month = int(input('Введите месяц по номеру: '))
# if month ==1 or month == 12 or month == 2:
#     print(seasons_dict.get(1))
#     print(seasons_list[0])
# elif month == 3 or month == 4 or month ==5:
#     print(seasons_dict.get(2))
#     print(seasons_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print(seasons_dict.get(3))
#     print(seasons_list[2])
#
# elif month == 9 or month == 10 or month == 11:
#     print(seasons_dict.get(4))
#     print(seasons_list[3])
# else:
#     print('Такого месяца не существует')

# # 4 Пользователь вводит строку из нескольких слов, разделённых пробелами.
# # Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# # Если в слово длинное, выводить только первые 10 букв в слове.
# string=input('Введите предложение: ')
# words=string.split()
# for i in range(len(words)):
#     print(str(i+1)+' '+words[i][:10])

# # 5 Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# # У пользователя необходимо запрашивать новый элемент рейтинга.
# # Если в рейтинге существуют элементы с одинаковыми значениями,
# # то новый элемент с тем же значением должен разместиться после них.
# list_3=[7, 5, 3, 3, 2]
# x=int(input('Введите число: '))
# list_3.append(x)
# print(sorted(list_3, reverse=True))

# 6
products=[]

number=int(input('Введите кол-во новых товаров: '))
for i in range(number):
    name=input(f'Введите название товара №{i+1}: ')
    price=float(input(f'Введите цену товара №{i+1}: '))
    amount=int(input(f'Введите кол-во товара №{i+1}: '))
    ed=input(f'Введите единицы измерения №{i+1}: ')

    product={
        'Название' : name,
        'Цена': price,
        'Количество' : amount,
        'Ед' : ed
    }
    products.append((i+1, product))
print(products)
