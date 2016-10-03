from inspect import isfunction
from datetime import datetime

def logger_decorator(func):
    def log(*args, **kwargs):
        print(func.__name__, datetime.now(), args)
        return func(*args, **kwargs)

    return log

class Logger(type):
    def __init__(self, namespece, bases, attributes):
        for key in attributes:
            func = attributes[key]

            if isfunction(func):
                print(func.__name__, datetime.now())

class People(metaclass=Logger):
    def speak(self, message):
        print(message)

    def run(self):
        print('vrrrrrum!')

person = People()
person.speak('hello world!')
person.run()

