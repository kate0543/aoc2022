import time

start = time.perf_counter()

def elves():
    elf = 0
    with open("adventofcode.com_2022_day_1_input.txt") as file:
        for line in file:
            line = line.replace('\n', '')
            if line:
                line = int(line)
                elf += line
            else:
                yield elf
                elf = 0
        yield elf


first = 0
second = 0
third = 0
for calories in elves():
    if calories > third:
        third = calories
        if third > second:
            third, second = second, third
            if second > first:
                first, second = second, first
print(first)
print(first + second + third)

print(time.perf_counter() - start)

