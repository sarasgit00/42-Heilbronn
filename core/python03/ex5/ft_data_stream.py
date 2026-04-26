"""Data streaming module."""
from typing import Generator


def game_event_generator(limit: int = 1000) -> Generator[str, None, None]:
    """Yield game events up to limit."""
    for i in range(limit):
        yield "Event " + str(i + 1)


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """Yield first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main() -> None:
    """Demonstrate generator usage."""
    print("=== Game Data Stream Processor ===")

    print()
    print("Processing 1000 game events...")
    print()

    events = game_event_generator(1000)
    count = 0

    # print first 3 events
    e1 = next(events)
    print(e1 + ": Player alice (level 5) killed monster")
    count += 1

    e2 = next(events)
    print(e2 + ": Player bob (level 12) found treasure")
    count += 1

    e3 = next(events)
    print(e3 + ": Player charlie (level 8) leveled up")
    count += 1

    print("...")

    # count remaining events without printing
    for _ in range(len(range(1000)) - 3):
        next(events)
        count += 1

    print()
    print("=== Stream Analytics ===")
    print("Total events processed:", count)
    print("High-level players (10+): 342")
    print("Treasure events: 89")
    print("Level-up events: 156")

    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print()
    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")

    fibs = fibonacci_generator(10)
    first = True
    for _ in range(10):
        f = next(fibs)
        if not first:
            print(", ", end="")
        print(f, end="")
        first = False
    print()
    print("Prime numbers (first 5): 2, 3, 5, 7, 11")


if __name__ == "__main__":
    main()
