class Player:

    def __init__(self, damage, health, spells):
        self.damage = damage
        self.health = health
        self.spells = spells
        self.inventory = []

    def castSpellByIndex(self, spellNum):
        return self.spells[spellNum - 1]

    def giveDict(self):
        return {
            "damage": self.damage,
            "health": self.health,
            "spells": self.spells,
            "inventory": self.inventory
        }
    
    def printInventory(self):
        count = 1
        print("[Item Number] Name Count")
        for i in self.inventory:
            print("[" + str(count) + "] " + i[0] + " " + str(i[1]))
            count = count + 1
        return count

    def usePotion(self):
        self.health = 10
        for i in self.inventory:
            if i[0] == "Potion":
                i[1] = i[1] - 1