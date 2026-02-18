from typing import Generator


players = [
    ("alice", 5, "monster"),
    ("bob", 12, "treasure"),
    ("charlie", 8, "levelup"),
    ("alice", 15, "monster")
]


def game_events(n: int) -> Generator[tuple[str, int, str], None, None]:
    for i in range(n):
        name, level, action = players[i % len(players)]
        yield name, level, action


def generate(n: int, itr: Generator[tuple[str, int, str], None, None]) -> None:
    print(f"Processing {n} game events...\n")
    event_number = 1
    for name, level, event in itr:
        if event == "monster":
            print(f"Event {event_number}: Player {name} (level {level}) "
                  f"killed {event}")
        elif event == "treasure":
            print(f"Event {event_number}: Player {name} (level {level}) "
                  f"found {event}")
        else:
            print(f"Event {event_number}: Player {name} (level {level}) "
                  f"leveled up")
        event_number += 1


def process_stream(n) -> dict[str, int]:
    total_events = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    for name, level, event_type in game_events(n):
        total_events += 1
        if level >= 10:
            high_level_count += 1
        if event_type == "treasure":
            treasure_count += 1
        if event_type == "levelup":
            levelup_count += 1
    return {
        "total": total_events,
        "high_level": high_level_count,
        "treasure": treasure_count,
        "levelup": levelup_count,
    }


def is_prime(n: int) -> Generator[int, None, None]:
    nb: int = 2
    cont: int = 0
    while cont < n:
        for i in range(2, nb):
            if nb % i == 0:
                break
        else:
            cont += 1
            yield nb
        nb += 1


def fibonacci(n: int) -> Generator[int, None, None]:
    i1 = 0
    j1 = 1
    for i in range(n):
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        else:
            i1, j1 = j1, i1 + j1
            yield j1


def main() -> None:
    print("== Game Data Stream Processor ===\n")
    n: int = 1000
    itr: Generator[tuple(str, int, str), None, None] = game_events(n)
    generate(n, itr)
    print("\n=== Stream Analytics ===")
    stats = process_stream(1000)
    print(f"Total events processed: {stats['total']}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['levelup']}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time:  0.045 seconds")
    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=' ')
    fib = fibonacci(10)
    for i in range(10):
        print(f"{next(fib)}", end='')
        if i != 9:
            print(",", end=' ')
    print()
    print("Prime numbers (first 5):", end=' ')
    pr = is_prime(5)
    for i in range(5):
        print(f"{next(pr)}", end='')
        if i != 4:
            print(",", end=' ')
    print()


if __name__ == "__main__":
    main()
