inp = []

with open('aoc_2022_1_input.txt', encoding='utf-8') as f:
    item = []
    for line in f:
        # print(len(line))
        if len(line) > 1:
            line = line.strip()
            line = line.split(' ')
            line = int(line[0])
            item.append(line)
        else:
            inp.append(item)
            item = []
    inp.append(item)


# Part 1: Calculate the highest number of calories carried by any elf

def count_cals(supplies):
    highest_calories = 0

    for set in supplies:
        count = 0

        for item in set:
            count += item
        
        if count > highest_calories:
            highest_calories = count
    
    return highest_calories

print(count_cals(inp))


# Part 2: Calculate the total of the top 3 highest calories carried by elves

def top_three_calories(supplies):
    total_calories = []

    for set in supplies:
        count = 0

        for item in set:
            count += item
        
        total_calories.append(count)
    
    
    total_calories.sort(reverse=True)
    
    total = total_calories[0] + total_calories[1] + total_calories[2]

    return total
    

print(top_three_calories(inp))
    

