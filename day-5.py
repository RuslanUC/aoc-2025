def part1(ranges: list[tuple[int, int]], ids: list[int]) -> None:
    available = 0

    for i in ids:
        for start, end in ranges:
            if start <= i <= end:
                available += 1
                break

    print(f"Part 1 available ids: {available}")


def part2(ranges: list[tuple[int, int]]) -> None:
    ranges.sort(key=lambda e: e[0])
    correct_ranges = []

    for start, end in ranges:
        if not correct_ranges:
            correct_ranges.append((start, end))
            continue

        last_start, last_end = correct_ranges[-1]
        if last_start <= start <= last_end:
            correct_ranges[-1] = (last_start, max(end, last_end))
        else:
            correct_ranges.append((start, end))

    available = 0
    # print("ranges:")
    for s, e in correct_ranges:
        available += e - s + 1
        # print(f"  {s} - {e}")

    print(f"Part 2 available ids: {available}")


def main() -> None:
    with open("inputs/day-5.txt") as f:
        ranges, ids = f.read().split("\n\n")

    ranges = [
        (int(start), int(end))
        for range_ in ranges.splitlines(False)
        for start, end in (range_.split("-"),)
    ]
    ids = [
        int(id_)
        for id_ in ids.splitlines(False)
    ]

    part1(ranges, ids)
    part2(ranges)


if __name__ == "__main__":
    main()
