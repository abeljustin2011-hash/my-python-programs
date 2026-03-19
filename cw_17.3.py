class Minion:
  
    def __init__(self, name, height, eyes, epitome):
        self.name = name
        self.height = height
        self.eyes = eyes
        self.epitome = epitome

    def display_info(self):
        print("I am:", self.name)
        print("My height is :", self.height)
        print("I have ", self.eyes, " eyes")
        print("I am:", self.epitome)

Bob = Minion("Bob", 1.2, 2, "the Main Charactar")
Carl = Minion("Carl", 1.5, 1, "Tall")

Bob.display_info()
Carl.display_info()