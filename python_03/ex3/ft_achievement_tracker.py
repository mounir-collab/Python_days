data_dict = {
    "alice": [
        "first_blood",
        "pixel_perfect",
        "speed_runner",
        "first_blood",
        "first_blood",
    ],
    "bob": [
        "level_master",
        "boss_hunter",
        "treasure_seeker",
        "level_master",
        "level_master",
    ],
    "charlie": [
        "treasure_seeker",
        "boss_hunter",
        "combo_king",
        "first_blood",
        "boss_hunter",
        "first_blood",
        "boss_hunter",
        "first_blood",
    ],
    "diana": [
        "first_blood",
        "combo_king",
        "level_master",
        "treasure_seeker",
        "speed_runner",
        "combo_king",
        "combo_king",
        "level_master",
    ],
    "eve": [
        "level_master",
        "treasure_seeker",
        "first_blood",
        "treasure_seeker",
        "first_blood",
        "treasure_seeker",
    ],
    "frank": [
        "explorer",
        "boss_hunter",
        "first_blood",
        "explorer",
        "first_blood",
        "boss_hunter",
    ],
}

# hashable : int , str , tuple (immutable)
# unhashable : set , list , dict (muttable)


if __name__ == "__main__":

    print("=== Achievement Tracker System ===\n")

    alice = set(data_dict["alice"])
    bob = set(data_dict["bob"])
    charlie = set(data_dict["charlie"])

    print("\nPlayer alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)

    print("\n=== Achievement Analytics ===\n")

    unique_achievements = alice.union(bob).union(charlie)
    print("All unique achievements: ", unique_achievements)
    print("Total unique achievements: ", len(unique_achievements))

    common_for_all = alice.intersection(bob).intersection(charlie)
    print("\nCommon to all players: ", common_for_all)

    rare_achievements = alice.difference(bob).difference(charlie)
    print("Rare achievements (1 player): ", rare_achievements)

    common_alice_bob = alice.intersection(bob)
    print("\nAlice vs Bob common: ", common_alice_bob)

    alice_unique = alice.difference(bob)
    print("Alice unique: ", alice_unique)

    bob_unique = bob.difference(alice)
    print("Bob unique: ", bob_unique)
