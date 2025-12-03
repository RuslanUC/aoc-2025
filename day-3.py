def maxidx(lst: list[int], start: int | None = None, end: int | None = None) -> int:
    if start is None:
        start = 0
    if end is None:
        end = len(lst)
    return max(range(start, end), key=lst.__getitem__)


def part1(banks: list[list[int]]) -> None:
    total_output = 0

    for bank in banks:
        max_idx = maxidx(bank)
        if max_idx == len(bank) - 1:
            bat2 = bank[max_idx]
            bat1 = bank[maxidx(bank, end=len(bank) - 1)]
        else:
            bat1 = bank[max_idx]
            bat2 = bank[max_idx + 1]
            for i in range(max_idx + 1, len(bank)):
                bat2 = max(bat2, bank[i])

        joltage = bat1 * 10 + bat2
        total_output += joltage
        # print(joltage)

    print(f"Part 1 total joltage: {total_output}")


def part2(banks: list[list[int]]) -> None:
    total_output = 0

    for bank in banks:
        enable = []
        start = 0
        while len(enable) < 12:
            max_idx = maxidx(bank, start, len(bank) - 12 + len(enable) + 1)
            enable.append(bank[max_idx])
            start = max_idx + 1

        joltage = 0
        for bat in enable:
            joltage *= 10
            joltage += bat

        total_output += joltage
        # print(joltage)

    print(f"Part 2 total joltage: {total_output}")


def main() -> None:
    with open("inputs/day-3.txt") as f:
        banks = f.read().splitlines(False)

    banks = [
        [int(battery) for battery in bank]
        for bank in banks
    ]

    # part1(banks)
    part2(banks)


if __name__ == "__main__":
    main()
