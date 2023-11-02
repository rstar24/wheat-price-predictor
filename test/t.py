x = "yay!" if 1 >= 1 else "nay!"
print(x)


class Myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello {self.name} you are {self.age} years old now")

obj = Myclass("Rishabh",22)

obj.greet()

