from enum import Enum
import string


def get_priorities(same_items: list):
    item_priority_value = []
    for i in range(53):
        item_priority_value.append(i)
    item_priority_value = item_priority_value[1:]
    alphabets_keys = list(string.ascii_letters)
    item_priority_dict = dict(zip(alphabets_keys, item_priority_value))
    priorities = []
    for item in same_items:
        priority = item_priority_dict[item]
        priorities.append(priority) 
    return sum(priorities)


def get_same_item(compartments: list):
    compartment_1, compartment_2 = compartments
    # print(compartment_1,compartment_2)
    same_items = []
    for item in compartment_1:
        if item in compartment_2:
            if item not in same_items:
                same_items.append(item)
    return same_items


def get_compartments(line_str: str):
    rucksack = line_str.strip()
    compartment_size = len(rucksack) // 2
    compartment_1 = rucksack[0:compartment_size]
    compartment_2 = rucksack[compartment_size:]
    compartments = [compartment_1, compartment_2]
    return compartments


with open("adventofcode.com_2022_day_3_input.txt") as file:
    same_items = []
    for line in file:
        compartments = get_compartments(line)
        same_items.extend(get_same_item(compartments))
    # print(len(same_items),' number of same items:',same_items)
    total_priority = get_priorities(same_items)
    print('total_priority', '=', total_priority)
