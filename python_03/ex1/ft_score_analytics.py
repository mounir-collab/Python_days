import sys

if __name__ == "__main__":
    total_arguments = len(sys.argv)
    print("=== Player Score Analytics ===")

    if total_arguments == 1:
        print(
            "No scores provided. Usage: "
            + "python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        scores = []
        try:
            for i in range(1, total_arguments):
                scores.append(int(sys.argv[i]))
        except ValueError as e:
            print("Error: ", e)
        else:
            total_players = len(scores)
            total_score = sum(scores)
            average_score = total_score / total_players
            high_score = max(scores)
            low_score = min(scores)
            score_range = high_score - low_score

            print("Scores processed: ", scores)
            print("Total players: ", total_players)
            print("Total score: ", total_score)
            print(f"Average score: {average_score:.1f}")
            print("High score: ", high_score)
            print("Low score: ", low_score)
            print("Score range: ", score_range, "\n")
