instructions = []

# Stacks 1-9 Ordered from bottom of stack to top
crates =[['H', 'C', 'R'], ['B', 'J', 'H', 'L', 'S', 'F'], ['R', 'M', 'D', 'H', 'J', 'T', 'Q'], ['S', 'G', 'R', 'H', 'Z', 'B', 'J'], 
['R', 'P', 'F', 'Z', 'T', 'D', 'C', 'B'], ['T', 'H', 'C', 'G'], ['S', 'N', 'V', 'Z', 'B', 'P', 'W', 'L'], ['R', 'J', 'Q', 'G', 'C'], 
['L', 'D', 'T', 'R', 'H', 'P', 'F', 'S']]

with open('aoc_2022_5_input.txt', encoding='utf-8') as f:
    for line in f:
        if 'move' in line:
            line = line.strip()
            line = line.split(' ')
            instruction = {'move': int(line[1]), 'from': int(line[3]), 'to': int(line[5])}
            instructions.append(instruction)


# Part 1: Find which crates are at the top of each stack after the rearrangement procedure

# 1. Feed instructions into move function - remove last element and append to new list
def move_crates(stacks, step):
    count = step['move']
    start = step['from'] - 1
    target = step['to'] - 1

    while count > 0:
        move = stacks[start].pop()
        stacks[target].append(move)
        count -= 1
    
    return stacks

# 2. Return updated crate stacks
def follow_steps(crate_stacks, steps):

    for item in steps:
        crate_stacks = move_crates(crate_stacks, item)
    
    return crate_stacks

# 3. Get string of final elements in each list
def get_top_crates(stacks):
    top_crates = ''

    for stack in stacks:
        top_crates += stack[-1]
    
    return top_crates

#new_stacks = follow_steps(crates, instructions)
#print(new_stacks)
#print(get_top_crates(new_stacks))


# Part 2: Get top crate of each stack when all crates are moved in one go for each step

def move_all_crates(stacks, step):
    stack_count = step['move']
    start = step['from'] - 1
    target = step['to'] - 1

    move_stack = stacks[start][-stack_count:]
    while len(move_stack) > 0:
        move = move_stack.pop(0)
        crates[target].append(move)

    del stacks[start][-stack_count:]

    return stacks

def follow_new_steps(crate_stacks, steps):
    
    for item in steps:
        crate_stacks = move_all_crates(crate_stacks, item)
    
    return crate_stacks

rearranged_stacks = follow_new_steps(crates, instructions)
print(rearranged_stacks)
print(get_top_crates(rearranged_stacks))
