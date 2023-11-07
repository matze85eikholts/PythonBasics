class Person:

    # -constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("The body was created")

    def sing(self):
        print(self.name + " sings well")

    def dance(self):
        print(self.name + " dances also well!!!")
