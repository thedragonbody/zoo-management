class Animal():
    zoo_name = 'safari'
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species 
        self.age = age
        self.sound = sound
        
    def make_sound(self):
        print (f'sound: {self.sound}')

    def info(self):
        print (f'name: {self.name}, species: {self.species}, age: {self.age}, sound: {self.sound}')
    
lion = Animal ('lion', 'mammal', 10, 'wow!')
lion.info()
lion.make_sound()

class bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        self.name = name
        self.species = species 
        self.age = age
        self.sound = sound
        self.wing_span = wing_span

    def make_sound(self):
        print (f'sound: {self.sound}')

    def info(self):
        print (f'name: {self.name}, species: {self.species}, age: {self.age}, sound: {self.sound} wing span: {self.wing_span}')

bird = bird('bird', 'pigeon', 3, 'jic! jic!', 10)
bird.info()
bird.make_sound()