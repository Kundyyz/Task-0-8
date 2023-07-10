# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод: Парам пам-пам


def rhythm(glasnye_bukvy, stikh):
    list1 = []
    for i in stikh:
        count = 0
        for j in i:
            if j in glasnye_bukvy:
                count += 1
        list1.append(count)
    print(list1)
    return(len(set(list1)))<2
    

stikh = input('Vvedite tekst stikha: ').lower().split()
print(stikh)
glasnye_bukvy = 'ыуаеоэиюя'
if rhythm(glasnye_bukvy, stikh):
    print('Парам пам-пам')
else:
    print('Пам парам')


