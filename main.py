calories = []

with open("adventofcode.com_2022_day_1_input.txt") as file:
    elves = []
    elf = []
    calories=[]
    for line in file:
        line = line.replace('\n', '')
        if line:
            line=int(line)
            elf.append(line)
        else:
            calories.append(sum(elf))
            elves.append(elf)
            elf = []

    print(max(calories))
