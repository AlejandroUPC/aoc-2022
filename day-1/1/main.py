import typing as tp


def main() -> tp.NoReturn:
    elf_total = []
    local_cter = 0
    with open("day-1/2/input.txt", "r") as fr:
        elf_calories = fr.read().splitlines()
    for fruit in elf_calories:
        if fruit:
            local_cter += int(fruit)
        else:
            elf_total.append(local_cter)
            local_cter = 0
    print(sum(list(sorted(elf_total)[-3:])))


if __name__ == "__main__":
    main()
