def howdy(self, you):
    print('Howdy ' + you)

MyList = type('MyList', (list,), dict(x=42, howdy=howdy))

ml = MyList()
ml.append('Camembert')
print(ml)
print(ml.x)
ml.howdy('John')

print(ml.__class__.__class__)
