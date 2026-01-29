#!/usr/bin/env python3
import math
import sys


def main() -> None:
    origin: tuple = (0, 0, 0)
    x0, y0, z0 = origin
    try:
        full_input: str = ''
        for arg in sys.argv[1:]:
            full_input = full_input + ' ' + arg
        coords: str = full_input.split('), (')
        for arg in coords:
            parts: str = arg.split('(')[-1].split(')')[0]
            coord: tuple = tuple(int(x) for x in parts.split(','))
            print(f"Parsing coordinates: {coord}")
            # Unpacking demonstration
            x1, y1, z1 = coord
            print(f"Distance between {origin} and {coord}: "
                  f"{math.sqrt((x1-x0)**2 + (y1-y0)**2 + (z1-z0)**2):.2f}")
            print()
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error detail - Type: ValueError, Args: {e.args}")


if __name__ == "__main__":
    print("\n=== Game Coordinate System ===\n")
    main()
    print()
