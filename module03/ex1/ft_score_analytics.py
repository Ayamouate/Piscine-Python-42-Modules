import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) > 1:
        numbers = []
        for arg in sys.argv[1:]:
            try:
                nbr = int(arg)
                numbers.append(nbr)
            except ValueError:
                print(f"Oops, {arg} is not a valid number!")
        print(f"Scores processed: {numbers}")
        print(f"Total players: {len(numbers)}")
        print(f"Total score: {sum(numbers)}")
        print(f"Average score: {sum(numbers) / len(numbers)}")
        print(f"High score: {max(numbers)}")
        print(f"Low score: {min(numbers)}")
        print(f"Score range: {max(numbers) - min(numbers)}")
    else:
        print(f"No scores provided. Usage: python3"
              f"{sys.argv[0]} <score1> <score2> ...")
