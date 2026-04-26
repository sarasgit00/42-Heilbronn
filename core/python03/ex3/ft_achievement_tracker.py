def ft_achievement_tracker() -> None:
    alice_achievements = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon",
    }
    bob_achievements = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector",
    }
    charlie_achievements = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print("=== Achievement Tracker System ===")
    print()
    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")
    print()

    print("=== Achievement Analytics ===")
    # Union: | combine everything without duplicates
    all_unique_achievements = (
        alice_achievements
        | bob_achievements
        | charlie_achievements
    )
    print(f"All unique achievements: {all_unique_achievements}")
    print(f"Total unique achievements: {len(all_unique_achievements)}")
    print()

    # Intersection: & keep only achievements shared by everyone
    common_achievements = (
        alice_achievements
        & bob_achievements
        & charlie_achievements
    )
    print(f"Common to all players: {common_achievements}")

    # difference
    rare_achievements = (
        (alice_achievements - bob_achievements - charlie_achievements)
        | (charlie_achievements - alice_achievements - bob_achievements)
        | (bob_achievements - alice_achievements - charlie_achievements)
    )
    print(f"Rare achievements (1 player): {rare_achievements}")
    print()

    print(f"Alice vs Bob common: {alice_achievements & bob_achievements}")
    print(f"Alice unique: {alice_achievements - bob_achievements}")
    print(f"Bob unique: {bob_achievements - alice_achievements}")


if __name__ == "__main__":
    ft_achievement_tracker()
