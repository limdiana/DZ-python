"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""

def exam(students):
    ocenka = {}
    for i in range(1, students + 1):
        mark = int(input("Введите полученную оценку студента " + f'{i}' + ': '))
        ocenka[i] = mark


    for a in ocenka.keys():
        if ocenka.get(a) >= 50:
            print("Студент номер", a, ', вы сдали экзамен')
        else:
            print("Студент номер", a, ", вы отчислены")
exam(2)