#!/usr/bin/env python3
import sys
import site


if __name__ == "__main__":

    print()

    # Check if running in global environment (no venv active)
    if (sys.prefix == sys.base_prefix):

        print("MATRIX STATUS: You're still plugged in")

        print()

        # Show Python path and version
        print("Current Python: "
              f"{sys.executable}{sys.version.split(' ')[0][1:]}")
        print("Virtual Environment: None detected")

        print()

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print()

        # Instructions to create and activate venv
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate     # On Windows")

        print()

        print("Then run this program again.")

    else:
        # Virtual environment is active

        print("MATRIX STATUS: Welcome to the construct")

        print()

        # Display venv info
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {sys.prefix.split('/')[-1]}")
        print(f"Environment Path: {sys.prefix}")

        print()

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        print()

        # Show where packages will be installed
        print("Package installation path:")
        print(f"{site.getsitepackages()[0]}")
