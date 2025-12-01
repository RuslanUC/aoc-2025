def main() -> None:
    with open("input-day-1.txt") as f:
        rotations = f.read().splitlines(False)

    part1_password = 0
    part2_password = 0

    dial = 50

    for rot in rotations:
        print(f"{rot} = ", end="")
        dist = int(rot[1:])
        old_dial = dial
        print(f"{dial} -> ", end="")
        if rot[0] == "L":
            dial -= dist
        else:
            dial += dist
        print(f"{dial}", end="")

        part2_password_old = part2_password

        if dial >= 100:
            part2_password += dial // 100
            print(f", +{dial // 100}", end="")
        elif dial <= 0:
            part2_password += -dial // 100
            if old_dial:
                part2_password += 1
            print(f", +{-dial // 100 + 1}", end="")

        print()

        old_dial = dial
        dial %= 100

        if old_dial != dial and part2_password == part2_password_old:
            print("WHAT")

        if not dial:
            part1_password += 1

    print(f"Dial at the end: {dial}")
    print(f"Part 1 password: {part1_password}")
    print(f"Part 2 password: {part2_password}")


if __name__ == "__main__":
    main()
