from typing import TypeVar, Generator

T = TypeVar("T")
CoordT = tuple[int, int]

def enumerate_from(it: list[T], start_from: int) -> Generator[tuple[int, T], None, None]:
    for i in range(start_from, len(it)):
        yield i, it[i]


def area(x1: int, y1: int, x2: int, y2: int) -> int:
    h = abs(y2 - y1) + 1
    w = abs(x2 - x1) + 1
    return h * w


def intersects(sx: int, sy: int, ex: int, ey: int, line: tuple[CoordT, CoordT]) -> bool:
    (lsx, lsy), (lex, ley) = line

    if lsx == lex:
        if lsx <= sx or lsx >= ex:
            return False

        min_y = min(lsy, ley)
        max_y = max(lsy, ley)
        if max_y <= sy or min_y >= ey:
            return False

        return True

    if lsy == ley:
        if lsy <= sy or lsy >= ey:
            return False

        min_x = min(lsx, lex)
        max_x = max(lsx, lex)
        if max_x <= sx or min_x >= ex:
            return False

        return True

    return True


def part1(tiles: list[CoordT]) -> None:
    largest_area = 0

    for i1, (x1, y1) in enumerate(tiles):
        for i2, (x2, y2) in enumerate_from(tiles, i1 + 1):
            largest_area = max(largest_area, area(x1, y1, x2, y2))

    print(f"Part 1 largest area: {largest_area}")


def part2(tiles: list[CoordT]) -> None:
    lines: list[tuple[CoordT, CoordT]] = []
    prev: CoordT | None = None

    for xy in tiles:
        if prev is None:
            prev = xy
            continue

        lines.append((prev, xy))
        prev = xy

    lines.append((prev, tiles[0]))

    largest_area = 0

    for i1, (x1, y1) in enumerate(tiles):
        for i2, (x2, y2) in enumerate_from(tiles, i1 + 1):
            area_ = area(x1, y1, x2, y2)
            if area_ < largest_area:
                continue
            
            start_x = min(x1, x2)
            end_x = max(x1, x2)
            start_y = min(y1, y2)
            end_y = max(y1, y2)

            for line in lines:
                if intersects(start_x, start_y, end_x, end_y, line):
                    break
            else:
                largest_area = area_

    print(f"Part 2 largest area: {largest_area}")



def main() -> None:
    with open("inputs/day-9.txt") as f:
        rows = f.read().splitlines(False)

    tiles = [
        (int(x), int(y))
        for x, y in (
            row.split(",") for row in rows
        )
    ]

    # part1(tiles)
    part2(tiles)


if __name__ == "__main__":
    main()
