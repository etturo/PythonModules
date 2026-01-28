#!/usr/bin/env python3
import math


def main():
    origin = (0, 0, 0)
    coord_1 = (10, 20, 5)
    print(f"Position created: {coord_1}")
    x1, y1, z1 = coord_1
    x0, y0, z0 = origin
    distance = math.sqrt((x1-x0)**2 + (y1-y0)**2 + (z1-z0)**2)
    print(f"Distance between {origin} and {coord_1}: {distance:.2f}")
    print()
    try:
        # Parsing valid coordinated
        str_coord_2 = "3,4,0"
        coord_2 = tuple(int(x) for x in str_coord_2.split(','))
        print(f"Parsing valid coordinates: \"{str_coord_2}\"")
        print(f"Parsed position: {coord_2}")
        x2, y2, z2 = coord_2
        distance = math.sqrt((x2-x0)**2 + (y2-y0)**2 + (z2-z0)**2)
        print(f"Distance between {origin} and {coord_2}: {distance:.2f}")
        print()
        # Parsing invalid coordinates
        str_coord_3 = "abc,def,ghi"
        coord_3 = tuple(int(x) for x in str_coord_3.split(','))
        print(f"Parsing invalid coordinates: \"{str_coord_3}\"")
        print(f"Parsed position: {coord_3}")
        x3, y3, z3 = coord_3
        distance = math.sqrt((x3-x0)**2 + (y3-y0)**2 + (z3-z0)**2)
        print(f"Distance between {origin} and {coord_3}: {distance:.2f}")
        print()
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error detail - Type: ValueError, Args: {e.args}")
    print()
    print("Unpacking demonstration:")
    coor = (4, 7, 3)
    print(f"Player at x={coor[0]}, y={coor[1]}, z={coor[2]}")
    x, y, z = coor
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("\n=== Game Coordinate System ===\n")
    main()
    print()
