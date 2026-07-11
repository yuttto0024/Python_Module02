#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}℃ is too hot for plants (max 40℃)")

    if temp < 0:
        raise ValueError(f"{temp}℃ is too cold for plants (min 0℃)")
    return temp


def test_temperature() -> None:
    print("--- Test 1 ---")
    print("Input: '25'")
    temp = input_temperature("25")
    print(f"Temperature is now {temp}℃\n")

    print("--- Test 2---")
    print("Input: 'abc'")
    try:
        temp = input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("--- Test 3---")
    print("Input: '100'")
    try:
        temp = input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("--- Test 4---")
    print("Input: '-50'")
    try:
        temp = input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
