from typing import Literal


def part1(problems: list[list[int | Literal["+", "*"]]]) -> None:
    total = 0

    for i in range(len(problems[0])):
        if problems[-1][i] == "+":
            for j in range(len(problems) - 1):
                total += problems[j][i]
        else:
            this = 1
            for j in range(len(problems) - 1):
                this *= problems[j][i]
            total += this

    print(f"Part 1 total: {total}")


def part2(problems: list[list[int | Literal["+", "*"]]], rows: list[str]) -> None:
    total = 0

    start_indexes = [idx for idx, char in enumerate(rows[-1]) if char in ("+", "*")]

    maxrowlen = max(map(len, rows))

    for i in range(len(problems[0])):
        start_idx = start_indexes[i]
        if i == len(problems[0]) - 1:
            end_idx = maxrowlen
        else:
            end_idx = start_indexes[i + 1] - 1

        this = 0 if problems[-1][i] == "+" else 1

        for j in range(end_idx - 1, start_idx - 1, -1):
            num = 0
            for k in range(len(problems) - 1):
                if j >= len(rows[k]):
                    continue
                if rows[k][j].isdigit():
                    num *= 10
                    num += int(rows[k][j])
            if problems[-1][i] == "+":
                print(f"+{num}")
                this += num
            else:
                print(f"*{num}")
                this *= num

        total += this

        print("=" * 32)

    print(f"Part 2 total: {total}")


def main() -> None:
    with open("inputs/day-6.txt") as f:
        rows = f.read().splitlines(False)

    problems = [
        [
            int(col.strip()) if col.strip().isdigit() else col.strip()
            for col in row.split(" ")
            if col != ""
        ]
        for row in rows
    ]

    part1(problems)
    part2(problems, rows)


if __name__ == "__main__":
    main()
