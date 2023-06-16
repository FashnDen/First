# d = int(input("Сколько дней до экзамена?"))
# p = int(input("Сколько страниц для подготовки?"))
# print("В день нужно читать:", p//d)
# import Proga
# import random

# print(films)
# print(films[-1])

# films = []
# print(films)
# film_1 = input("Введите фильм")
# film_2 = input("Введите фильм")
# film_3 = input("Введите фильм")
# films.append(film_1)
# films.append(film_2)
# films.append(film_3)
# print(films)
# print(films[-1])

# facts = ["Не все китайцы на одно лицо", "Киты могут взрываться", "Для мух мы двигаемся очень медленно"]
# a = int(input("Введите номер интересующего факта"))
# b = a - 1
# print(facts[b])

# cords = [[2, 4], [5, 6], [3, 7]]
# a = ["string", 1, True]

# score = [5, 5, 5, 4, 4, 5]
# del score[3]


# films = ["Матрица", "Терминатор", "Человек паук"]
# print(films)
# l = len(films)
# print(l)

# print(films)
# films.remove("Матрица")
# print(films)

# Кол-во элементов х
# score = [5, 5, 5, 4, 4, 5]
# films = ["Матрица", "Терминатор", "Человек паук"]
# k = films.count("Матрица")
# print(k)

# # Сортировка
# score = [5, 5, 5, 4, 4, 5]
# print(score)
# score.sort(reverse=1)
# print(score)
# score.sort()
# print(score)

# # Возврат индекса
# score = [5, 5, 5, 4, 4, 5]
# i = score.index(5)
# print(i)

# # Очистка списка
# score = [5, 4, 3, 2, 1]
# print(score)
# score.clear()
# print(score)

# score = [5, 4, 3, 2, 1]
# x = sum(score) // len(score)
# print(x)
# m = max(score)
# print(m)
# s = min(score)
# print(s)
# c = score.count(5)
# print(c)

# Срез
# list[start:stop:step]
# score = [5, 4, 3, 3, 4, 2, 1, 2, 4, 4, 3, 2, 1]
# print(score)
# print(score[3:])
# print(score[3:8])
# print(score[:3])
# print(score[::-1])

# elements = ["water", "fire", "earth", "air"]
# print(elements[::-1])

# scores = [1, 2, 3, 4, 5]
# print(sum(scores))
# a = scores[0]
# b = scores[1]
# c = scores[2]
# d = scores[3]
# e = scores[4]
# print(a + b + c + d + e)

# shoplist = ["Помидоры", "Огурцы", "Картофель", "Лук", "Масло"]
# shoplist.append("Сыр")
# shoplist[2 - 1] = "Колбаса"
# print(len(shoplist))
# shoplist.sort()
# del(shoplist[-1])



# a = [1, 4123, 32, -234, 56, 23]
# r = random.choice(a)
# r = random.randint(1, 100)
# import random

# import math
# m = math.
# print

# import os
# os.mkdir("new")

# range(start, stop, range)

# for i in range(100):
#     print(i)

# for i in range(5, 10, 2):
#     print(i)

# for i in range(5, 10, 2):
#     print(i)

# facts = ["Не все китайцы на одно лицо", "Киты могут взрываться", "Для мух мы двигаемся очень медленно"]
# for i in facts:
#     print(i)

# for i in range(5):
#     a = int(input("Введите число"))
#     s += a
# print(s)

# films = []
# for i in range(3):
#     film = input("Введите фильм: ")
#     films.append(film)
#     print(films)
# print(films)

# hys = []
# for i in range(6):
#     sal = int(input("Введите зарплату: "))
#     hys.append(sal * 0.3)
# print(sum(hys))

# numbers = []
# for i in range(101):
#     numbers.append(i)
# print(numbers)

# animals = []
# description = []
# for i in range(3):
#     animals.append(input("Введите животное: "))
#     description.append(input("Введите описание: "))
# for i in range(3):
#     print(random.choice(description) + " " + random.choice(animals))

# numbers = []
# for i in range(30):
#     numbers.append(random.randint(0, 5))
# print(numbers.count(5))

# temperature = int(input("Введите температуру: "))
# if temperature <= -25:
#     print("Очень холодно")
# elif -24 <= temperature <= -10:
#     print("Холодно")
# elif -9 <= temperature <= 0:
#     print("Прохладно")
# elif 1 <= temperature <= 10:
#     print("Тепло")
# elif 11 <= temperature <= 25:
#     print("Жарко")
# else:
#     print("Очень жарко")

# numbers = []
# n = int(input("Введите количество элементов списка: "))
# a = int(input("Введите минимальную границу списка: "))
# b = int(input("Введите максимальную границу списка: "))
# for i in range(n):
#     numbers.append(random.randint(a, b))
# numbers.sort()
# print(numbers)

# game = ["Орёл", "Решка"]
# n = random.choice(game)
# chosen = input("Выберите сторону монетки: ")
# if chosen == n:
#     print("Вы выиграли")
# else:
#     print("Вы проиграли")

# a = {
#     "молоко": 65,
#     "кефир": 70,
#     "список": [12, 3, 2536, 543],
#     "словарь": {
#         "ключ": "значение"
#     }
# }
#
# s = []
#
# print(a["словарь]["ключ"])

# english_dict = {
#     "яблоко": "apple",
#     "молоко": "milk",
#     "кот": "cat"
# }
# word = input("Введите слово на русском")
# if word in english_dict:
#     print(word + " на английском языке будет: " + english_dict[word])
# else:
#     print("Такого слова нет в словаре")


# films_dict = {
#     "Начало": "Леонардо ди каприо",
#     "Человек паук": "Том Холанд",
#     "Терминатор": "Арнольд Шварцненеггер",
#     "Драйв": "Райан Гослинг"
# }
#
# favorite_actor = "Райан Гослинг"
# film = input("введите фильм, который хотите посмотреть")
# if film in films_dict:
#     actor = films_dict[film]
#     if actor == favorite_actor:
#         print("Этот фильм точно стоит посмотреть")
#     else:
#         print("Я бы не тратил своё время")
# else:
#     print("Такого фильма в базе нет")


# a = {
#     "молоко": 65,
#     "кефир": 70,
#     "список": [12, 3, 2536, 543],
#     "словарь": {
#         "ключ": "значение"
#     }
# }
# print(a.get("чипсы", "Такого ключа нет"))


# a = {
#     "молоко": 65,
#     "кефир": 70,
#     "список": [12, 3, 2536, 543],
#     "словарь": {
#         "ключ": "значение"
#     }
# }

# Список из тг
# questions = [
#     {
#         'question': 'Кто из героев Киновселенной Marvel начал знакомство с Землёй, попав под грузовик?',
#         'answers': ['Фил Колсон', 'Халк', 'Капитан Америка', 'Правильного ответа нет'],
#         'right_answer': 4
#     },
#     {
#         'question': 'Как звучит полное имя младшего брата Тора?',
#         'answers': ['Локи Одинсон', 'Локи Эриксон', 'Локи Лафейсон', 'Правильного ответа нет'],
#         'right_answer': 3
#     },
#     {
#         'question': 'Какой суперзлодей отличился тем, что за очень короткое время собрал в ангаре сотни управляемых дронов для армии США?',
#         'answers': ['Иван Ванко', 'Альтрон', 'Танос', 'Правильного ответа нет'],
#         'right_answer': 1
#     },
#     {
#         "question": "Как называется классический молот Тора?",
#         "answers": ["Громобой", "Мьелнир", "Убиватор_3000", "Штормио"],
#         "right_answer": 2
#     },
#     {
#         "question": "Из чего сделан молот Тора?",
#         "answers": ["Неизвестный материал космического происхождения", "Вибраниум", "Железо", "Уру"],
#         "right_answer": 4
#     }
# ]
# right_answers = 0
# for question in questions:
#     print(question["question"])
#     answer_number = 0
#     for answer in question["answers"]:
#         answer_number += 1
#         print(answer_number, ". ",  answer)
#     user_answer = int(input("Введите ваш ответ: "))
#     if user_answer == question["right_answer"]:
#         print("Верно")
#         right_answers += 1
#     else:
#         print("Неверно")
#     print("-----------------------")
#     print(" ")
# if right_answers >= 3:
#     print("Ты победил")
# else:
#     print("Ты проиграл")
# print("Правильных ответов:", right_answers)


# songs_playlist = {
#     "Curcus": 4.95,
#     "Absolute": 3.65,
#     "HDMI": 2.98,
#     "Notion": 3.05,
#     "Yeezy": 2.32,
#     "Savage": 3.49,
#     "Adderall": 4.26
# }
# number_songs = int(input("Сколько песен выбрать? "))
# length = 0
# for i in range(number_songs):
#     song = input("Введите название песни: ")
#     length += songs_playlist[song]
# print("Общее время звучания песен: ", length)

# product = {
#     "Видеокарта": "2653",
#     "Процессор": "1542",
#     "Кулер": "4853",
#     "Плашка памяти": "3269",
#     "Материнская плата": "5486",
#     "Жёсткий диск": "6781",
# }
# store = {
#     "2653": [
#         {"quantity": 12, "price": 13450},
#         {"quantity": 10, "price": 5600},
#         {"quantity": 6, "price": 23400},
#         {"quantity": 20, "price": 59000}
#     ],
#     "1542": [
#         {"quantity": 15, "price": 12000},
#         {"quantity": 7, "price": 15300},
#         {"quantity": 8, "price": 3900},
#         {"quantity": 12, "price": 26000},
#         {"quantity": 2, "price": 9900},
#     ],
#     "4853": [
#         {"quantity": 25, "price": 2300},
#         {"quantity": 30, "price": 1500},
#         {"quantity": 22, "price": 4000},
#     ],
#     "3269": [
#         {"quantity": 42, "price": 2450},
#         {"quantity": 50, "price": 6500},
#         {"quantity": 26, "price": 1400},
#         {"quantity": 12, "price": 3250},
#     ],
#     "5486": [
#         {"quantity": 6, "price": 56300},
#         {"quantity": 4, "price": 24500},
#         {"quantity": 16, "price": 14590},
#     ],
#     "6781": [
#         {"quantity": 15, "price": 2130},
#         {"quantity": 19, "price": 3540},
#         {"quantity": 21, "price": 4560},
#         {"quantity": 12, "price": 5680},
#         {"quantity": 8, "price": 9800},
#     ],
# }
# for product_name, product_code in product.items():
#     total_quantity = 0
#     total_cost = 0
#     for product in store[product_code]:
#         item_quantity = product['quantity']
#         item_cost = product['price']
#         total_cost += item_quantity * item_cost
#         total_quantity += item_quantity
#     print('{0} - {1} шт, общая стоимость {2} рублей'.format(product_name, total_quantity, total_cost))


# questions = [
#     {
#         'question': 'Кто из героев Киновселенной Marvel начал знакомство с Землёй, попав под грузовик?',
#         'answers': ['Фил Колсон', 'Халк', 'Капитан Америка', 'Правильного ответа нет'],
#         'right_answer': 4
#     },
#     {
#         'question': 'Как звучит полное имя младшего брата Тора?',
#         'answers': ['Локи Одинсон', 'Локи Эриксон', 'Локи Лафейсон', 'Правильного ответа нет'],
#         'right_answer': 3
#     },
#     {
#         'question': 'Какой суперзлодей отличился тем, что за очень короткое время собрал в ангаре сотни управляемых дронов для армии США?',
#         'answers': ['Иван Ванко', 'Альтрон', 'Танос', 'Правильного ответа нет'],
#         'right_answer': 1
#     },
#     {
#         "question": "Как называется классический молот Тора?",
#         "answers": ["Громобой", "Мьелнир", "Убиватор_3000", "Штормио"],
#         "right_answer": 2
#     },
#     {
#         "question": "Из чего сделан молот Тора?",
#         "answers": ["Неизвестный материал космического происхождения", "Вибраниум", "Железо", "Уру"],
#         "right_answer": 4
#     }
# ]
# right_answers = 0
# name = input("Введите имя: ")
# for question in questions:
#     print(question["question"])
#     answer_number = 0
#     for answer in question["answers"]:
#         answer_number += 1
#         print(answer_number, ". ",  answer)
#     user_answer = int(input("Введите ваш ответ: "))
#     if user_answer == question["right_answer"]:
#         print("Верно")
#         right_answers += 1
#     else:
#         print("Неверно")
#     print("-----------------------")
#     print(" ")
# if right_answers >= 3:
#     print("Ты победил")
# else:
#     print("Ты проиграл")
# # print("Правильных ответов:", right_answers)
#
# file = open("result.txt","a")
# file.write(name + ": " + str(right_answers) + "\n")
# file.close()
#
# fileR = open("result.txt","r")
# print(fileR.read())


# Функции

# def summ(a):
#     s = a + 5
#     return s
#
# result = summ(4)
# print(result)
#
# def summ(a):
#     return a + 5
# print(summ(4))
#
# def calculator(a, b, operand):
#     if operand == "+":
#         result = a + b
#     elif operand == "-":
#         result = a - b
#     elif operand == "*":
#         result = a * b
#     elif operand == "/":
#         result = a / b
#     else:
#         result = "Я не знаю такой операции"
#     return result
#
# num_1 = int(input("Введите число: "))
# num_2 = int(input("Введите число: "))
# op = input("Введите операцию (+,-,*,/): ")
# r = calculator(num_1, num_2, op)
# file = open("results", "a")
# file.write(str(r) + "\n")
# file.close()
# print(r)

# def summa_n(N):
#     s = 0
#     for i in range(1, N + 1):
#         s += i
#     print(f"Я знаю, что сумма чисел от 1 до {N} равна {s}")
# a = int(input("Введите число: "))
# summa_n(a)

# def greeting(visitors):
#     print('Привет!')
#     print('Добро пожаловать!')
# visitors = int(input("Введите количество поситителей: "))
# for i in range(visitors):
#     a = input('Зайдёте? Да/Нет: ')
#     if a == 'Да':
#         greeting(visitors)
#     print('Следующий.\n')

# from tkinter import *
#
# window = Tk()
# window.geometry('700x500')
# window.title('Самый сложный тест по вселенной Marvel')
#
# facts = [
#     {'text': 'Человеческое имя Халка - Брюс Беннет', 'right': 1},
#     {'text': 'Уолт Дисней является создателем вселенной Marvel', 'right': 0},
#     {'text': 'До появления костюма супергероя, человек муравей занимался воровством', 'right': 1},
#     {'text': 'Выдуманный город Дженоша является родиной Черной пантеры', 'right': 0}
# ]
#
# cur_q = 0
# points = 0
#
# def check():
#     global cur_q, points
#     answer = var.get()
#     if bool(answer) == facts[cur_q]['right']:
#         points += 1
#     if cur_q < len(facts)-1:
#         cur_q += 1
#         fact['text'] = facts[cur_q]['text']
#     else:
#         points_label = Label(text='Вы набрали ' + str(points) + ' очка', font=('Arial', 34), fg='red', bg='white')
#         points_label.place(x=0, y=0, width=700, height=250)
#
# label_title = Label(text = 'Тестирование по вселенной Marvel', font=('Arial', 24), fg='white', bg='red')
# label_title.place(width=700, height=50, x=0, y=0)
#
# fact = Message(text=facts[0]['text'], font=('Arial', 14),
#          width=680, borderwidth=0)
# fact.place(x=10, y=70)
#
# var = IntVar()
# true = Radiobutton(text='Верно', variable=var, value=1)
# true.place(x=10, y=120)
#
# false = Radiobutton(text='Неверно', variable=var, value=0)
# false.place(x=10, y=170)
#
# b = Button(text='Ответить', font=('Arial', 24), fg='black', command=check)
# b.place(x=200, y=130)
#
#
#
# window.mainloop()

# from tkinter import *
# import random
# import time
#
# window = Tk()
# window.geometry('700x500')
# window.title('Кликер')
#
# points = 0
# button1_points = 0
# button2_points = 0
#
# def check1():
#     global points
#     global button1_points
#     global button2_points
#     b.place(x=random.randint(1,550),y=random.randint(1,350))
#     points +=1
#     button1_points +=1
#     button2_points = 0
#     label['text'] = points
#     if points == 20:
#         b.configure(bg='red')
#         time.sleep(2)
#     if button1_points - button2_points == 10:
#         a.configure(text='Ну пожалуйста...')
#     else:
#         a.configure(text='нажми меня')
# def check2():
#     global points
#     global button1_points
#     global button2_points
#     a.place(x=random.randint(1,550),y=random.randint(1,350))
#     points +=1
#     button2_points +=1
#     button1_points = 0
#     label['text'] = points
#     if points == 20:
#         a.configure(bg='green')
#         time.sleep(2)
#     if button2_points - button1_points == 10:
#         b.configure(text='Ну пожалуйста...')
#     else:
#         b.configure(text='нажми меня')
# b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check1)
# b.place(x=200,y=130)
# a = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check2)
# a.place(x=130,y=200)
# label = Label(text = points, font=('Arial',15), fg='black')
# label.place(x=10,y=10)
#
# window.mainloop()

# from tkinter import *
#
# window = Tk()
# window.geometry('900x300')
# window.resizable(width=False, height=False)
# # window.overrideredirect(True)
# window.config(bg='black')
#
# text = Label(text='Ваш компьютер заражён!!', bg='black', font=('Courier New', 34), fg='green')
# text.place(x=100, y=100, width=700, height=100)
#
# count_text = Label(text='6', fg='green', bg='black', font=('Courier New', 34))
#
# def count_start():
#     if int(count_text['text']) > 0:
#         count_text['text'] = int(count_text['text'])-1
#         count_text.place(x=250, y=25, width=400, height=100)
#         window.after(1000, count_start)
#
#     else:
#         width = window.winfo_width()
#         height = window.winfo_height()
#         window.geometry(f'{width}x{height}+0+0')
#
#         photo = PhotoImage(file='skelet.gif')
#         label = Label(image=photo, bg='black')
#         label.image = photo
#         label.place(width=width, height=height, x=0, y=0)
#
# def on_close():
#     count_start()
#
# window.protocol("WM_DELETE_WINDOW", on_close)
#
# window.mainloop()

# from tkinter import *
#
# window = Tk()
# window.geometry('900x300')
# window.resizable(width=False, height=False)
#
# text = Label(text='ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!', font=('Arial', 20), fg='orange')
# text.place(x=100, y=0, width=700, height=100)
#
# def prize():
#     text.configure(text='Чтобы забрать выйгрыш необходимо внести 1000руб.')
#
# b = Button(text='ПОЛУЧИТЬ ВЫЙГРЫШ!', font=('Arial', 20), fg='black', command=prize)
# b.place(x=250,y=130)
#
# def on_close():
#     print('Hello')
#
# window.protocol("WM_DELETE_WINDOW", on_close)
#
# window.mainloop()

# dogs_points = [120, 152, 12, 164, 59, 598]
# min_p= min(dogs_points)
# max_p = max(dogs_points)
# ind_min_p = dogs_points.index(min_p)
# ind_max_p = dogs_points.index(max_p)
# dogs_points[ind_min_p] = max_p
# dogs_points[ind_max_p] = min_p
# print(dogs_points)




# from tkinter import *
#
# window = Tk()
# window.geometry('1200x600')
# window.resizable(width=False, height=False)
# window.title('Попробуй закрыть')
#
# def tap():
#     b.configure(text='Не вышло((')
#
# b = Button(text='Может стоит нажать сюда?', font=('Arial', 20), fg='black', bg='red', command=tap)
# b.place(x=250,y=130)
#
# def create():
#     b.place(x=random.randint(1, 550), y=random.randint(1, 350))
#     b.configure(text='Может стоит нажать сюда?')
# def on_close():
#     create()
# window.protocol("WM_DELETE_WINDOW", on_close)
#
# window.mainloop()

#import requests
# from bs4 import BeautifulSoup
#
# adress = input('Введите ссылку: ')
# response = requests.get(adress)
# response = response.content
# html = BeautifulSoup(response, 'html.parser')
# items = [h3.text for h3 in html.findAll('h3')]
# print(items)


# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
# response = response.content
# html = BeautifulSoup(response, 'html.parser')
# device_info = html.findAll(class_ = 'row ecomerce-items ecomerce-items-ajax')
# print(device_info)

# import requests
# from bs4 import BeautifulSoup
# import random
# response = requests.get('https://store.steampowered.com/?l=russian')
# response = response.content
# html = BeautifulSoup(response, 'html.parser')
# genres = {
#     'Экшен': '1',
#     'Ролевые игры': '2',
#     'Стратегия': '3',
#     'Приключенческая игра': '4',
#     'Симулятор': '5',
#     'Спорт и гонки': '6'
# }
# choise

# a = 0
# s = 0
# while a != -1:
#     s += a
#     a = int(input())
# print(s)

# user_wish = ''
# while user_wish != 'хватит':
#     user_wish = input('Чем бы вы хотели заняться?: ').lower()
#     if user_wish == '':
#         get_interesting_fact()
#     elif user_wish == '':
#         get_concert()
#     elif user_wish == '':
#         get_event()
#     else:
#         print('Может остаться дома?...')

# from fpdf import FPDF
#
# pdf = FPDF('P', 'cm', (10,20))
# pdf.add_page()
#
# pdf.add_font('courier', '', 'C:\Windows\Fonts\Cour.ttf', uni=True)
#
# pdf.set_text_color(0, 255, 0)
# pdf.set_fill_color(150, 50, 168)
# pdf.set_draw_color(0, 0, 255)
#
# pdf.set_font('courier', size=20)
# pdf.cell(8, 3, txt='Скоро новый год!', align='C', fill=True, border=1)
#
# pdf.image('skelet.gif', h=0, w=10, x=0, y=5)
#
# pdf.output('test_fpdf.pdf')


# from fpdf import FPDF
# from datetime import datetime
#
#
# pdf = FPDF('P', 'mm', 'A4')
# pdf.add_page()
#
# pdf.image('bg.jpg', h=297, w=210, x=0, y=0)
#
# pdf.add_font('comic', '', 'C:\Windows\Fonts\Comic.ttf', uni=True)
# pdf.set_font('Comic', size=35)
#
# friend_name = input('Введите имя друга: ')
#
# pdf.cell(0, 95, ln=1)
# pdf.cell(0, 20, txt='Дорогой ' + friend_name + '!', align='C', ln=1)
#
# pdf.set_font('comic', size=18)
# pdf.set_right_margin(50)
# pdf.set_left_margin(50)
#
# message = input('Введите поздравление: ')
#
# pdf.multi_cell(0, 20, txt='message', align='C')
#
# pdf.set_text_color(124, 94, 147)
#
# today = datetime.today().strftime('%d.%m.%y')
# pdf.cell(0, 20, txt=today, align='R', ln=1)
#
# author_name = input('Введите ваше имя: ')
# pdf.cell(0, 20, txt=author_name, align='R', ln=1)
#
# pdf.output('bday_card.pdf')

# summ = 0
# number = int(input('Введите число: '))
# while number != 0:
#     summ += number
#     number = int(input('Введите число: '))
# print(summ)

# password = 235
# inp_password = 0
# while inp_password != password:
#     inp_password = int(input('Введите пароль: '))
#     if inp_password == password:
#         print('Добро пожаловать!')
#     else:
#         print('Неверный пароль')


# i = 1
#
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)

# import telebot
# import random
#
# token = '5630592642:AAFdCWd4AbOmzcpS2NcYTzosbgnNa29SA4E'
#
# greetings = ['Доброго времени суток!', 'Здравствуйте!', 'Привет!', 'Рад видеть!', 'Рад встрече!', 'Приветствую!']
# bot = telebot.TeleBot(token)
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     welcome = 'Привет! Я бот для связи с Hekomata, но также могу отправить котиков <3(/cats, /steam, /discord)'
#     bot.send_message(message.from_user.id, welcome)
#
# @bot.message_handler(commands=['cats'])
# def send_cat(message):
#     cat_num = str(random.randint(1,9))
#     cat_img = open('topcats/' + cat_num + '.jpg', 'rb')
#     bot.send_message(message.from_user.id, send_cat)
#
# @bot.message_handler(content_types=['text'])
# def get_text_message(message):
#     global greetings
#     if message.text == 'Привет':
#         choisen = random.choice(greetings)
#         bot.send_message(message.from_user.id, choisen)
#     else:
#         bot.send_message(message.from_user.id, 'Я вас не понимаю!')
#
# bot.polling()

# from docx import Document
# import os
#
# user = os.getenv("USERPROFILE")
# document = Document(user + "\\Desktop")
# document = Document(user + '\\Desktop\\document.docx')

# import os
# os.mkdir("new")

# a = 5
# b = 2
# print(a / b)
# print(a // b)
# print(a ** b)
# print(a % b)

# try:
#     print()
# except ValueError:
#     print("Такого значения нет")
# else:
# stop_word = ''
# def calculation():
#     print('---------------')
#     print("Добро пожаловать в калькулятор! (Операции: +; -; *; /; **; //; %")
#     try:
#         num_1 = int(input('Введите первое число: '))
#         num_2 = int(input('Введите второе число: '))
#         operand = input('Введите необходимую операцию: ')
#     except ValueError:
#         print('Такой операции не существует')
#     else:
#         if operand == "+":
#             print('Ваш результат:', num_1 + num_2)
#         elif operand == "-":
#             print('Ваш результат:', num_1 - num_2)
#         elif operand == "/":
#             print('Ваш результат:', num_1 / num_2)
#         elif operand == "*":
#             print('Ваш результат:', num_1 * num_2)
#         elif operand == "**":
#             print('Ваш результат:', num_1 ** num_2)
#         elif operand == '%':
#             print('Ваш результат:', num_1 % num_2)
#         elif operand == '//':
#             print('Ваш результат:', num_1 // num_2)
#         else:
#             'Извините, но такой операции не существует'
#
# while stop_word != 'Нет':
#     print('---------------')
#     stop_word = input('Желаете продолжить? (Да/Нет): ')
#     calculation()


# stop_word = ''
# discriminant_value = 0
# def discriminant():
#     global discriminant_value
#     print('---------------')
#     print("")
#     try:
#         a = int(input('Введите первое число: '))
#         b = int(input('Введите второе число: '))
#         c = int(input('Введите третье число: '))
#     except ValueError:
#         print('Невозможное действие')
#     else:
#         discriminant_value = (b ** 2) - (4 * a * c)
#         print('Значение дискриминанта:', discriminant_value)
#
# while stop_word != 'Нет':
#     print('---------------')
#     stop_word = input('Желаете найти дискриминант? (Да/Нет): ')
#     discriminant()

# import math
# stop_word = ''
# find_sqrt = 0
# def sqrt():
#     global find_sqrt
#     print('---------------')
#     try:
#         a = int(input('Введите число: '))
#         find_sqrt = math.sqrt(a)
#     except ValueError:
#         print('Невозможное действие')
#     else:
#         print('Значение корня:', find_sqrt)
#
# while stop_word != 'Нет':
#     print('---------------')
#     stop_word = input('Желаете найти корень из числа? (Да/Нет): ')
#     sqrt()

# import telebot
# import random
# import requests
# from bs4 import BeautifulSoup
#
# token = '5630592642:AAFdCWd4AbOmzcpS2NcYTzosbgnNa29SA4E'
#
# greetings = ['Доброго времени суток!', 'Здравствуйте!', 'Привет!', 'Рад видеть!', 'Рад встрече!', 'Приветствую!']
# bot = telebot.TeleBot(token)
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     welcome = """
#     Привет! Я бот для связи с Hekomata, но также могу отправить котиков <3(/cats, /steam, /discord, /fact)
#     """
#     keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
#     button1 = telebot.types.KeyboardButton('Факт')
#     button2 = telebot.types.KeyboardButton('Котики')
#     keyboard.add(button1, button2)
#     bot.send_message(message.from_user.id, welcome, reply_markup=keyboard)
#
# @bot.message_handler(content_types=['text'])
# def answer(message):
#     global greetings
#     if message.text == 'Факт':
#         send_fact(message)
#     if message.text == 'Котики':
#         send_cat(message)
#     if message.text.lower() == 'привет':
#         choisen = random.choice(greetings)
#         bot.send_message(message.from_user.id, choisen)
#
# @bot.message_handler(commands=['cats'])
# def send_cat(message):
#     cat_number = str(random.randint(1,9))
#     cat_img = open('img/' + cat_number + '.jpg', 'rb')
#     bot.send_photo(message.from_user.id, cat_img)
#     # keyboard1 = telebot.types.InlineKeyboardMarkup(row_width=1)
#     # button_url = telebot.types.InlineKeyboardButton('Перейти', url='')
#     # keyboard1.add(button_url)
#     # bot.send_message(message.chat.id, 'БОльше по ссылке', reply_markup=keyboard1)
#
# @bot.message_handler(commands=['fact'])
# def send_fact(message):
#     response = requests.get('https://i-fakt.ru')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     fact = random.choice(html.findAll(class_ = 'p-2 clearfix'))
#     fact_text = fact.text
#     bot.send_photo(message.from_user.id, fact_text)
#
# @bot.message_handler(commands=['sticker'])
# def send_sticker(message):
#     bot.send_sticker(message.chat.id, '')
#
# bot.polling()

# from tkinter import *
#
# window = Tk()
# window.geometry('800x600')
#
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
#
# canvas.create_polygon(80, 100, 150, 50, 220, 100, fill='red')
# canvas.create_rectangle(100, 100, 200, 200, fill='red')
#
#
#
# window.mainloop()


# class Unit:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def sayHello(self):
#         print('Hi! My nickname is', self.name)
#
#     def kalash(self, other):
#         damage = 25
#         print(self.name, 'did RA-TA-TA-TA-TA')
#         other.health -= damage
#
#     def m4a4(self, other):
#         damage = 20
#         print(self.name, 'did TRRRRRRRRR')
#         other.health -= damage
#
#
# unit_1 = Unit('s1mple', 100)
# unit_2 = Unit('Zywoo', 88)
#
# print('Здоровье Зайву до выстрела', unit_2.health)
# unit_1.kalash(unit_2)
# print('Здоровье Зайву после выстрела', unit_2.health)
# unit_2.sayHello()
#
# print(unit_1.health

# from tkinter import *
#
# window = Tk()
#
# w = 600
# h = 600
#
# window.geometry(str(w) + 'x' + str(h))
#
# canvas = Canvas(window, width=w, height=h)
# canvas.place(in_=window, x=0, y=0)
#
# bg_photo = PhotoImage(file="bg_2.png")
# canvas.create_image(300, 300, image=bg_photo)
#
# class Knight:
#     def __init__(self):
#         self.x = 60
#         self.y = h/2
#         self.v = 0
#         self.s = 0
#         self.photo = PhotoImage(file='knight.png')
#
#     def up(self, event):
#         self.v = -3
#
#     def down(self, event):
#         self.v = 3
#
#     def stop(self, event):
#         self.v = 0
#         self.s = 0
#         print(knight.x)
#
#     def right(self, event):
#         self.s = 6
#
#     def left(self, event):
#         self.s = -6
#
# knight = Knight()
#
# def game():
#     canvas.delete('all')
#     canvas.create_image(300, 300, image=bg_photo)
#     canvas.create_image(knight.x, knight.y, image=knight.photo)
#     if knight.y <= 653 and knight.y >= -51:
#         knight.y += knight.v
#     # Вариант с перемещением
#     elif knight.y == 654:
#         knight.y = -48
#     elif knight.y == -54:
#         knight.y = 651
#     # Вариант с ограничителем
#     # elif knight.y == 654:
#     #     knight.y = 600
#     # elif knight.y == -54:
#     #     knight.y = 0
#     if knight.x <= 642 and knight.x >= -24:
#         knight.x += knight.s
#     elif knight.x == -30:
#         knight.x = 0
#     elif knight.x == 648:
#         knight.x = -18
#     window.after(5, game)
#
# game()
#
# window.bind('<Key-Up>', knight.up)
# window.bind('<Key-Down>', knight.down)
# window.bind('<Key-Right>', knight.right)
# window.bind('<Key-Left>', knight.left)
# window.bind('<KeyRelease>', knight.stop)
#
#
#
# window.mainloop()

# import requests
#
# url = 'https://swapi.dev/api/'
#
# response = requests.get(url)
#
# response = response.json()
#
# # peopleApi = response['people']
#
# # responsePeople = requests.get(peopleApi + '/1').json()
# # responsePeople = requests.get(peopleApi).json()
# #
# # print(responsePeople)
# # planetsApi = response['planets']
# # def check_people(url):
# #     for i in range(1,6):
# #         response = requests.get(url + '/' + str(i)).json()
# #         if len(response['starships']) >= 1:
# #             print(response['name'], response['starships'])
#
# def check_planets(url):
#     for i in range(1,11):
#         response = requests.get(url + '/' + str(i)).json()
#         print('Планета', response['name'], 'имеет диаметр', response['diameter'], 'условных единиц' )


# check_people(peopleApi)
# check_planets(planetsApi)

# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/'
#
# def getCourse(id, year):
#     response = requests.get(url+ str(year))
#     xml = BeautifulSoup(response.content, 'html.parser')
#     valute = xml.find('valute', {'id': id})
#     return valute.value.text
#
# year = input('Введите год: ')
# print(getCourse("R01239", year))
#
#
# # Перевод из доллара в тенге
# # 1) находим кол-во рублей: кол-во долларов * курс доллара
# # 2) Находим кол-во тенге: Кол-во рублей/курс тенге
#
# def convert(from_valute, to_valute, value):
#     rub = from_valute.course * value
#     valute = rub / to_valute.course
#     return valute
#
#
# dict = {
#     'EUR': "R01239",
#     'KZT': "R01335",
#     'USd': "R01235"
# }
#
# convert(dict['EUR'], dict['KZT'], 25)
# arr = xml.find_all('valute')
#
# print(arr[0].charcode.text)

# for i in arr:
#     print(i.charcode.text, i.value.text)

# import pyaudio
# import speech_recognition as sr
# import pyttsx3
# import webbrowser
#
# voice = pyttsx3.init()
# voice.say('Привет, я голосовой помощник Геннадий!')
# voice.runAndWait()
#
# rec = sr.Recognizer()
#
# with sr.Microphone(device_index=1) as sourse:
#     # rec.adjust_for_ambient_noise(sourse, duration=4)
#     print('Скажите что-то...')
#     audio = rec.listen(sourse)
# text = rec.recognize_google(audio, language='ru_RU').lower()
# if text == 'привет':
#     voice.say('Как ваши дела?')
#     voice.runAndWait()
# elif text == 'открой youtube':
#     voice.say('Открываю, господин')
#     voice.runAndWait()
#     webbrowser.open_new('https://www.youtube.com/')


# from tkinter import *
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
#
# url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='
#
# def getCourse(id):
#     response = requests.get(url)
#     xml = BeautifulSoup(response.content, 'html.parser')
#     valute = xml.find('valute', {'id': id})
#     return valute.value.text
#
#
# window = Tk()
# window.geometry('410x400')
# window.title('Банк Максимум')
#
# title = Label(window, text='Курс валют\nМаксимум Банк', bg='orange', font='Arial 22')
# title.place(x=165, y=40)
#
# img_logo = PhotoImage(file='logo.png')
# logo = Label(window, image=img_logo)
# logo.place(x=0, y=0)
#
# today = datetime.today()
# today = today.strftime('%d.%m.%Y')
# date_info = Label(window, text='Курс на ' + today, font='Arial 14')
# date_info.place(x=120, y=160)
#
# usd_label = Label(window, text='$' + getCourse('R01235'), font='Arial 16')
# usd_label.place(x=60, y=240)
#
# eur_label = Label(window, text='€' + getCourse('R01239'), font='Arial 16')
# eur_label.place(x=230, y=240)
#
# def converte():
#     res = int(input_value.get()) * float(getCourse('R01235').replace(',', '.'))
#     result['text'] = res
#
# input_value = Entry(window, width=10)
# input_value.place(x=30, y=315)
#
# btn = Button(text='Конвертировать!', background='#555', font='Arial 12', command=converte)
# btn.place(x=120, y=310)
#
# result = Label(window, text='Введите\nсумму', font='Arial 12')
# result.place(x=280, y=310)
#
# window.mainloop()


# value = None
# if value is None:
#     res = []
# else:
#     res = value

# value = None
# res = [] if value is None else value
# print(res)

# value = 15
# res = []
# res = value or res

# div_5_list = []
# for x in range(100):
#     if x % 5 == 0:
#         div_5_list.append(x)
# print(div_5_list)

# div_5_list = [x**3 if x > 50 else x for x in range(100) if x % 5 == 0]
# print(div_5_list)
# spisok = [x for x in range(0,250) if x % 30 == 0 or x % 31 == 0]
# print(spisok)

# any_dict = {'key': 'value'}

# words = ['red', 'blue', 'pink', 'black']
# any_dict = {x: len(x) for x in words}
# print(any_dict)

# def y(x):
#     return x**2 + 1
#
# any_list = [2454, 453463, 796, 2353, -314]
# any_dict = {x: y(x) for x in any_list}
# print(any_dict)

# div_2_list = []
# div_not2_list = []
# for i in range(10):
#     inp = int(input("Введите число: "))
#     if inp % 2 == 0:
#         div_2_list.append(inp)
#     else:
#         div_not2_list.append(inp)
# print(div_2_list)
# print(div_not2_list)

# some_tuple = (1, 2, 3, 4)
# print(some_tuple)
# some_list = list(some_tuple)
# print(some_list)
# some_list.append(15)
# print(some_list)
# some_tuple = tuple(some_list)
# print(some_tuple)


# some_dict = {(1,2,3): 'value'}
# print(some_dict)

# def func(a, b , *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)
#
# func(21, 1, bg ='orange', font='Arial')

# a = (5, 3, 2, 1, 4)
# a = tuple(sorted(list(a)))
# print(a)
# a = list(a)
# a.sort()
# a = tuple(a)

# import random
#
# class Unit:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#     def sword_attack(self, other):
#         damage = 20
#         print(self.name, 'ударил мечом', other.name)
#         other.health -= damage
#
# unit_1 = Unit('Воин маркиза', 100)
# unit_2 = Unit('Воин герцога', 100)
#
# while unit_1.health > 0 and unit_2.health > 0:
#     if random.randint(1, 2) == 1:
#         unit_1.sword_attack(unit_2)
#         print('У', unit_2.name, 'осталось', unit_2.health, 'здоровья')
#         print('')
#     else:
#         unit_2.sword_attack(unit_1)
#         print('У', unit_1.name, 'осталось', unit_1.health, 'здоровья')
#         print('')
#     if unit_1.health == 0:
#         print(unit_2.name, 'победил!')
#     elif unit_2.health == 0:
#         print(unit_1.name, 'победил!')

# import requests
#
# url = 'https://swapi.dev/api/'
# response = requests.get(url)
# response = response.json()
# starshipsAPI = response['starships']
#
# # def check_starships(starshipsAPI):
# response = requests.get(starshipsAPI).json()
# result = response['results']
# print(result)

# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/'
#
# def getCourse(id, year):
#     response = requests.get(url+ str(year))
#     xml = BeautifulSoup(response.content, 'html.parser')
#     valute = xml.find('valute', {'id': id})
#     return valute.value.text
#
# year = input('Введите год: ')
# print(getCourse("R01239", year))


# Перевод из доллара в тенге
# 1) находим кол-во рублей: кол-во долларов * курс доллара
# 2) Находим кол-во тенге: Кол-во рублей/курс тенге

# def convert(from_valute, to_valute, value):
#     rub = from_valute.course * value
#     valute = rub / to_valute.course
#     return valute
#
#
# dict = {
#     'EUR': "R01239",
#     'KZT': "R01335",
#     'USd': "R01235"
# }
#
# convert(dict['EUR'], dict['KZT'], 25)
# arr = xml.find_all('valute')
#
# print(arr[0].charcode.text)
#
# for i in arr:
#     print(i.charcode.text, i.value.text)

# from tkinter import *
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
#
# url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='
#
# def getCourse(id):
#     response = requests.get(url)
#     xml = BeautifulSoup(response.content, 'html.parser')
#     valute = xml.find('valute', {'id': id})
#     return valute.value.text
#
#
# window = Tk()
# window.geometry('410x400')
# window.resizable(height=False, width=False)
# window.title('Банкирство')
#
# title = Label(window, text='Курс валют\nЛучший Банк', bg='orange', font='Arial 22')
# title.place(x=165, y=40)
#
# img_logo = PhotoImage(file='logo.png')
# logo = Label(window, image=img_logo)
# logo.place(x=0, y=0)
#
# today = datetime.today()
# today = today.strftime('%d.%m.%Y')
# date_info = Label(window, text='Курс на ' + today, font='Arial 14')
# date_info.place(x=120, y=160)
#
# usd_label = Label(window, text='$' + getCourse('R01235'), font='Arial 16')
# usd_label.place(x=60, y=240)
#
# eur_label = Label(window, text='€' + getCourse('R01239'), font='Arial 16')
# eur_label.place(x=230, y=240)
#
# def converte():
#     res = int(input_value.get()) * float(getCourse('R01235').replace(',', '.'))
#     result['text'] = res
#
# input_value = Entry(window, width=10)
# input_value.place(x=30, y=315)
#
# btn = Button(text='Конвертировать!', background='#555', font='Arial 12', command=converte)
# btn.place(x=120, y=310)
#
# result = Label(window, text='Введите\nсумму', font='Arial 12')
# result.place(x=280, y=310)
#
# window.mainloop()

# # Полиморфизм
#
# # Динамическая типизация
#
# # def func(a):
# #     print(a)
# # func(5/'Hello'/True)
#
#
# class Animal:
#     legs = 4
#     tail = 1
#     def voice(self):
#         print('какой-то звук')
#
# class Cat(Animal):
#     def voice(self):
#         print('Мяу-мяу')
#
# class Dog(Animal):
#     def voice(self):
#         print('Гав-гав')
#
# animal = Animal()
# cat = Cat()
# dog = Dog()
#
# farm_band = [animal, cat, dog]
#
# # print(isinstance(cat, Cat))
#
# for animal in farm_band:
#     animal.voice()
# #     if isinstance(animal, Cat):
# #         animal.voice_cat()
# #     elif isinstance(animal, Dog):
# #         animal.voice_dog()
# #     else:
# #         animal.voice()
#
#
# # Статическая типизация

# # Инкапсуляция - настройка доступа
#
# class Animal:
#     _legs = 4
#     __tail = 1
#     def voice(self):
#         print('какой-то звук')
#
#     def getter(self):
#         print(self.__tail)
#
# animal = Animal()
# animal.getter()
# print(animal._Animal__tail)

# Декоратор

# def func_decorator(func):
#     def inner():
#         print('...start')
#         func()
#         print('......end')
#     return inner
#
# @func_decorator
# def some_func():
#     print('Супер важный, но базовый функционал')
#
# # some_func = func_decorator(some_func)
# some_func()

# 3 модуль

# name = 'Даниил'
# salary = 200000
# print(f'У {name} зарплата в месяц = {salary}')

# employee = {
#     'name':'Даниил',
#     'salary': 200000
# }
# print(f'У {employee["name"]} зарплата в месяц = {employee["salary"]}')

# employee_list = [
#     {
#         'name':'Даниил',
#         'salary': 200000
#     },
#     {
#         'name':'Олег',
#         'salary': 150000
#     },
#     {
#         'name':'Питон',
#         'salary': 50000
#     }
# ]
# print(employee_list[0]['name'])


# Нанимаем

# print('\n** Нанимаем сотрудника **')
# name = input('Введите имя сотрудника')
# salary = input('Введите зарплату сотрудника')
# new_employee = {
#     'name': name,
#     'salary': salary
# }
# employee_list.append(new_employee)

# for employee in employee_list:
#     print(f"У {employee['name']} зарплата в месяц = {employee['salary']}")
#
# # Увольняем
#
# print('\n** Увольняем сотрудника **')
# name = input('Введите имя сотрудника: ')
# for employee in employee_list:
#     if employee['name'] == name:
#         employee_list.remove(employee)
#
# for employee in employee_list:
#     print(f"У {employee['name']} зарплата в месяц = {employee['salary']}")

# ООП

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = False
#
#     def get_info(self):
#         return f"У {self.name} зарплата в месяц = {self.salary}"
#
#
# employee_list = [Employee('Даниил', 150000), Employee('Кирилл', 250000), Employee('Петя', 1500000)]
# Employee('Кирилл', 150000)
#
# for employee in employee_list:
#     print(employee.get_info())

# import vk_api
# import course
# import starw
#
# token = 'vk1.a.EoDkns-CYbdvwyzBmHu6EfbwpafWsM8kJulcZerCe8IWYWYratvvQmeJfRnOZCwSV4fYKIbxJVZ0IfJRtaMPhq3EO_rUi7MsQyhR7Kq6XgRmgr6Ur4H5ug4qi2ddwfW9o3w5I7noeKfXKeWp3TJsOv24vQc9ELi3wQF68eFf1F3P1vXqeCSPk0KHY16n2LyJdQgPhd2DPpvVsWR6A_Wi4w'
#
# vk = vk_api.VkApi(token=token)
#
# while True:
#     messages = vk.method("messages.getConversations", {'count': 20, 'filter': 'unanswered'})
#     if messages['count'] >= 1:
#         print(messages)
#         user_id = messages['items'][0]['last_message']['from_id']
#         message_id = messages['items'][0]['last_message']['id']
#         message_text = messages['items'][0]['last_message']['text']
#         if 'привет' in message_text.lower():
#             vk.method("messages.send", {'peer_id': user_id, 'random_id': message_id, 'message': 'Привет!'})
#         elif 'курс доллара' in message_text.lower():
#             vk.method("messages.send", {'peer_id': user_id, 'random_id': message_id, 'message': course.get_course('R01235')})
#         elif 'планета' in message_text.lower():
#             vk.method("messages.send", {'peer_id': user_id, 'random_id': message_id, 'message': starw.check_planets(url='https://swapi.dev/api/')})
#         else:
#             vk.method("messages.send", {'peer_id': user_id, 'random_id': message_id, 'message': 'Что?'})

# my_list = [x for x in range(1, 1000)]
# print(my_list)
# my_list_2 = (x for x in range(1, 1000))
# print(my_list_2)
# print(type(my_list_2))
# print(next(my_list_2))

# def lazy_func():
#     for item in range(1,11):
#         print("До", item)
#         yield item
#         print("После", item)
#
# for i in lazy_func():
#     print(i)

# f = open("test.txt", "w")
# f.write("Hello")
# f.close()
#
# with open("test.txt", "w") as f:
#     f.write("Hello")

# import contextlib
#
# @contextlib.contextmanager
# def reverse_str(you_str):
#     print("Вход в контекстный менеджер")
#     yield you_str[::-1]#переворот строки и возврат
#     print("Выход из контекстного менеджера")
#
# with reverse_str("Hello world") as r:
#     print(r)

# list = [x**2 for x in range(0,1000000)]
# list_2 = (x**2 for x in range(0, 1000000))

# @contextlib.contextmanager
# def exc_handler(exc):
#     try:
#         yield True #заморозка
#     except exc:
#         print("Произошло исключение")
#
# with exc_handler(IndexError):
#     my_list = [1,2]
#     print(my_list[3])

# class Year:
#     def __init__(self):
#         self.days = 365
#
#     @property
#     def days(self):
#         return self.__days
#
#     @days.setter
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception('Некорректное значение!!')
#
#
# year1 = Year()



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age >= 0:
#             self.__age = age
#         else:
#             raise Exception('Вы ещё не родились')
#
#
# person = Person('Иван', 25)


# goods = [
#     {
#         'name': 'Iphone 14',
#         'brand': 'Apple',
#         'price': 1200
#     },
#     {
#         'name': 'Samsung Galaxy A23',
#         'brand': 'Samsung',
#         'price': 600
#     },
#     {
#         'name': 'Xiaomi Mi13 Ultra',
#         'brand': 'Xiaomi',
#         'price': 800
#     },
#     {
#         'name': 'Iphone 11',
#         'brand': 'Apple',
#         'price': 400
#     }
# ]

# apple_list = filter(lambda item: item['brand'] == 'Apple' ,goods)
# print(list(apple_list))
# print(sorted(goods, key=lambda item: item['price']))

# a = ['1', '2', '3', '4']
# # b = map(int, a)
#
# def ussr(item):
#     return item + 'ussr'
# print(list(map(ussr, a)))

# a = ['1', '2', '3', '4']

# for index, item in enumerate(goods):
#     print(index, item)

# names = ['А', 'Б', 'B', 'Г']
# numb = ['1', '2', '3', '4']
# for name, num in zip(names, numb):
#     print(name, num)

# s = 'aaabca'
# a: 4, b: 1, c: 1

# s = 'aaabca'
# for sym in s:
    # count = 0
    # for sub_sym in s:
    #     if sub_sym == sym:
    #         count += 1
    # print(sym, count)
# s = 'aaabca'
# for sym in s:
#     print(sym, s.count(sym))
# O(N) = N**2

# s = 'aaabca'
# for sym in set(s):
#     count = 0
#     for sub_sym in s:
#         if sub_sym == sym:
#             count += 1
#     print(sym, count)
# O(N) = M(Уникальные символы) * N = N ** 2

# s = 'aaabca'
# syms_counter = {}
# for sym in s:
#     syms_counter[sym] = syms_counter.get(sym, 0) + 1
# print(syms_counter)
# O(N) =
