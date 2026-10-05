class Creature:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
    def health_below_50(self):
        return self.hp<=50
    def health_below_100(self):
        return self.hp<=100
    def boss(self):
        return self.hp>=500 and self.damage>=50

    

creatures = {
    1: Creature("Ant", 10, 2),
    2: Creature("Caterpillar", 20, 3),
    3: Creature("Rat", 30, 5),
    4: Creature("Spider", 40, 7),
    5: Creature("Wolf", 50, 10),
    6: Creature("Goblin", 100, 20),
    7: Creature("Zombie", 150, 20),
    8: Creature("Skeleton", 200, 25),
    9: Creature("Orc", 250, 30),
    10: Creature("Troll", 300, 35),
    11: Creature("Dark Knight", 350, 40),
    12: Creature("Ogre", 400, 45),
    13: Creature("Demon", 500, 50),
    14: Creature("Mega Boss", 1000, 99)
}