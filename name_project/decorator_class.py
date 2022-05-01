def adv_deco(my_class):
    def inner(*args, **kwargs):
        print("Start!")
        return my_class(*args, **kwargs)
    return inner


@adv_deco
class MyClass():
    pass