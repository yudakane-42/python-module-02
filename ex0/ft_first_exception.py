#! /usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    print("\nInput data is '25'")
    try:
        temp = "25"
        print("Temperature is now %d°C" % input_temperature(temp))
    except ValueError as e:
        print("Caught input_temperature error:", e)

    print("\nInput data is 'abc'")
    try:
        temp = "abc"
        print("Temperature is now %d°C" % input_temperature(temp))
    except ValueError as e:
        print("Caught input_temperature error:", e)

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
