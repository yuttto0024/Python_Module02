#!/usr/bin/env python3

def garden_operation(operation_number: int) -> None:

    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("non/existent/file")
    elif operation_number == 3:
        "Happy" + 42
    else:
        return


def test_error_type() -> None:

    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operation(i)
            print("Operation completed successfully\n")

        except ValueError as e:
            print("--- Test 1 ---")
            print(f"Caught ValueError: {e}\n")
        except ZeroDivisionError as e:
            print("--- Test 2 ---")
            print(f"Caught ZeroDivisionError: {e}\n")
        except FileNotFoundError as e:
            print("--- Test 3 ---")
            print(f"Caught FileNotFoundError: {e}\n")
        except TypeError as e:
            print(f"Caught TypeError: {e}\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_type()
