#!/usr/bin/env python3
def garden_operations():
    print("Testing ValueError...")
    try:
        int("ciao")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        return 19 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError...")
    fd = 0
    try:
        fd = open("zuppa.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'zuppa.txt'\n")
    finally:
        if fd:
            fd.close()
    print("Testing KeyError...")
    try:
        name = {"Bob": 10, "Roberto": 22}
        print(f"{name['Piero']}")
    except KeyError:
        print("Caught KeyError: missing 'Piero' in dictionary\n")


def test_error_types():
    fd = 0
    try:
        int("ciao")
        fd /= 0
        fd = open("zuppa.txt")
        name = {"Bob": 10, "Roberto": 22}
        print(f"{name['Piero']}")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    finally:
        if fd:
            fd.close()


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("Testing multiple errors together...")
    test_error_types()
    print("All error types tested successfully!\n")
