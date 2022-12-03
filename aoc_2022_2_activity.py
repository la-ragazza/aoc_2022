inp = []

with open('aoc_2022_2_input.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split(' ')
        inp.append(line)

print(inp)

# Part 1: calculate my total score if I follow the strategy guide and 'X' = rock, 'Y' - paper & 'Z' = scissors

# calculate points awarded where rock = 1, paper = 2, scissors = 3
def sum_shape(guide):
    score = 0

    for item in guide:
        shape = item[1]
        match shape:
            case 'X':
                score += 1
            case 'Y':
                score += 2
            case 'Z':
                score += 3
            case _:
                print('Error: input ' + shape + ' not matched.')
    
    return score

# calculate points for win/lose/draw (6/0/3))
def sum_wld(guide):
    score = 0
    wins = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
    losses = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]
    draws = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]

    for item in guide:
        if item in wins:
            # print('Win!')
            score += 6
        elif item in losses:
            continue
        elif item in draws:
            # print('Draw!')
            score += 3
        else:
            print('Item ' + item + ' not matched.')
    
    return score

# get total of above scores
def sum_score():
    shape = sum_shape(inp)
    wld = sum_wld(inp)

    total = shape + wld

    print('Shape score: ' + str(shape))
    print('W/L/D score: ' + str(wld))

    return total

print(sum_score())


# Part 2: Calculate score if 'X' = lose, 'Y' = draw & 'Z' = win

# get score for W/L/D (6/0/3)
def wld_score(guide):
    score = 0

    # 'X' = lose, 'Y' = draw, 'Z' = win

    for item in guide:
        strategy = item[1]

        match strategy:
            case 'X':
                continue
            case 'Y':
                score += 3
            case 'Z':
                score += 6
            case _:
                print('Error: strategy ' + strategy + ' not matched.')
    
    return score

# take opponent moves, calculate W/L/D option for each, and add points for corresponding shape to score
def get_shape(guide):
    score = 0
    
    # W/L/D for each opponent choice
    # rock = 1, paper = 2, scissors = 3
    rock = [2, 3, 1]
    paper = [3, 1, 2]
    scissors = [1, 2, 3]

    for item in guide:
        opp = item[0]
        me = item[1]
        
        match me:
            case 'X': # lose
                match opp:
                    case 'A':
                        score += rock[1]
                    case 'B':
                        score += paper[1]
                    case 'C':
                        score += scissors[1]
                    case _:
                        print('Opponent choice ' + opp + ' not matched. Cannot calculate loss.')
            case 'Y': # draw
                match opp:
                    case 'A':
                        score += rock[2]
                    case 'B':
                        score += paper[2]
                    case 'C':
                        score += scissors[2]
                    case _:
                        print('Opponent choice ' + opp + ' not matched. Cannot calculate draw.')
            case 'Z': # win
                match opp:
                    case 'A':
                        score += rock[0]
                    case 'B':
                        score += paper[0]
                    case 'C':
                        score += scissors[0]
                    case _:
                        print('Opponent choice ' + opp + ' not matched. Cannot calculate win.')
            case _:
                print('Your strategy ' + me + ' not matched. Should be X, Y, or Z.')
    
    return score


# calculate total score

def get_score():
    wld = wld_score(inp)
    shape = get_shape(inp)

    total = wld + shape

    print('Shape score: ' + str(shape))
    print('W/L/D score: ' + str(wld))

    return total

print(get_score())

