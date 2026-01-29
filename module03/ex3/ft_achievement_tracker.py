#!/usr/bin/env python3
def main() -> None:
    alice_ach = {"first_kill",
                 "level_10",
                 "treasure_hunter",
                 "speed_demon"}
    bob_ach = {"first_kill",
               "level_10",
               "boss_slayer",
               "collector"}
    charlie_ach = {"level_10",
                   "treasure_hunter",
                   "boss_slayer",
                   "speed_demon",
                   "perfectionist"}
    # adding a duplicate value to show that is won't add to the set
    alice_ach.add("first_kill")
    total_achievements = alice_ach.union(bob_ach, charlie_ach)
    common_achievements = alice_ach.intersection(bob_ach, charlie_ach)
    alice_unique = alice_ach.difference(bob_ach, charlie_ach)
    bob_unique = bob_ach.difference(alice_ach, charlie_ach)
    charlie_unique = charlie_ach.difference(alice_ach, bob_ach)
    rare_achievements = alice_unique.union(bob_unique, charlie_unique)
    print(f"Player Alice achievements: {alice_ach}")
    print(f"Player Bob achievements: {bob_ach}")
    print(f"Player Charlie achievements: {charlie_ach}")
    print()
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {total_achievements}")
    print(f"Total unique achievements: {len(total_achievements)}")
    print()
    print(f"Common to all players: {common_achievements}")
    print(f"Rare achievements: {rare_achievements}")
    print()
    print(f"Alice vs Bob common: {alice_ach.intersection(bob_ach)}")
    print(f"Alice unique: {alice_ach.difference(bob_ach)}")
    print(f"Bob unique: {bob_ach.difference(alice_ach)}")


if __name__ == "__main__":
    print("\n=== Achievement Tracker System ===\n")
    main()
    print()
