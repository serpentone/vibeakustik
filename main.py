from random import randint
import csv

class Room:
    def __init__(self):
        self.size = int()
        self.chest = False
        self.enemyCount = int()
        self.doorCount = int()
        self.enemyDict = {}

    def setRoom(self):
        self.size = randint(1,4)
        self.enemyCount = randint(1,3)
        self.doorCount = randint(1,2)
        chestRoll = randint(1,2)
        if chestRoll == 1:
            self.chest = True
        else:
            self.chest = False
    
    def setEnemyArr(self):
        enemy = Enemy()
        self.enemyDict.update[enemy]

class Enemy:
    def __init__(self, prefix, suffix):
        self.name = prefix + " of the " + suffix
        self.prefix = prefix
        self.suffix = suffix
        self.health = int()
        self.damage = int()

    def setEnemy(self):
        pass

room = Room()
room.setRoom()
print(room.size, room.chest, room.enemyCount, room.doorCount)
enemy = Enemy("Warrior", "North")
print(enemy.name)
