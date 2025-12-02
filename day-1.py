def main() -> None:
    with open("inputs/day-1.txt") as f:
        rotations = f.read().splitlines(False)

    part1_password = 0
    part2_password = 0

    dial = 50

    for rot in rotations:
        dist = int(rot[1:])
        old_dial = dial
        if rot[0] == "L":
            dial -= dist
        else:
            dial += dist

        if dial >= 100:
            part2_password += dial // 100
        elif dial <= 0:
            part2_password += -dial // 100
            if old_dial:
                part2_password += 1

        dial %= 100

        if not dial:
            part1_password += 1

    print(f"Dial at the end: {dial}")
    print(f"Part 1 password: {part1_password}")
    print(f"Part 2 password: {part2_password}")


if __name__ == "__main__":
    main()
