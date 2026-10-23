#! /usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError("%d°C is too cold for plants (min 0°C)" % temp)
    if temp > 40:
        raise ValueError("%d°C is too hot for plants (max 40°C)" % temp)
    return temp


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

    print("\nInput data is '100'")
    try:
        temp = "100"
        print("Temperature is now %d°C" % input_temperature(temp))
    except ValueError as e:
        print("Caught input_temperature error:", e)

    print("\nInput data is '-50'")
    try:
        temp = "-50"
        print("Temperature is now %d°C" % input_temperature(temp))
    except ValueError as e:
        print("Caught input_temperature error:", e)

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
