#! /usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        a = 100 / 0
        print(a)
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        a = "abc" + 123
        print(a)


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    operation_number = 0
    while operation_number < 5:
        try:
            print("Testing operation %d..." % operation_number)
            garden_operations(operation_number)
            print("Operation completed successfully")
        except Exception as e:
            print("Caught %s: %s" % (type(e).__name__, e))
        operation_number += 1
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
