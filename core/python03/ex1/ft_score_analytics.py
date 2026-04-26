import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    total_args: list = sys.argv[1:]

    if not total_args:
        print(f"No scores provided. Usage: python3 {sys.argv[0]}" "<score1> "
              "<score2> ...")
        return

    try:
        # checking if args are ints and adding them 1by1 to the list "scores"
        scores = [int(arg) for arg in total_args]
        print(f"Scores processed: {scores}")
    except ValueError:
        print("The input is invalid :-( please type in numbers")
        return

    total_players: int = len(scores)
    total_score: int = sum(scores)
    average_score: float = total_score / total_players
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score

    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
