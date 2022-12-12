def open_input_file():
    inputFile = open("input.txt", "r")
    inputString = inputFile.read()
    inputFile.close()
    return inputString

def eval_a(playerMove):
    if (playerMove == 'X'):
        return 4
    elif(playerMove == 'Y'):
        return 8
    return 3

def eval_b(playerMove):
    if (playerMove == 'X'):
        return 1
    elif(playerMove == 'Y'):
        return 5
    return 9

def eval_c(playerMove):
    if (playerMove == 'X'):
        return 7
    elif(playerMove == 'Y'):
        return 2
    return 6

def part_one(inputString):
    for game in inputString.split('\n'):
        playerMove = game.split(' ')[1]
        switch={
            'A': eval_a(playerMove),
            'B': eval_b(playerMove),
            'C': eval_c(playerMove),
        }
        total += switch.get(game.split(' ')[0])
    print('Part 1 Total score: ' + str(total))

def part_two(inputString):
    for game in inputString.split('\n'):
        playerMove = game.split(' ')[1]
        switch={
            'A': eval_a(playerMove),
            'B': eval_b(playerMove),
            'C': eval_c(playerMove),
        }
        total += switch.get(game.split(' ')[0])
    print('Part 2 Total score: ' + str(total))

def main():
    inputString = open_input_file()
    part_one(inputString)
    part_two(inputString)
    

main()