def part1(grid: list[list[int]]) -> None:
    can_be_accessed = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not grid[i][j]:
                continue
            adj = 0
            for ci in (i - 1, i, i + 1):
                for cj in (j - 1, j, j + 1):
                    if ci < 0 or ci >= len(grid) or cj < 0 or cj >= len(grid) or (i, j) == (ci, cj):
                        continue
                    adj += grid[ci][cj]
                    if adj >= 4:
                        break
            if adj < 4:
                can_be_accessed += 1

    print(f"Part 1: {can_be_accessed}")


def part2(grid: list[list[int]]) -> None:
    can_be_removed = 0

    grid_next = grid
    old_can_be_removed = -1
    while can_be_removed != old_can_be_removed:
        old_can_be_removed = can_be_removed
        grid = grid_next
        grid_next = [
            row.copy()
            for row in grid
        ]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    continue
                adj = 0
                for ci in (i - 1, i, i + 1):
                    for cj in (j - 1, j, j + 1):
                        if ci < 0 or ci >= len(grid) or cj < 0 or cj >= len(grid) or (i, j) == (ci, cj):
                            continue
                        adj += grid[ci][cj]
                        if adj >= 4:
                            break
                if adj < 4:
                    grid_next[i][j] = 0
                    can_be_removed += 1

    print(f"Part 2: {can_be_removed}")


def main() -> None:
    with open("inputs/day-4.txt") as f:
        rows = f.read().splitlines(False)

    grid = [
        [col == "@" for col in row]
        for row in rows
    ]

    part1(grid)
    part2(grid)


if __name__ == "__main__":
    main()
