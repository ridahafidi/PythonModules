class GardenError(Exception):
    """Unknown garden error."""
    pass

class PlantError(GardenError):
    """Unknown plant error."""
    pass

class WaterError(GardenError):
    """Unknown water error."""
    pass


def test_custom_errors(i):
    if i == 0:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting")
    elif i == 1:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank")
    elif i == 2:
        print("Testing catching all garden errors...")
        raise GardenError("The tomato plant is wilting")
    elif i == 3:
        raise GardenError("Not enough water in the tank")

def try_all_custom_errors(i):
    try:
        test_custom_errors(i)
    except PlantError as pe:
        print(f"Caught PlantError: {pe}")
    except WaterError as we:
        print(f"Caught WaterError: {we}")
    except GardenError as ge:
        print(f"Caught GardenError: {ge}")
    except Exception as e:
        print(f"Caught unexpected exception: {e}")

def main():
    print("=== Custom Garden Errors Demo ===")
    for i in range(4):
        try_all_custom_errors(i)
    print("All custom error types work correctly!")

if __name__ == "__main__":
    main()