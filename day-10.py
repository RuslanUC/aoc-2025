class MachinePart1:
    __slots__ = ("need", "buttons",)

    def __init__(self, need: int, buttons: list[int]) -> None:
        self.need = need
        self.buttons = buttons


class MachinePart2:
    __slots__ = ("buttons", "joltage",)

    def __init__(self, buttons: list[list[int]], joltage: list[int]) -> None:
        self.buttons = buttons
        self.joltage = joltage


def dfs_part1(state: int, buttons: list[int]) -> int | float:
    initial_state = state

    if not buttons:
        return float("inf")

    state ^= buttons[0]
    if state == 0:
        return 1

    presses1 = dfs_part1(state, buttons[1:])
    presses2 = dfs_part1(initial_state, buttons[1:])

    if presses1 < presses2:
        return presses1 + 1
    return presses2


def part1(machines: list[MachinePart1]) -> None:
    presses = 0

    for machine in machines:
        presses += dfs_part1(machine.need, machine.buttons)

    print(f"Part 1 presses: {presses}")


def part2(machines: list[MachinePart2]) -> None:
    import z3

    total = 0
    for machine in machines:
        solver = z3.Optimize()
        variables = []
        joltages: list[None | z3.Int] = [None for _ in machine.joltage]

        for name, button in enumerate(machine.buttons):
            var = z3.Int(str(name))
            variables.append(var)
            solver.add(var >= 0)

            for entry in button:
                if joltages[entry] is None:
                    joltages[entry] = var
                else:
                    joltages[entry] = joltages[entry] + var

        for jolt_int, entry in enumerate(machine.joltage):
            if joltages[jolt_int] is None:
                continue
            solver.add(machine.joltage[jolt_int] == joltages[jolt_int])

        total_presses = solver.minimize(sum(variables))

        if solver.check() == z3.sat:
            total += total_presses.value().as_long()
        else:
            assert False

    print(f"Part 2 presses: {total}")


def main() -> None:
    with open("inputs/day-10.txt") as f:
        rows = f.read().splitlines(False)

    machines_part1 = []
    machines_part2 = []

    for row in rows:
        need_bits = 0
        need = []
        buttons_bits = []
        buttons = []
        joltage = []

        for info in row.split(" "):
            if info[0] == "[":
                need = 0
                for char in info[1:-1]:
                    need <<= 1
                    need |= char == "#"
                    need_bits += 1
            elif info[0] == "(":
                button = 0
                for bit in info[1:-1].split(","):
                    button |= 1 << need_bits - int(bit) - 1
                buttons_bits.append(button)
                buttons.append([int(j) for j in info[1:-1].split(",")])
            elif info[0] == "{":
                joltage = [int(j) for j in info[1:-1].split(",")]
            else:
                print(f"WHAT: {info!r}")

        machines_part1.append(MachinePart1(need, buttons_bits))
        machines_part2.append(MachinePart2(buttons, joltage))

    part1(machines_part1)
    part2(machines_part2)


if __name__ == "__main__":
    main()
