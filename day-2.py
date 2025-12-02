def part1(ranges: list[str]) -> None:
    invalid_ids = 0
    invalids_sum = 0

    for range_ in ranges:
        start, end = range_.split("-")
        for i in range(int(start), int(end) + 1):
            si = str(i)
            lsi = len(si)

            if lsi % 2 != 0:
                continue

            if si[:lsi // 2] == si[lsi // 2:]:
                invalid_ids += 1
                invalids_sum += i

    print(f"Part 1 invalid ids: {invalid_ids}")
    print(f"Part 1 invalid ids sum: {invalids_sum}")


def part2(ranges: list[str]) -> None:
    invalid_ids = 0
    invalids_sum = 0

    factors = {}

    for range_ in ranges:
        start, end = range_.split("-")
        for i in range(int(start), int(end) + 1):
            si = str(i)
            lsi = len(si)

            if lsi not in factors:
                factors[lsi] = []
                for j in range(1, lsi):
                    if lsi % j == 0:
                        factors[lsi].append((j, lsi // j))

            for first, mul in factors[lsi]:
                if si[:first] * mul == si:
                    invalid_ids += 1
                    invalids_sum += i
                    break

    print(f"Part 2 invalid ids: {invalid_ids}")
    print(f"Part 2 invalid ids sum: {invalids_sum}")


def main() -> None:
    with open("inputs/day-2.txt") as f:
        ranges = f.read().replace("\n", "").split(",")

    part1(ranges)
    part2(ranges)


if __name__ == "__main__":
    main()
