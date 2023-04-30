


def decorator(func):
    def wrapper():
        print("Что-то до исполнения функции")# До исполнения функции
        func()
        print("Что-то после исполнения функции")# После исполнения функции
    return wrapper

@decorator
def say_hello():
    print("Hey, how is it going?")

say_hello()