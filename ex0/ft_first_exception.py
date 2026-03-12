from typing import Optional


def check_temperature(temp_str: str) -> Optional[int]:
    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Error: Invalid input. '{temp_str}' is not a valid integer.")
        return None

    if 0 <= temp_int <= 40:
        return temp_int
    else:
        print(f"Warning: Temperature {temp_int}"
              "is out of the acceptable range (0-40).")
        return None


if __name__ == "__main__":
    test_cases = ["25", "25.5", "hot", "50", "-5"]

    for val in test_cases:
        print(f"--- Test Input: {val} ---")
        result = check_temperature(val)
        print(f"Return: {result}\n")
