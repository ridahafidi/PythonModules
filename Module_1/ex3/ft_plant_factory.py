class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
 
    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, growth):
        self.height += growth

    def agin(self, days):
        self.age += days


def create_plant(name, height, age):
    P = Plant(name, height, age)
    print("Created: ", end="")
    P.show()
    return P



def main():
    print("=== Plant Factory Output ===")
    rose = create_plant("Rose", 25.0, 30)
    Oak = create_plant("Oak", 200.0, 365)
    Cactus = create_plant("Cactus", 5.0, 90)
    Sunflower = create_plant("Sunflower", 80.0, 45)
    Fern = create_plant("Fern", 15.0, 120)

if __name__ == "__main__":
    main()