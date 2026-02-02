#!/usr/bin/env python3
def main():
    print("=== List Comprehension Examples ===")
    players_list: list = ['alice', 
                          'charlie', 
                          'diana']
    print(f"Actual Players: {players_list}")
    print()
    players_list.append('bob')
    print("Added a new player!")
    print(f"Actual Players: {players_list}")
    print()
    print("Let's capitalize every name in Player's list!")
    for player in players_list:
        player = player.capitalize()
    print(f"Actual Players: {players_list}")
    print()
    print("=== Dict Comprehension Examples ===")
    players_dict: dict = {'alice' : 3450,
                          'charlie' : 5829,
                          'diana' : 4932}
    print(f"Players in the game:")
    for player in players_dict.keys():
        print(f"{player}", end="\t")
        print(f"({players_dict[player]} points)")
    print()
    high_score: int = 0
    for score in players_dict.values():
        if score > 4000:
            high_score += 1
    print(f"High scores (over 4000): {high_score} platers")
    print()
    print("=== Set Comprehension Examples ===")
    achievements_set: set = {'first_kill', 
                             'level 10', 
                             'boss_slayer'}
    achievements_set.add('boss_slayer')
    print(f"Unique Players: {achievements_set}")


if __name__ == "__main__":
    print("\n=== Game Analytics Dashboard ===\n")
    main()
    print()