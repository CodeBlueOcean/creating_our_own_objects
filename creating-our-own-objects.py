#OOP
from typing import AsyncGenerator


class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')

player1 = PlayerCharacter('Cindy')
player2 = PlayerCharacter('Tom')

print(player1.name)
print(player2.name)

#OOP
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age
    def run(self):
        print('run')

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1.age)
print(player2.age)

#OOP
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1.run())
print(player2.age)

#OOP
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age
        
    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1)
print(player2.attack)


