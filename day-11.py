def part1(paths: list[tuple[str, list[str]]]) -> None:
    import networkx as nx

    graph = nx.DiGraph()

    for source, dests in paths:
        for dest in dests:
            graph.add_edge(source, dest)

    out_paths = nx.all_simple_paths(graph, "you", "out")

    count = 0
    for _ in out_paths:
        count += 1

    print(f"Part 1 paths: {count}")


def part2(paths: list[tuple[str, list[str]]]) -> None:
    ...


def main() -> None:
    with open("inputs/day-11.txt") as f:
        rows = f.read().splitlines(False)

    paths = []

    for row in rows:
        source, destinations = row.split(":")
        destinations = [dest.strip() for dest in destinations.split(" ")]

        paths.append((source, destinations))

    part1(paths)
    part2(paths)


if __name__ == "__main__":
    main()
