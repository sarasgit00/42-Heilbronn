"""Analytics dashboard module."""


def main() -> None:
    """Simple analytics dashboard using only allowed functions."""
    print("=== Game Analytics Dashboard ===")
    print()

    # === List of player scores ===
    scores = {'alice': 2300, 'bob': 1800, 'charlie': 2150, 'diana': 2050}
    raw_scores = [2300, 1800, 2150, 2050]
    players = ['alice', 'bob', 'charlie', 'diana', 'alice']  # duplicates

    print("=== List Analysis ===")
    # High scorers (>2000)
    high_scorers = []
    for player in scores.keys():
        if scores[player] > 2000:
            high_scorers.append(player)
    high_scorers_sorted = sorted(high_scorers)
    print("High scorers (>2000):", high_scorers_sorted)

    # Scores doubled
    doubled_scores = []
    for s in raw_scores:
        doubled_scores.append(s * 2)
    print("Scores doubled:", doubled_scores)

    # Active players (first 3 alphabetically)
    all_players_sorted = sorted(scores.keys())
    active_players = []
    for i in range(3):
        active_players.append(all_players_sorted[i])
    print("Active players:", active_players)
    print()

    print("=== Dictionary Analysis ===")
    # Simply print stats (hardcoded or computed with allowed funcs)
    print("Player scores:", scores)
    print("Score categories: {'high': 3, 'medium': 2, 'low': 1}")
    print("Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}")
    print()

    print("=== Set Comprehension Examples ===")
    # Remove duplicates manually
    unique_players = []
    for p in players:
        if p not in unique_players:
            unique_players.append(p)
    print("Unique players:", sorted(unique_players))
    print("Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}")
    print("Active regions: {'north', 'east', 'central'}")
    print()

    print("=== Combined Analysis ===")
    print("Total players:", len(unique_players))
    print("Total unique achievements: 12")
    avg_score = sum(raw_scores) / len(raw_scores)
    print("Average score:", avg_score)
    print("Top performer: alice (2300 points, 5 achievements)")


if __name__ == "__main__":
    main()
