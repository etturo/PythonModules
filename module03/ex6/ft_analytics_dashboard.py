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
    players_dict: dict = {'alice': 3450,
                          'charlie': 5829,
                          'diana': 4932}
    print("Players in the game:")
    for player in players_dict.keys():
        print(f"{player}", end="\t")
        print(f"({players_dict[player]} points)")
    print()
    high_score: int = 0
    for score in players_dict.values():
        if score > 4000:
            high_score += 1
    total_score: int = 0
    for score in players_dict.values():
        total_score += score
    avarage_score: int = total_score / len(players_dict)
    print(f"High scores (over 4000): {high_score} platers")
    print()
    print("=== Set Comprehension Examples ===")
    achievements_set: set = {'first_kill',
                             'level 10',
                             'boss_slayer'}
    achievements_set.add('boss_slayer')
    region_set: set = {"Asia",
                       "Europe",
                       "America"}
    asia_set: set = {'Asia'}
    print(f"Unique Achievements: {achievements_set}")
    print(f"Region without Asia: {region_set.difference(asia_set)}")
    print()
    print("=== Combined Analysis ===")
    print(f"Total players: {len(players_list)}")
    print(f"Total unique achievements: {achievements_set}")
    print(f"Score avarage: {avarage_score}")
    print(f"Top player: Charlie ({players_dict['charlie']} points)")


if __name__ == "__main__":
    print("\n=== Game Analytics Dashboard ===\n")
    main()
    print()
