#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        return print(f"Total arguments: {len(sys.argv)}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    i = 1
    while i < len(sys.argv):
        print(f"Arguments {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {len(sys.argv)}")
    return


if __name__ == "__main__":
    main()
