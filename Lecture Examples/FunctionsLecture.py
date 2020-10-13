dog_name = 'Kitty'
dog_weight = 45
if dog_weight > 20:
    print(dog_name, 'says WOOF WOOF')
else:
    print(dog_name, 'says woof woof')

dog_name = 'Sparky'
dog_weight = 15
if dog_weight > 20:
    print(dog_name, 'says WOOF WOOF')
else:
    print(dog_name, 'says woof woof')

dog_name = 'Jackson'
dog_weight = 12
if dog_weight > 20:
    print(dog_name, 'says WOOF WOOF')
else:
    print(dog_name, 'says woof woof')

dog_name = 'Ranger'
dog_weight = 65
if dog_weight > 20:
    print(dog_name, 'says WOOF WOOF')
else:
    print(dog_name, 'says woof woof')




def bark(name, weight):
    if weight > 20:
        print(name, 'says WOOF WOOF')
    else:
        print(name, 'says woof woof')

bark('Kitty', 45)
bark('Sparky', 15)
bark('Jackson', 12)
bark('Ranger', 65)

greeting = 'Greetings'

def greet(name, message):
    print(greeting, name + '.', message)

greet('June', 'See you soon!')


greeting = 'Greetings'

def greet(name, message):
    greeting = 'Hi'
    print(greeting, name + '.', message)

greet('June', 'See you soon!')
print(greeting)

greeting = 'Greetings'

def greet(name, message):
    global greeting
    greeting = 'Hi'
    print(greeting, name + '.', message)

greet('June', 'See you soon!')
print(greeting)

def get_bark(weight):
    if weight > 20:
        return 'WOOF WOOF'
    else:
        return 'woof woof'

def get_bark(weight):
    if weight > 20:
        return 'WOOF WOOF'
    return 'woof woof'

def greet(name, message='You rule!'):
    print('Hi', name + '.', message)

greet('John') # Hi John. You rule!
greet('Jennifer', 'How are you today?') # Hi Jennifer, How are you today?


#def greet(message='You rule!', name):
#    print('Hi', name + '.', message)

greet('John', 'Howdy partner!')
greet(message='Howdy partner!', name = 'John')