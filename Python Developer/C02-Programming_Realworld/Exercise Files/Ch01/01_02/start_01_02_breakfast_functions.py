""" A Functional Breakfast """

def mix_cook():
    print('Mixing the ingredients')
    print('Greese the pane')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')


def make_omelette():
    mix_cook()
    omelette = 'a tasty omelette'
    return omelette

def make_pancake():
    mix_cook()
    pancake = 'a delicious pancake'
    return pancake

omelette = make_omelette()
pancake = make_pancake()

print("Today's Breakfast is: " + omelette + " & " + pancake)
print(make_omelette())
print(make_pancake())

