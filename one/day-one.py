def open_input_file():
    inputFile = open("input.txt", "r")
    inputString = inputFile.read()
    inputFile.close()
    return inputString.split('\n\n')

def find_highest_num_total(inputList):
    total = 0
    totalList = []

    for section in inputList:
        numList = section.split('\n')
        for num in numList:
            total += int(num)
        totalList.append(total)
        total = 0
        
    totalList.sort(reverse=True)
    print('Highest Total: ' + str(totalList[0]))
    print('Second Highest: ' + str(totalList[1]))
    print('Third Highest: ' + str(totalList[2]))
    print('Total of those three elves: ' + str(totalList[0] + totalList[1] + totalList[2]))

def main():
    inputList = open_input_file()
    find_highest_num_total(inputList)

main()