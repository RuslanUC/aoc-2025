from math import sqrt
from typing import TypeVar, Generator

T = TypeVar("T")
CoordT = tuple[int, int, int]
DistanceT = tuple[int | float, CoordT, CoordT]
CircuitsT = dict[CoordT, set[CoordT]]

def enumerate_from(it: list[T], start_from: int) -> Generator[tuple[int, T], None, None]:
    for i in range(start_from, len(it)):
        yield i, it[i]


def part1(distances: list[DistanceT]) -> CircuitsT:
    circuits: dict[CoordT, set[CoordT]] = {}

    for i in range(1000):
        _, xyz1, xyz2 = distances[i]

        if xyz1 not in circuits and xyz2 not in circuits:
            circuits[xyz1] = circuits[xyz2] = {xyz1, xyz2}
        elif xyz1 in circuits and xyz2 not in circuits:
            circuits[xyz1].add(xyz2)
            circuits[xyz2] = circuits[xyz1]
        elif xyz1 not in circuits and xyz2 in circuits:
            circuits[xyz2].add(xyz1)
            circuits[xyz1] = circuits[xyz2]
        elif circuits[xyz1] is not circuits[xyz2]:
            new_circuit = {*circuits[xyz1], *circuits[xyz2]}
            for j in circuits[xyz2]:
                circuits[j] = new_circuit
            for j in circuits[xyz2]:
                circuits[j] = new_circuit

    seen_ids = set()
    result = 1

    for idx, circuit in enumerate(sorted(circuits.values(), key=len, reverse=True)):
        if id(circuit) in seen_ids:
            continue
        seen_ids.add(id(circuit))
        if len(seen_ids) <= 3:
            result *= len(circuit)

    print(f"Part 1 answer: {result}")

    return circuits


def part2(
        distances: list[DistanceT], boxes_num: int, circuits: CircuitsT | None = None, start_from: int | None = None
) -> None:
    if start_from is None or circuits is None:
        start_from = 0
    if circuits is None:
        circuits = {}

    for i in range(start_from, len(distances)):
        _, xyz1, xyz2 = distances[i]

        if xyz1 not in circuits and xyz2 not in circuits:
            circuits[xyz1] = circuits[xyz2] = {xyz1, xyz2}
        elif xyz1 in circuits and xyz2 not in circuits:
            circuits[xyz1].add(xyz2)
            circuits[xyz2] = circuits[xyz1]
        elif xyz1 not in circuits and xyz2 in circuits:
            circuits[xyz2].add(xyz1)
            circuits[xyz1] = circuits[xyz2]
        elif circuits[xyz1] is not circuits[xyz2]:
            new_circuit = {*circuits[xyz1], *circuits[xyz2]}
            for j in circuits[xyz1]:
                circuits[j] = new_circuit
            for j in circuits[xyz2]:
                circuits[j] = new_circuit

        if len(circuits[xyz1]) == boxes_num:
            x1 = xyz1[0]
            x2 = xyz2[0]
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

    distances = [
        (
            sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2),
            (x1, y1, z1),
            (x2, y2, z2),
        )
        for idx1, (x1, y1, z1) in enumerate(boxes)
        for idx2, (x2, y2, z2) in enumerate_from(boxes, idx1 + 1)
    ]

    distances.sort(key=lambda e: e[0])

    circuits = part1(distances)
    part2(distances, len(boxes), circuits, 1000)


if __name__ == "__main__":
    main()
