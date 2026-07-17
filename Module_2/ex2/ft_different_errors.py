


def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("non/existent/file", "r")
    elif operation_number == 3:
        "" + 5
    else:
        print("Operation completed successfully", end="\n\n")
        return "Success"


def test_error_types(i):
    try:
        garden_operations(i)
    except ValueError as ve:
        print(f"Caught ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"Caught ZeroDivisionError: {zde}")
    except FileNotFoundError as fnfe:
        print(f"Caught FileNotFoundError: {fnfe}")
    except TypeError as te:
        print(f"Caught TypeError: {te}")
    except Exception as e:
        print(f"Caught unexpected exception: {e}")


def main():
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}")
        test_error_types(i)
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()