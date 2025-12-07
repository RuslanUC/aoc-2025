from typing import Literal


def part1(manifold: list[list[Literal[".", "^", "S"]]]) -> None:
    splits = 0

    beams = [manifold[0].index("S")]

    for idx, row in enumerate(manifold):
        new_beams = []
        split_idx = set()
        for beam in beams:
            if row[beam] == "^":
                if beam > 0 and (beam - 1) not in new_beams:
                    new_beams.append(beam - 1)
                if beam < len(manifold[0]) - 1 and (beam + 1) not in new_beams:
                    new_beams.append(beam + 1)
                if beam not in split_idx:
                    splits += 1
                    split_idx.add(beam)
            else:
                new_beams.append(beam)

        beams = new_beams

    print(f"Part 1 splits: {splits}")


CACHE = {}


def dfs(manifold: list[list[Literal[".", "^", "S"]]], row: int, beam: int) -> int:
    key = (row, beam)
    if key in CACHE:
        return CACHE[key]

    for i in range(row, len(manifold)):
        if manifold[i][beam] != "^":
            continue

        left = 0
        right = 0

        if beam > 0:
            left = dfs(manifold, i + 1, beam - 1)
        if beam < len(manifold[0]) - 1:
            right = dfs(manifold, i + 1, beam + 1)

        CACHE[key] = left + right
        return left + right

    CACHE[key] = 1
    return 1


def part2(manifold: list[list[Literal[".", "^", "S"]]]) -> None:
    beam = manifold[0].index("S")
    timelines = dfs(manifold, 1, beam)

    print(f"Part 1 timelines: {timelines}")


def main() -> None:
    with open("inputs/day-7.txt") as f:
        rows = f.read().splitlines(False)

    manifold = [
        list(row)
        for row in rows
    ]

    part1(manifold)
    part2(manifold)


if __name__ == "__main__":
    main()
