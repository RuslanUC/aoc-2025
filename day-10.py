class Machine:
    __slots__ = ("need", "buttons", "joltage",)

    def __init__(self, need: int, buttons: list[int], joltage: list[int]) -> None:
        self.need = need
        self.buttons = buttons
        self.joltage = joltage


def dfs(state: int, buttons: list[int]) -> int | float:
    initial_state = state

    if not buttons:
        return float("inf")

    state ^= buttons[0]
    if state == 0:
        return 1

    presses1 = dfs(state, buttons[1:])
    presses2 = dfs(initial_state, buttons[1:])

    if presses1 < presses2:
        return presses1 + 1
    return presses2


def part1(machines: list[Machine]) -> None:
    total_presses = 0

    for machine in machines:
        presses = dfs(machine.need, machine.buttons)
        total_presses += presses

    print(f"Part 1 presses: {total_presses}")


def part2(machines: list[Machine]) -> None:
    print(f"Part 2 ...: {...}")



def main() -> None:
    with open("inputs/day-10.txt") as f:
        rows = f.read().splitlines(False)

    machines = []
    for row in rows:
        need_bits = 0
        need = []
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
                buttons.append(button)
            elif info[0] == "{":
                joltage = [int(j) for j in info[1:-1].split(",")]
            else:
                print(f"WHAT: {info!r}")

        machines.append(Machine(need, buttons, joltage))

    part1(machines)
    # part2(machines)


if __name__ == "__main__":
    main()
