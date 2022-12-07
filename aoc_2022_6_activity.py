inp = ""

with open('aoc_2022_6_input.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        inp += line


# Part 1: find the index of the final element in the first set of 4 non-repeating characters in the string
# Part 2: the same thing but for 14 non-repeating characters

def get_marker_end(my_string, packet_size):

    for i in range(0, len(my_string)):
        my_set = set(my_string[i:i+packet_size])
        # print(my_set)
        if len(my_set) == packet_size:
            print('Set found!')
            print(my_set)
            return i + packet_size

print(get_marker_end(inp, 4)) # Part 6.1
print(get_marker_end(inp, 14)) # Part 6.2
            