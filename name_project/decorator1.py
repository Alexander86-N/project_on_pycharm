"""Прокидываем параметры в декоратор."""


def passing_parameters(*dargs, **dkwargs):
    def wrapper(func):
        def inner(*args, **kwargs):
            print(*dargs, **dkwargs)
            return func(*args, **kwargs)
        return inner
    return wrapper


@passing_parameters("Started!")
def summa(num1, num2):
    return num1 + num2


print(summa(2, 8))
