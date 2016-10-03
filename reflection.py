class MyClass(object):
    def method(self):
        return 'my method!'

obj = globals()['MyClass']()
getattr(obj, 'method')
