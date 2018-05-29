"Author: James Hakan Nell"
"This is a sudoku solver program"

def read_sudoku(file): #reads in sudoku problem from notepad text file.
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))

def convertToSets(problem): #returns a list of the problems, but as a list containing sets and sets with all possible values for each position.
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if problem[i][j] in range(1,10):
                problem[i][j] = {problem[i][j]}
            else:
                problem[i][j] = set(range(1,10))
    return problem


def convertToInts(problem): #need to add to make sure no empty value thingy #converts list of sets back to list of integers.
    problem = list(problem)
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if len(problem[i][j]) == 1:
                if 1 in problem[i][j]: problem[i][j] = 1
                elif 2 in problem[i][j]: problem[i][j] = 2
                elif 3 in problem[i][j]: problem[i][j] = 3
                elif 4 in problem[i][j]: problem[i][j] = 4
                elif 5 in problem[i][j]: problem[i][j] = 5
                elif 6 in problem[i][j]: problem[i][j] = 6
                elif 7 in problem[i][j]: problem[i][j] = 7
                elif 8 in problem[i][j]: problem[i][j] = 8
                elif 9 in problem[i][j]: problem[i][j] = 9
            else:
                problem[i][j] = 0
    return problem


def getRowLocations(rowNumber): #returns list of all nine row locations in row,column tuple format.
    b = []
    for i in range(9):
        b.append((rowNumber, i))
    return b

def getColumnLocations(columnNumber): #returns list of all nine column locations in row,column tuple format.
    b = []
    for i in range(9):
        b.append((i, columnNumber))
    return b

def getBoxLocations(location): #Returns a list of all nine locations as tuples in the same box as the given location.
    grid1 = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    grid2 = [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]
    grid3 = [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)]
    grid4 = [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)]
    grid5 = [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)]
    grid6 = [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)]
    grid7 = [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)]
    grid8 = [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)]
    grid9 = [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]
    if location in grid1: return grid1
    elif location in grid2: return grid2
    elif location in grid3: return grid3
    elif location in grid4: return grid4
    elif location in grid5: return grid5
    elif location in grid6: return grid6
    elif location in grid7: return grid7
    elif location in grid8: return grid8
    elif location in grid9: return grid9



def eliminate(problem, location, listOfLocations):#
    count = 0
    s = (problem[location[0]][location[1]].pop())
    problem[location[0]][location[1]] = {s}
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if (i,j) in listOfLocations and (i,j) != location:
                if s in problem[i][j]:
                    (problem[i][j]).discard(s),
                    count += 1
    return count

def isSolved(problem): #Returns true if all elements of the problem array contain only one element/value
    if all(len(problem[i][j]) == 1 for i in range(len(problem)) for j in range(len(problem[i]))):
        return True
    else:
        return False


def solve(problem): #Given an nxn array, this function solves the sudoku puzzle and changes the original array. Returns Boolean
    while not isSolved(problem):
        count = 0
        for i in range(len(problem)):
            for j in range(len(problem[i])):
                location = (i,j)
                if len(problem[i][j]) == 1:
                    count += eliminate(problem, location, getRowLocations(i))
                    count += eliminate(problem, location, getBoxLocations(location))
                    count += eliminate(problem, location, getColumnLocations(j))
        if count == 0:
            return False
            print("This puzzle cannot be solved")
    return True



def print_sudoku(problem): #Prints Sudoku Function for user.
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            print(problem[i][j], end=' ')
        print()


def ask_play_again(prompt1):
    prompt1 = 0
    prompt1 = input("Would you like to load another puzzle ? Enter 'Y' or 'y' to to load again, or N/n not to: ")
    while prompt1 not in ["y","Y","N","n"]: prompt1 = input("That is not a correct input. Please enter again, you must enter either Y/y or N/n:")
    else:
        if prompt1 in ["y","Y"]: return True
        elif prompt1 in ["N","n"]: return False


def main():
    prompt1 = True #Declaring Boolean variable to use as loop, so user can load game again if they wish to.
    while prompt1 == True:
        print("Welcome to my Sudoku Puzzle Solver")
        prompt = input("Please input a path to your sudoku text file:")
        problem = read_sudoku(prompt)
        #try:
#           prompt = input("Please input a path to your sudoku text file:")
#            problem = read_sudoku(prompt)
        #except Exception:
        #print("Either cannot use or find this file")
        print()
        print("Here is the Sudoku Problem you have Loaded:")
        print()
        print_sudoku(problem)
        convertToSets(problem)
        print()
        if solve(problem) is False:
            print("This problem could not be solved. Please see the program's attempt below:")
        else:
            print("Please find the Sudoku Puzzle's Solution below:")
        print()
        convertToInts(problem)
        print_sudoku(problem)
        print()
        ask_play_again(prompt1)


if __name__ == "__main__":
    main()
