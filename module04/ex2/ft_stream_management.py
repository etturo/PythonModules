#!/usr/bin/env python3
import sys


def main():
    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    name = sys.stdin.readline()
    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    report = sys.stdin.readline()
    print()
    sys.stdout.flush()
    sys.stdout.write("[STANDARD] Archive status from "
                     f"{name.strip()}: {report.strip()}\n")
    sys.stdout.flush()
    sys.stderr.write("[ALERT] System diagnostic:"
                     " Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.flush()
    sys.stdout.write("\nThree-channel communication test successful.\n")
    sys.stdout.flush()


if __name__ == "__main__":
    print("\n=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    main()
    print()
