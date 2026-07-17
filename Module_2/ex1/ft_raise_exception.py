def input_temperature(temp_str):
    try:
        temp = int(temp_str)
        if (temp < 0):
            raise ValueError(f"{temp} is too cold for plants (min 0°C)")
        elif (temp > 40):
            raise ValueError(f"{temp} is too hot for plants (max 40°C)")
        return temp
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return None

def test_temperature():
    test_cases = ["25", "abc", "-10", "50", ""]
    for case in test_cases:
        result = input_temperature(case)
        if result is not None:
            print(f"Input data is {case}")
            print(f"Temperature is now {result}°C")

def main():
    test_temperature()
    print("All tests completed - program didn't crash!")



if __name__ == "__main__":
    main()