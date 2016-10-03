class a:
    def __init__(self, data):
        self.data = data
 
    def getd3(self):
        return self.data * 3
 
 
class MyMeta(type):
    def __new__(metaname, classname, baseclasses, attrs):
        print('New called with')
        print('metaname', metaname)
        print('classname', classname)
        print('baseclasses', baseclasses)
        print('attrs', attrs)
        attrs['getdata'] = a.__dict__['getd3']
        # attrs['getdata'] = a.getd3
        return type.__new__(metaname, classname, baseclasses, attrs)
 
    def __init__(classobject, classname, baseclasses, attrs):
        print('init called with')
        print('classobject', classobject)
        print('classname', classname)
        print('baseclasses', baseclasses)
        print('attrs', attrs)
 
 
class Kls(metaclass=MyMeta):
    def __init__(self,data):
        self.data = data
 
    def printd(self):
        print(self.data)
 
ik = Kls('arun')
ik.printd()
print(ik.getdata())
