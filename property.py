class Person:
    name = property()

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')

        self._name = value

evandro = Person()
evandro.name = 'Evandro'
print(evandro.name)
