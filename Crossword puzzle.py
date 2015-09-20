import sys



def main():

    guessedwords = 0
    acrosswords = 0
    gameover = False

    # Call function readPuzzle() to read data file into puzzle object

    puzzle = readPuzzle()

    #Count the number of word going across

    for i in puzzle:
        if( puzzle[i]["direction"] == "A" ):
            acrosswords += 1

    
    # Create 15 x 15 game grid, initially filled with blocks ('*')
    
    grid = createGrid(puzzle)

   
    # Iterate through every word in the puzzle, adding each word to the grid

    # Print the fully-populated grid to the console
    
    printGrid(puzzle, grid)

    while( not gameover ):

        
        print("(G) Guess Word, (C) Show Clue, (R) Show Grid, (Q) Quit")

        choice = input("Your choice?: ").upper()
        
        if( choice == "G" ):
            
            box = input("Please enter the box number: ").upper()
            direction = input("Please enter the direction: ").upper()
            guess = input("Guess a word: ").upper()

            worddict = findWord(puzzle, box, direction)

            if( worddict == None ):
                print("The guess is not in the selected box\direction.")
            else:
                if(worddict["word"] == guess):
                    guessedwords += 1
                    addWordToGrid(worddict, grid)
                    print("\nYour guess was correct!")

                    if( acrosswords == guessedwords ):
                        print("Congratulations, you won the crossword puzzle and guessed all the words!\n")
                        gameover = True


                else:
                    print("Your guess was incorrect.")


        elif( choice == "C" ):
            box = input("Please enter the box number: ").upper()
            direction = input("Please enter the direction: ").upper()

            worddict = findWord( puzzle, box, direction)
            
            if( type(worddict) == dict ):

                print("The clue is: " + worddict["clue"] )

            else:

                print(" There is no word at the given box and direction." )
        
        elif( choice == "R" ):

            printGrid(puzzle, grid)

        elif( choice == "Q" ):

            print("You correctly guessed " + str(guessedwords) + " word(s) in the puzzle!")
            gameover = True
        
        else:
            print ("I do not recognize your choice! Please try again.")                

    # Pause before exiting the program

    input('Press ENTER to exit program. ')



def readPuzzle():

    #
    # READ THE PUZZLE DATA FILE INTO A DICTIONARY
    #

    # This function should: open the data file, read each line (representing a
    # word), split each line into a list (representing the properties of the
    # word), store these properties into a dictionary with sensible key names,
    # and add these dictionaries into the main dictionary 'puzzle', using the
    # word as the key name.  Finally, return the 'puzzle' dictionary to the
    # caller.


    # INSERT YOUR CODE HERE

    inputfile = open( 'E:\\Python\Project #2\puzzle.csv' )
    line = inputfile.readline()


    wordlist = {}

    while( len(line) > 0 ):
        line = line.strip()
        line = line.split("\t")

        newdict = {}
        newdict["y"] = line[0]
        newdict["x"] = line[1]
        newdict["box"] = line[2]
        newdict["direction"] = line[3]
        newdict["word"] = line[4]
        newdict["clue"] = line[5]

        wordlist[line[4]] = newdict

        line = inputfile.readline()


    return wordlist



def addWordToGrid(newword, grid):

    #
    # ADD A WORD TO THE GRID
    #

    # This function should: accept a word dictionary ('newword') and the grid
    # object ('grid') as arguments, and add each letter of 'newword', one by
    # one, into the correct squares of the grid, replacing any letters or
    # blocks already in these squares.  (Remember that the word dictionary
    # includes all of the properties of the word, including the X and Y
    # coordinates of the first letter of the word and each letter of the word.
    # You can use this information to determine the correct square for every
    # letter of the word.)  This function does not have to return a value to
    # the caller.

    # INSERT YOUR CODE HERE (and remove the "pass" statement in the next line)


    word = newword["word"]
    direction = newword["direction"]
    x = int( newword["x"] )
    y = int( newword["y"] )
    
    for i in word:
        grid[y][x] = i
        if( direction == "A" ):
             x += 1
        elif (direction == "D"):
             y += 1


def createGrid(puzzle):
    
    # CREATE A NEW GRID, FILLED WITH BLOCKS
    grid = [['*' for x in range(15)] for x in range(15)]
    #LOOP THROUHG ALL WORDS IN THE PUZZLE
    for i in puzzle:
        # GET INFORMATION ABOUT THE NEXT WORD
        word = puzzle[i]["word"]
        x = int( puzzle[i]["x"] )
        y = int( puzzle[i]["y"] )
        direction = puzzle[i]["direction"]

        # LOOP THROUGH EACH LETTER OF THE NEXT WORD
        for j in word:
            # PUT AN EMPTY SPACE IN THE GRID
            grid[y][x] = " "
            # MOVE ON TO THE NEXT LETTER
            if ( direction == "A" ):
                x += 1
            elif (direction == "D" ):
                y += 1
    return grid


def findWord(puzzle, box, direction):
    
    # LOOP THROUGH ALL WORD IN THE DICTIONARY

    for i in puzzle:

        # GET DICTIONARY FOR NEXT WORD

        newword = puzzle[i]

        # GET DIRECTION AND BOX NUMBER FROM DICTIONARY

        newworddirection = newword["direction"]
        newwordbox = newword["box"]

        if(( newworddirection == direction ) and ( newwordbox == box )):
            return newword

    return None

            
def printGrid(puzzle, grid):

    #
    # PRINT THE GAME GRID TO THE CONSOLE
    #

    # Begin by creating a new two-dimensional array for the box numbers
    
    boxnumbers = [[0 for x in range(15)] for x in range(15)]

    # Next, loop through all the words in the puzzle to get the box numbers

    for i in puzzle:

        # Get the next word in the puzzle

        nextword = puzzle[i];

        # Retrieve the X and Y of the first letter, along with the box number

        x = int(nextword['x'])
        y = int(nextword['y'])
        box = int(nextword['box'])

        # Add the box number to the array

        boxnumbers[y][x] = box

    # Now, print the grid to the console

    for y in range(0,15):

        # Print the top border of the next row, box by box

        for x in range(0, 15):

            # If there is no box number on this box, print an empty top

            if ( boxnumbers[y][x] == 0 ):
                sys.stdout.write('+---')

            # If there is a single-digit box number, print it in the center
            
            elif ( boxnumbers[y][x] < 10 ):
                sys.stdout.write('+-' + str(boxnumbers[y][x]) + '-')

            # If there is a double-digit box number, print it at the left edge
                
            elif ( boxnumbers[y][x] >= 10 ):
                sys.stdout.write('+' + str(boxnumbers[y][x]) + '-')

        # End the top border and begin printing the next row
        
        sys.stdout.write('+\n|')

        # Print the next row, box by box, padding each letter with spaces

        for x in range(0,15):

            sys.stdout.write(' ' + grid[y][x] + ' |')

        print()

    # Print the bottom border for the grid

    print('+' + '---+' * 15)

    

main()
