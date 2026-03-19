
class Pokemon:

    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, opponent):
        damage = 10
        opponent.health -= damage
        print(self.name, "attacks", opponent.name)
        print(opponent.name, "loses", damage, "health")
        print(opponent.name, "health is now", opponent.health)

    def dodge(self, chance):

        if chance % 2 == 0:
            print(self.name, "dodged the attack!")
            return True
        else:
            print(self.name, "failed to dodge.")
            return False

    def evolve(self):
        if self.name == "Pikachu":
            self.name = "Raichu"
            self.health += 30
            print("Pokemon evolved into", self.name)
        if self.name == "Raichu":
            self.name = "Ashchu"
            self.health += 50
            print("Pokemon evolved into", self.name)


pikachu = Pokemon("Pikachu", "Electric", 70)
charmander = Pokemon("Charmander", "Fire", 60)

pikachu.attack(charmander)

pikachu.dodge(2)

pikachu.evolve()

pikachu.evolve()