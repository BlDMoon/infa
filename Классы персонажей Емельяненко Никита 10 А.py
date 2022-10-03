class Player:
    def __init__(self):
        self.belonging = ""
        self.name = ""
        self.height = 180
        self.weight = 70
        self.haircolor = ""
        self.lvl = 1
        self.damage = 50
        self.armor =20
        self.strength = 10
        self.magic = 10
        self.dexterity = 10
        self.vitality = 10
        self.hp = 70
        self.manna = 10

Player1 = Player()
Player1.belonging = "Warrior"
Player1.name = "kolbas"
Player1.height = 198
Player1.weight = 87
Player1.haircolor = "Black"
Player1.lvl = 28
Player1.damage = 154
Player1.armor = 246
Player1.strength = 87
Player1.magic = 23
Player1.dexterity = 40
Player1.vitality = 90
Player1.hp = 320
Player1.manna = 100

class Undead:
    def __init__(self):
        self.belonging =""
        self.name = ""
        self.height = 178
        self.weight = 63
        self.lvl = 1
        self.damage = 34
        self.armor = 5
        self.strength = 43
        self.magic = 10
        self.dexterity = 20
        self.vitality = 15
        self.hp = 53
        self.manna = 10

skeleton = Undead()
skeleton.belonging = "Standard skelet"
skeleton.name = "Garry"
skeleton.height = 176
skeleton.weight = 77
skeleton.lvl = 22
skeleton.damage = 144
skeleton.armor = 38
skeleton.strength = 121
skeleton.magic = 0
skeleton.dexterity = 12
skeleton.vitality = 42
skeleton.hp = 220
skeleton.manna = 0

class Treasure:
    def __init__(self):
        self.belonging = ""
        self.name = ""
        self.gold = 190
        self.xp = 100

chest = Treasure()
chest.belonging = "Standard treasure"
chest.name = "Classic Chest"
chest.gold = 400
chest.xp = 320

print(Player1.belonging)
print(Player1.name)
print(Player1.height)
print(Player1.weight)
print(Player1.haircolor)
print(Player1.lvl)
print(Player1.damage)
print(Player1.armor)
print(Player1.strength)
print(Player1.magic)
print(Player1.dexterity)
print(Player1.vitality)
print(Player1.hp)
print(Player1.manna)

print(skeleton.belonging)
print(skeleton.name)
print(skeleton.height)
print(skeleton.weight)
print(skeleton.lvl)
print(skeleton.damage)
print(skeleton.armor)
print(skeleton.strength)
print(skeleton.magic)
print(skeleton.dexterity)
print(skeleton.vitality)
print(skeleton.hp)
print(skeleton.manna)

print(chest.belonging)
print(chest.name)
print(chest.gold)
print(chest.xp)
