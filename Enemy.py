class Enemy:

    def __init__(self, damage, health, positioning):
        self.damage = damage
        self.health = health
        self.positioning = positioning

    def giveDict(self):
        return {
            "damage": self.damage,
            "health": self.health,
            "positioning": self.positioning
        }