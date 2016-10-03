from functools import wraps

def my_first_decorator(fn):
    @wraps(fn)
    def wrap():
       return '<p>%s</p>' % fn()
    return wrap

@my_first_decorator
def get_name():
    """ Returns my name """
    return 'Evandro'

print(get_name())
print(get_name.__name__)
print(get_name.__doc__)
print(get_name.__module__)
