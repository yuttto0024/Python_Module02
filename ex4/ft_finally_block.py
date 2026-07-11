#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:

    print("--- Test 1 ---")
    print("Testing valid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")

    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print("... ending tests and returning to main")
        return

    finally:
        print("Closing watering system\n")

    print("--- Test 2 ---")
    print("Testing invalid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")
        water_plant("lettuce")

    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print("... ending tests and returning to main")
        return

    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
