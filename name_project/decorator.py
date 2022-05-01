def wrapper(func):
    def inner(*args, **kwargs):
        print("Запуск функциию!")
        return func(*args, **kwargs)
    print("Окончание!")
    return inner


def summa(number1, number2):
    return number1 + number2


summa = wrapper(summa)
print(summa(3, 5))