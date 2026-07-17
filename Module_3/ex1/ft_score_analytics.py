import sys

def process_scores(args):
    scores = []
    for arg in args:
        try:
            score = int(arg)
            if score < 0:
                raise ValueError(f"{score} is too low for a score (min 0)")
            scores.append(score)
        except ValueError as e:
            print(f"Caught process_scores error: {e}")
    return scores

def main():
    print("=== Player Score Analytics ===")
    l = len(sys.argv[1:])
    if (l == 0):
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    scores = process_scores(sys.argv[1:])
    if scores:
        TotalPlayers = l
        TotalScore = sum(scores)
        AverageScore = (TotalScore / TotalPlayers) * 1.0
        HighScore = max(scores)
        LowScore = min(scores)
        ScoreRange = HighScore - LowScore
        print(f"Total Players: {TotalPlayers}")
        print(f"Total Score: {TotalScore}")
        print(f"Average Score: {AverageScore}")
        print(f"High Score: {HighScore}")
        print(f"Low Score: {LowScore}")
        print(f"Score Range: {ScoreRange}")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")

if __name__ == "__main__":
    main()