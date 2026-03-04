data_dict = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7,
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4,
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7,
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1,
        },
    },
    "sessions": [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 2361,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 2985,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 34,
            "score": 1285,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 1238,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 1555,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 92,
            "score": 2754,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 98,
            "score": 1102,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 39,
            "score": 2721,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 46,
            "score": 329,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 56,
            "score": 1196,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 1388,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 118,
            "score": 2733,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 22,
            "score": 1110,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 79,
            "score": 1854,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "charlie",
            "duration_minutes": 33,
            "score": 666,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 101,
            "score": 292,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 25,
            "score": 2887,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 53,
            "score": 2540,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 115,
            "score": 147,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 118,
            "score": 2299,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 97,
            "score": 1178,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 18,
            "score": 2661,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 761,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 46,
            "score": 2101,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1359,
            "mode": "casual",
            "completed": True,
        },
    ],
    "game_modes": ["casual", "competitive", "ranked"],
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer",
    ],
}


if __name__ == "__main__":

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    high_scores = [
        player
        for player, p_data in data_dict["players"].items()
        if p_data["total_score"] > 2000
    ]
    print("High scorers (>2000): ", high_scores)

    doubled_scores = [
        p_data["total_score"] * 2 for p_data in data_dict["players"].values()
    ]
    print("Scores doubled: ", doubled_scores)

    active_players = [
        active["player"]
        for active in data_dict["sessions"]
        if active["completed"] is True and active["mode"] == "competitive"
    ]
    print("Active players: ", active_players)

    print("\n=== Dict Comprehension Examples ===")

    dict_scores = {
        player: p_data["total_score"]
        for player, p_data in data_dict["players"].items()
    }
    print("Player scores: ", dict_scores)

    score_categories = {
        "high": sum(1 for val in dict_scores.values() if val >= 4000),
        "medium": sum(1 for val in dict_scores.values() if 2000 <= val < 4000),
        "low": sum(1 for val in dict_scores.values() if val < 2000),
    }
    print("Score categories: ", score_categories)

    achievement_dict = {
        player: p_data["achievements_count"]
        for player, p_data in data_dict["players"].items()
    }
    print("Achievement counts: ", achievement_dict)

    print("\n=== Set Comprehension Examples ===")

    unique_players = {p_data["player"] for p_data in data_dict["sessions"]}
    print("Unique players: ", unique_players)

    unique_achievements = {
        achievement for achievement in data_dict["achievements"]
        }
    print("Unique achievements: ", unique_achievements)

    game_modes = {p_mode["mode"] for p_mode in data_dict["sessions"]}
    print("Game modes: ", game_modes)

    print("\n=== Combined Analysis ===")

    print("Total players: ", len(unique_players))
    print("Total unique achievements: ", len(unique_achievements))
    print(
        f"Average score: "
        f"{sum(dict_scores.values()) / len(dict_scores.values()) :.1f}"
    )

    max_score = 0
    p_name = ""
    for player, score_p in dict_scores.items():
        if score_p > max_score:
            max_score = score_p
            p_name = player

    print(
        f"Top performer: {p_name} ({max_score} points , "
        f"{achievement_dict[p_name]} achievements)"
    )
