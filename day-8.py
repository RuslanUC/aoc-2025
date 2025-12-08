from math import sqrt
from typing import Literal, TypeVar, Iterable, Generator

T = TypeVar("T")


def enumerate_from(it: list[T], start_from: int) -> Generator[tuple[int, T], None, None]:
    for i in range(start_from, len(it)):
        yield i, it[i]


def part1(boxes: list[tuple[int, int, int]]) -> None:
    circuits: dict[int, set[int]] = {}

    distances = [
        (
            sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2),
            idx1,
            idx2,
        )
        for idx1, (x1, y1, z1) in enumerate(boxes)
        for idx2, (x2, y2, z2) in enumerate_from(boxes, idx1 + 1)
    ]

    distances.sort(key=lambda e: e[0])

    for i in range(1000):
        shortest_two = distances[i][1:]

        i1, i2 = shortest_two

        if i1 not in circuits and i2 not in circuits:
            circuits[i1] = circuits[i2] = {i1, i2}
        elif i1 in circuits and i2 not in circuits:
            circuits[i1].add(i2)
            circuits[i2] = circuits[i1]
        elif i1 not in circuits and i2 in circuits:
            circuits[i2].add(i1)
            circuits[i1] = circuits[i2]
        elif circuits[i1] is not circuits[i2]:
            new_circuit = {*circuits[i1], *circuits[i2]}
            for j in circuits[i1]:
                circuits[j] = new_circuit
            for j in circuits[i2]:
                circuits[j] = new_circuit

    seen_ids = set()
    result = 1

    for idx, circuit in enumerate(sorted(circuits.values(), key=len, reverse=True)):
        if id(circuit) in seen_ids:
            continue
        # print(circuit)
        seen_ids.add(id(circuit))
        if len(seen_ids) <= 3:
            result *= len(circuit)

    print(f"Part 1 answer: {result}")

    # print(f"Part 1 multiple of three largest circuits: {result}")


def part2(boxes: list[tuple[int, int, int]]) -> None:
    circuits: dict[int, set[int]] = {}

    distances = [
        (
            sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2),
            idx1,
            idx2,
        )
        for idx1, (x1, y1, z1) in enumerate(boxes)
        for idx2, (x2, y2, z2) in enumerate_from(boxes, idx1 + 1)
    ]

    distances.sort(key=lambda e: e[0])

    for i in range(len(distances)):
        shortest_two = distances[i][1:]

        i1, i2 = shortest_two

        if i1 not in circuits and i2 not in circuits:
            circuits[i1] = circuits[i2] = {i1, i2}
        elif i1 in circuits and i2 not in circuits:
            circuits[i1].add(i2)
            circuits[i2] = circuits[i1]
        elif i1 not in circuits and i2 in circuits:
            circuits[i2].add(i1)
            circuits[i1] = circuits[i2]
        elif circuits[i1] is not circuits[i2]:
            new_circuit = {*circuits[i1], *circuits[i2]}
            for j in circuits[i1]:
                circuits[j] = new_circuit
            for j in circuits[i2]:
                circuits[j] = new_circuit

        if len(circuits[i1]) == len(boxes):
            x1, *_ = boxes[i1]
            x2, *_ = boxes[i2]
            print(f"Part 2 answer: {x1 * x2}")
            break



def main() -> None:
    with open("inputs/day-8.txt") as f:
        rows = f.read().splitlines(False)

    boxes = [
        (int(x), int(y), int(z))
        for x, y, z in (
            row.split(",") for row in rows
        )
    ]

    part1(boxes)
    part2(boxes)


if __name__ == "__main__":
    main()
