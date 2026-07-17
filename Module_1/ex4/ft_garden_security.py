class Plant:
    
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age


    def get_height(self):
        return self.__height
    def get_age(self):
        return self.__age
    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, Height cannot be negative.")
            print("Height update rejected")
        else:
            self.__height = height
    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, Age cannot be negative.")
            print("Age update rejected")
        else:
            self.__age = age
    def show(self):
        print(f"{self.name}: {self.__height}cm, {self.__age} days old")

    def grow(self, growth):
        self.__height += growth

    def agin(self, days):
        self.__age += days

def create_plant(name, height, age):
    P = Plant(name, height, age)
    print("Created: ", end="")
    P.show()
    return P


def main():
    print("=== Garden Security System ===")
    plant1 = create_plant("Rose", 15.0, 10)
    plant1.set_height(25.0)
    print(f"Height updated: {plant1.get_height()}cm")
    plant1.set_age(30)
    print(f"Age updated: {plant1.get_age()} days")
    plant1.set_height(-5.0)
    plant1.set_age(-10)
    print("Current state: ", end="")
    plant1.show()

if __name__ == "__main__":
    main()
