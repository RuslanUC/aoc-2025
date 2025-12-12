def rotate1(shape: list[list[bool]]) -> list[list[bool]]:
    rows = len(shape)
    cols = len(shape[0])

    result = [
        [
            False
            for _ in range(rows)
        ]
        for _ in range(cols)
    ]

    for row in range(rows):
        for col in range(cols):
            result[col][rows - row - 1] = shape[row][col]

    return result


def rotate2(shape: list[list[bool]]) -> list[list[bool]]:
    rows = len(shape)
    cols = len(shape[0])

    result = [
        [
            False
            for _ in range(cols)
        ]
        for _ in range(rows)
    ]

    for row in range(rows):
        for col in range(cols):
            result[rows - row - 1][cols - col - 1] = shape[row][col]

    return result


def rotate3(shape: list[list[bool]]) -> list[list[bool]]:
    rows = len(shape)
    cols = len(shape[0])

    result = [
        [
            False
            for _ in range(rows)
        ]
        for _ in range(cols)
    ]

    for row in range(rows):
        for col in range(cols):
            result[cols - col - 1][row] = shape[row][col]

    return result


def part1(regions: list[tuple[tuple[int, int], list[int]]], shapes: list[list[list[bool]]]) -> None:
    areas = []
    for shape in shapes:
        area = 0
        for row in shape:
            for col in row:
                area += col
        areas.append(area)


    can_fit = 0

    for (w, h), idxs in regions:
        size = w * h

        area = 0
        for idx, count in enumerate(idxs):
            area += areas[idx] * count

        # lol
        if size >= area and (area / size) <= 0.85:
            can_fit += 1

    print(f"Part 1 regions: {can_fit}")


def main() -> None:
    with open("inputs/day-12.txt") as f:
        rows = f.read().split("\n\n")

    rows = [row.splitlines(False) for row in rows]
    *shapes, regions = rows
    shapes = [
        [
            [
                c == "#"
                for c in row
            ]
            for row in shape[1:]
        ]
        for shape in shapes
    ]
    regions = [region.split(": ") for region in regions]
    regions = [
        (
            tuple(map(int, size.split("x"))),
            list(map(int, shapes.split(" ")))
        )
        for size, shapes in regions
    ]

    part1(regions, shapes)


if __name__ == "__main__":
    main()
