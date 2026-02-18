

players = {
    "alice": {
        "score": 2300,
        "achievements": {"first_kill", 'treasure_hunter', 'speed_demon',
                         'perfectionist', 'explorator'},
        "region": "north",
        "active": True
    },
    "bob": {
        "score": 1800,
        "achievements": {"level_10", 'boss', 'explorator'},
        "region": "east",
        "active": True
    },
    "charlie": {
        "score": 2150,
        "achievements": {"boss_slayer", 'treasure_hunter', 'speed_demon',
                         'collector', 'perfectionist', 'explorator',
                         'boss'},
        "region": "central",
        "active": True
    },
    "diana": {
        "score": 2050,
        "achievements": {'explorator', 'boss', 'collector'},
        "region": "north",
        "active": False
    }
}


def comprehension_list() -> None:
    print("\n=== List Comprehension Examples ===")
    high_scorers = [i for i in players if players[i]["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    scores_doubled = [players[j]["score"] * 2 for j in players]
    print(f"Scores doubled: {scores_doubled}")
    active_player = [x for x in players if players[x]["active"] is True]
    print(f"Active players: {active_player}")


def comprehension_dict() -> None:
    print("\n=== Dict Comprehension Examples ===")
    player_score = {
        k: players[k]["score"] for k in players if players[k]["score"] != 2050}
    print(f"Player scores: {player_score}")
    score_categories = {
        "high": sum(1 for p in players.values() if p["score"] >= 2100),
        "medium": sum(1 for p in players.values()
                      if 1900 <= p["score"] < 2100),
        "low": sum(1 for p in players.values() if p["score"] < 1900),
    }
    print(f"Scores Categories: {score_categories}")
    achv_cont = {
        k: len(players[k]["achievements"]) for k in players
        if players[k]["score"] != 2050
    }
    print(f"Achievement counts: {achv_cont}")


def comprehension_set() -> None:
    print("\n=== Set Comprehension Examples ===")
    unique_player = {name for name in players}
    print(f"Unique players: {unique_player}")

    all_achievements = set()
    for p in players.values():
        all_achievements.update(p["achievements"])

    unique_achievement = set()
    for achv in all_achievements:
        count = sum(1 for p in players.values() if achv in p["achievements"])
        if count == 1:
            unique_achievement.add(achv)

    print(f"Unique Achievements: {unique_achievement}")
    active_regions = {
        players[p]["region"] for p in players if players[p]["active"]
    }
    print(f"Active regions: {active_regions}")


def combined_analysis() -> None:
    print("\n=== Combined Analysis ===")
    total_player = len([i for i in players if players[i]])
    print(f"Total players: {total_player}")

    total_ach = {ach for p in players.values() for ach in p["achievements"]}
    print("Total unique achievements:", len(total_ach))

    score_list = [p["score"] for p in players.values()]
    print("Average score:", sum(score_list) / len(players))

    topscore = max(score_list)
    top = {k: v["score"] for k, v in players.items() if v["score"] == topscore}
    top_player = list(top.keys())[0]
    print(f"Top performer: {top_player} ({players[top_player]['score']} "
          f"points, {len(players[top_player]['achievements'])} achievements)")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    comprehension_list()
    comprehension_dict()
    comprehension_set()
    combined_analysis()
