inp = []

with open('aoc_2022_4_input.txt', encoding='utf-8') as f:
    for line in f:
        new_line = []
        line = line.strip()
        line = line.split(',')
        for item in line:
            item = item.split('-')
            item[0] = int(item[0])
            item[1] = int(item[1])
            new_line.append(item)
        inp.append(new_line)


# Part 1: Find in how many assignment pairs one range fully contains the other

# Take an assignment pair and find which has the largest value range
# Data in format [[a, b], [c, d]]
def find_largest_range(pair):
    range_a = pair[0][1] - pair[0][0]
    range_b = pair[1][1] - pair[1][0]

    if range_a > range_b:
        return [pair[0], pair[1]]
    elif range_b > range_a:
        return [pair[1], pair[0]]
    elif range_a == range_b:
        return [pair[0], pair[1]]

def count_contained_ranges(assignments):
    count = 0

    for i in assignments:
        pair = find_largest_range(i)
        if pair[0] == pair[1]:
            #print('These are the same:')
            #print(pair)
            count += 1
        else: 
            large_range = pair[0] # [a, b]]
            small_range = pair[1] # [c, d]
            if small_range[0] >= large_range[0] and small_range[1] <= large_range[1]:
                #print('Contained assignment found: ')
                #print(pair)
                count += 1
            else:
                continue
    
    return count

print(count_contained_ranges(inp))


# Part 2: Find the total of assigned pairs with any overlap

def count_overlap(assignments):
    count = 0

    for i in assignments:
        pair = find_largest_range(i) # [[a, b], [c, d]]
        if pair[1][0] >= pair[0][0] and pair[1][0] <= pair[0][1]:
            count += 1
        elif pair[1][1] <= pair[0][1] and pair[1][1] >= pair[0][0]:
            count +=1
        elif pair[1][0] < pair[0][0] and pair[1][1] < pair[0][0]:
            print('No overlap - second range lower than first')
            print(pair)
        elif pair[1][0] > pair[0][1] and pair[1][1] > pair[0][1]:
            print('No overlap - second range higher than first')
            print(pair)
        else:
            print('Not sure what\'s going on here')
            print(pair)

    return count

print(count_overlap(inp))