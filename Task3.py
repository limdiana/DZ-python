"""
На летней универсиаде будет проводиться по два забега. Чтобы соревнования были честными,
участники должны распределяться между забегами случайным образом.
Напишите программу, печатающую случайные номера забегов (1 или 2) до тех пор, пока не будет введено «off».
После генерации каждого номера должно печататься:
1) «Ваш номер: _».
2) «Участников в первом забеге: _», «Участников во втором забеге: _».
"""
from random import*

a = input()
while True:
    if a == 'off':
        break
    else:
        print('Ваш номер: ', randint(1, 2))
        print('Участников в первом забеге:', randint(2, 50), ',', 'участников во втором забеге:', randint(2, 50))
        a = input()