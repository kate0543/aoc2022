def to_priority(character: str) -> int:
    if character.islower():
        return ord(character) - ord('a') + 1
    return ord(character) - ord('A') + 27


def get_common_item(compartment_1: str, compartment_2: str) -> str:
    common_item = set(compartment_1) & set(compartment_2)
    assert len(common_item) == 1
    common_item, = common_item  # get only item in set
    return common_item


def get_compartments(rucksack: str) -> tuple[str, str]:
    rucksack = rucksack.strip()
    compartment_size = len(rucksack) // 2
    return rucksack[:compartment_size], rucksack[compartment_size:]


with open("adventofcode.com_2022_day_3_input.txt") as file:
    total = 0
    for line in file:
        compartment_1, compartment_2 = get_compartments(line)
        common_item = get_common_item(compartment_1, compartment_2)
        total += to_priority(common_item)
    print('total_priority', '=', total)
