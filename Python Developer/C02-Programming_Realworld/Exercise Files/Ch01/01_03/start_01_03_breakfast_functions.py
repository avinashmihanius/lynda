""" A Functional Breakfast """

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')    

def make_omelette(ingredient):
    mix_and_cook()
    omelette = 'a {} omelette'.format(ingredient)
    return omelette

def make_pancake():
    mix_and_cook()
    pancake = 'a delicious pancake'
    return pancake

def fancy_omelette(*ingredients): #astrieks shows ingredients tuple
    mix_and_cook()
    omelette = 'an omelette with {} ingredients'.format(len(ingredients))
    return omelette

print(fancy_omelette('onion','tomatoes','jalapenos','olives'))
print(make_omelette('tomato'))