def decorate(eat):
    def wrapper():
        print("Возьмите хлебную булочку.")
        eat()
        print("Добавте соус на Ваш вкус.")
        print("Накройте все хлебушком.")
    return wrapper
@decorate
def eat_to_decor():
    print("Для разнообразия предлагаю добавить Вам: ананас и салат!")

eat_to_decor()