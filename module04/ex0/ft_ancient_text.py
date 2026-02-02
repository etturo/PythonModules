#!/usr/bin/env python3
def main():
    print()
    print("Accessing Storage Vault: ancient_fragment.txt")
    with open("ancient_fragment.txt", "r") as fd:
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(fd.read())
    print()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    main()
    print()
