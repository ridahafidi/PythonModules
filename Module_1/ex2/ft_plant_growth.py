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


def main():
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    old_height = rose.height
    for day in range(0, 7):
        rose.grow(0.5)
        rose.agin(1)
        print(f"=== Day {day + 1} ===")
        rose.show()
    print(f"Growth this week: {rose.height - old_height}cm")


if __name__ == "__main__":
    main()