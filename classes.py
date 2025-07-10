class Human:
    # shared attributes are the same for all instance of the class
    species = 'Homo sapiens'

    # constructor method; while the constructor method takes in the class attribute(unique to each class)
    def __init__(self, gender, race):
        self.gender = gender
        self.race = race
        # init a new user object


    def birth(self):
        print('a new life begins')
        # do something

    def eat(self):
        print('consumes food...')
    
    def sleep(self):
        print('get rest...')

    def death(self):
        print('the end of life')

#  inheritance

class Female(Human):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def be_annoying(self):
        print('initiating nagging protocol...3 2 1')

class Male(Human):
    pass # pass helps us define empty class