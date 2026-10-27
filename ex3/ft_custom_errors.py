#! /usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise_plant_error()
    except PlantError as e:
        print("Caught PlantError: %s" % e)

    print("\nTesting WaterError...")
    try:
        raise_water_error()
    except WaterError as e:
        print("Caught WaterError: %s" % e)

    print("\nTesting catching all garden errors...")
    try:
        raise_plant_error()
    except GardenError as e:
        print("Caught GardenError: %s" % e)
    try:
        raise_water_error()
    except GardenError as e:
        print("Caught GardenError: %s" % e)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
