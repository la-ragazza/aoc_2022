inp = []

with open('aoc_2022_3_input.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        inp.append(line)


# Part 1: Find the incorrect item in each rucksack, and the sum of all their priority values

# Divide each rucksack into 2 compartments ()
def divide_rucksack(pack):
    midpoint = int(len(pack) / 2)

    first_compartment = pack[0:midpoint]
    second_compartment = pack[midpoint:]

    return [first_compartment, second_compartment]


# Find incorrectly packed items and push to array
def get_items(packs):
    mispacked = []
    
    for pack in packs:
        count = 0
        divided_pack = divide_rucksack(pack)
        for item in divided_pack[0]:
            if item in divided_pack[1]:
                if count == 0:
                    mispacked.append(item)
                    count += 1
                else:
                    if item == mispacked[-1]:
                        print('Found 2 of item type ' + item + ' in ' + divided_pack[0])
                    else:
                        print('Error: conflict with ' + item + ' and ' + mispacked[-1])
    
    # print(len(mispacked))

    return mispacked

# Total priority values for each mispacked item type
def calculate_priorities(item_types):
    priorities = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = 0

    for item_type in item_types:
        priority_value = priorities.index(item_type)
        # print('Type: ' + item_type + ', Priority value: ' + str(priority_value))
        value += priority_value

    return value

packed_items = get_items(inp)

print(calculate_priorities(packed_items))


# Part 2: Get badge (common item) for each group of 3, and calculate the priority values for all badges

# Group rucksacks into groups of three
def group_in_threes(packs):
    grouped_packs = []
    current_group = []

    for pack in packs:
        if len(current_group) == 3:
            grouped_packs.append(current_group)
            current_group = [pack]
        elif len(current_group) < 3:
            current_group.append(pack)
        elif len(current_group) > 3:
            print('Error: current group too large:')
            print(current_group)
    
    if len(current_group) > 0:
        grouped_packs.append(current_group)
    
    # print(len(grouped_packs))

    return grouped_packs

# Find badge type in each group
def get_badge_type():
    groups = group_in_threes(inp)
    item_types = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    badges = []

    for group in groups:
        for i in item_types:
            if i in group[0] and i in group[1] and i in group[2]:
                badges.append(i)
    
    print(len(badges))

    return badges

# Calculate priority values for badges using calculate_priorities function

badge_list = get_badge_type()
print(calculate_priorities(badge_list))

