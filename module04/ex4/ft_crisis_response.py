#!/usr/bin/env python3
def main() -> None:
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost archive", "r") as fd:
            fd.read()
    except (FileNotFoundError):
        print("RESPONSE: Archive not found in storage matrix")
    finally:
        print("STATUS: Crisis handled, system stable")
    print()
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("classified_vault.txt", "r") as fd:
            fd.read()
    except (PermissionError):
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained")
    print()
    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", "r") as fd:
            line: str = fd.read()
            print("SUCCESS: Archive recovered - "
                  f"''{line}''")
    except (PermissionError, FileNotFoundError):
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Normal operations resumed")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    print("\n=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    main()
    print()
