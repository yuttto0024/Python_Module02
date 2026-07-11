#!usr/binenv python3

class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The Tomato plant is wilting!")
    except GardenError as e:
        print("--- Test1 ---")
        print(f"Caught {e.__class__.__name__}: {e}\n")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print("--- test 2 ---")
        print(f"Caught {e.__class__.__name__}: {e}\n")

    try:
        raise GardenError("The tomato plant is wilting!")
    except GardenError as e:
        print("--- test 3 ---")
        print(f"Caught {e.__class__.__name__}: {e}\n")

    try:
        raise GardenError("Not enough water in the tank!")
    except GardenError as e:
        print("--- test 4 ---")
        print(f"Caught {e.__class__.__name__}: {e}\n")


if __name__ == "__main__":
    test_custom_errors()
