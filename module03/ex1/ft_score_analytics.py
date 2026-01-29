#!/usr/bin/env python3
import sys


def main() -> None:
    scores: list = []
    if len(sys.argv) == 1:
        return print(f"No scores provided. "
                     f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
    try:
        i: int = 1
        while i < len(sys.argv):
            scores.append(int(sys.argv[i]))
            i += 1
    except ValueError:
        return print("Error: non numerical value inserted")
    print(f"Scores processed: {scores}")
    print(f"Total player: {len(sys.argv) - 1}")
    print(f"Total Score: {sum(scores)}")
    print(f"Avarage score: {sum(scores) / (len(sys.argv) - 1)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("\n=== Player Score Analytics ===\n")
    main()
    print()
