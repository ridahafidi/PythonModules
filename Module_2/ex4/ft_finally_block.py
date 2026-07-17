class GardenError(Exception):
    """Unknown garden error."""
    pass

class PlantError(GardenError):
    """Unknown plant error."""
    pass

class WaterError(GardenError):
    """Unknown water error."""
    pass

def water_plant(plant_name):
    if plant_name.capitalize() != plant_name:
        raise PlantError(f"Invalid plant name to water: {plant_name}")
    else:
        print(f"Watering {plant_name}: [OK]")

def watering_system():
    print("Testing valid plants...")
    plants = ["Tomato", "Lettuce", "Carrots"]
    for plant in plants:
        water_plant(plant)

def watering_system_with_error():
    print("Testing invalid plants...")
    plants = ["tomato", "lettuce", "carrots"]
    for plant in plants:
        water_plant(plant)

def watering():
    try:
        print("opening watering system")
        watering_system()
        print("Closing watering system", end="\n\n")
        #==============================================#
        print("opening watering system")
        watering_system_with_error()
        print("Closing watering system", end="\n\n")
    except PlantError as pe:
        print(f"Caught PlantError: {pe}")
        print(".. ending tests and returning to main")
        print("Closing watering system")
    finally:
        print("Cleanup always happens, even with errors!")


def main():
    print("=== Garden Watering System ===", end="\n\n")
    watering()

if __name__ == "__main__":
    main()