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
