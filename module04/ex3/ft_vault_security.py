#!/urs/bin/env python3
def main():
    print("Initiating secure vault access...")
    with open("classified_data.txt", "r") as fd:
        print("Vault connection established with failsafe protocols")
        print()
        print("SECURE EXTRACTION:")
        print(fd.read())
        print()
    with open("new_data.txt", "w+") as fd:
        print("SECURE PRESERVATION")
        fd.write("[CLASSIFIED] New security protocols archived")
        print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    print("\n=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    main()
    print()
