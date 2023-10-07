# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

opponent_move = []
your_move = []
expect_move = []

round_score = []
expect_score = []


def get_score(opponent, you):
    base_score = 0
    score = 0
    # rock
    if you == 'X':
        base_score = 1
        # rock
        if opponent == 'A':
            score = 3
        # paper
        elif opponent == 'B':
            score = 0
            # scissors
        elif opponent == 'C':
            score = 6
    # paper
    elif you == 'Y':
        base_score = 2
        # rock
        if opponent == 'A':
            score = 6
        # paper
        elif opponent == 'B':
            score = 3
            # scissors
        elif opponent == 'C':
            score = 0
    # scissors
    elif you == 'Z':
        base_score = 3
        # rock
        if opponent == 'A':
            score = 0
        # paper
        elif opponent == 'B':
            score = 6
            # scissors
        elif opponent == 'C':
            score = 3
    return score + base_score


def get_expect_score (opponent, result):
    #     x- lose, y - draw, z - win
    you = ''

    #     lose
    if result == 'X':
        if opponent == 'A':
            you = 'Z'
        elif opponent == 'B':
            you = 'X'
        elif opponent =='C':
            you = 'Y'
    #         draw
    elif result == 'Y':
        if opponent == 'A':
            you = 'X'
        elif opponent == 'B':
            you = 'Y'
        elif opponent =='C':
            you = 'Z'
    #         win
    elif result == 'Z':
        if opponent == 'A':
            you = 'Y'
        elif opponent == 'B':
            you = 'Z'
        elif opponent =='C':
            you = 'X'
    return get_score(opponent,you)


with open("adventofcode.com_2022_day_2_input.txt") as file:
    for line in file:
        line_list = line.strip().split(' ')
        opponent_move.append(line_list[0])
        your_move.append(line_list[1])
        round_score.append(get_score(opponent_move[-1], your_move[-1]))
        # print(opponent_move[-1], your_move[-1], round_score[-1])

print(sum(round_score))

with open("adventofcode.com_2022_day_2_input.txt") as file:
    for line in file:
        line_list = line.strip().split(' ')
        opponent_move.append(line_list[0])
        expect_move.append(line_list[1])
        expect_score.append(get_expect_score(opponent_move[-1], expect_move[-1]))
        # print(opponent_move[-1], expect_move[-1], expect_score[-1])

print(sum(expect_score))