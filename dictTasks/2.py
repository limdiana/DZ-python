"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""
numbers = "0139412831055230677798"

num = {}
for key in numbers:
    if key not in num.keys():
        num[key] = 1
    else:
        num[key] += 1
print(num)