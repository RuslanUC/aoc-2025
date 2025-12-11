def count_paths(
        g: dict[str, set[str]], from_: str, to: str, visited: set[str] | None = None,
        cache: dict[str, int] | None = None,
) -> int:
    if visited is None:
        visited = set()

    if from_ in visited:
        return 0

    if from_ == to:
        return 1

    if from_ not in g:
        return 0

    if cache is not None and from_ in cache:
        return cache[from_]

    count_ = 0
    visited.add(from_)
    for new_from in g[from_]:
        count_ += count_paths(g, new_from, to, visited, cache)
    visited.remove(from_)

    if cache is not None:
        cache[from_] = count_

    return count_


def part1(graph: dict[str, set[str]]) -> None:
    count = count_paths(graph, "you", "out", cache={})
    print(f"Part 1 paths: {count}")


def part2(graph: dict[str, set[str]]) -> None:
    dac_fft = count_paths(graph, "dac", "fft", cache={})
    fft_dac = count_paths(graph, "fft", "dac", cache={})

    if dac_fft:
        svr_dac = count_paths(graph, "svr", "dac", cache={})
        fft_out = count_paths(graph, "fft", "out", cache={})
        count = svr_dac * dac_fft * fft_out
    elif fft_dac:
        svr_fft = count_paths(graph, "svr", "fft", cache={})
        dac_out = count_paths(graph, "dac", "out", cache={})
        count = svr_fft * fft_dac * dac_out
    else:
        count = 0

    print(f"Part 2 paths: {count}")


def main() -> None:
    with open("inputs/day-11.txt") as f:
        rows = f.read().splitlines(False)

    graph = {}

    for row in rows:
        source, destinations = row.split(":")
        graph[source] = set(destinations.strip().split(" "))

    part1(graph)
    part2(graph)


if __name__ == "__main__":
    main()
