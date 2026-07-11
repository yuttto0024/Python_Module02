#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("--- Test 1 ---")
    print("Input: '25'")
    temp = input_temperature("25")
    print(f"Temperature is now {temp}℃\n")

    print("--- Test 2 ---")
    print("Input: 'abc'")
    try:
        temp = input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
