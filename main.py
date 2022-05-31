# Johann Reyes
# Dec 7, 2020
# Purpose: This is a game that uses a table of digits as the players game board. The player must change the digits so that the sums of all columns and rows are even to win. The player may choose to play solo or against an AI and depending on which board the player chooses the game will vary i.e. # of turns, digits ect. Points are added/subtracted cumulative and the player may play multiple times. Also as a last feature, at the end of the game the program will take the list of sums from both rows and columns to generate a coloured image depending on the numbers in the list.

import createBoardImages as c

print("\n")
name = input("Hello there! What is your name?: ")
c.opening(name)

play = True #condition for gaming
gameCounter = 0 #game counter
points = 0  #points counter

check = True
while check == True:
  answ = input("\nWould you like to play? (y/n): ").lower().strip("!@#$%^&*()_+ ")
  if(answ=="y" or answ=="n"):
    check = False
  else:
    print("Answer is invalid. Please re-enter")

if(answ=="n"):
  print("See you next time!")
else:
  while play == True:
    gameCounter+=1
    print("\nGame "+str(gameCounter)+"\n")

    check = True #checks if inputs are valid
    while check == True:
      answ = input("How would you like to play? (Solo/AI): ").lower().strip("!@#$%^&*()_+ ")
      if(answ=="solo" or answ=="ai"):
        check = False
      else:
        print("Answer is invalid. Please re-enter")

    check = True
    while check == True:
      board = input("Which board would you like? (1,2,3): ").lower().strip("!@#$%^&*()_+ ")
      if(board == ""):
        print("Answer is invalid. Please re-enter")
      elif(1<=int(board)<=3):
        check = False
      else:
        print("Answer is invalid. Please re-enter")

    board= c.createBoard(int(board))
    dimension = int(len(board))
    nTurns = dimension * dimension
    print("\nBoard:\n")
    c.showBoard(board)

    if(answ == "ai"):
      check = True
      while check == True:
        turnOpt = input("Since you have chosen to battle the AI, would you like more number of turns? (y/n): ").lower().strip("!@#$%^&*()_+ ")
        if(turnOpt=="y" or turnOpt=="n"):
          if(turnOpt=="y"):
            check2 = True
            while check2 == True:
              turns = input("You now have more turns. How many turns would you like? (1-"+str(nTurns-1)+"): ").strip("!@#$%^&*()_+ ")
              if(turns == ""):
                print("Answer is invalid. Please re-enter")
              elif(0<=int(turns)<=nTurns-1):
                check2=False
              else:
                print("Answer is invalid. Please re-enter")
          else:
            check2 = True
            while check2 == True:
              turns = input("How many turns would you like? (1-"+str(int(dimension)-1)+"): ").strip("!@#$%^&*()_+ ")
              if(turns == ""):
                print("Answer is invalid. Please re-enter")
              elif(0<=int(turns)<=int(dimension)-1):
                check2 = False
              else:
                print("Answer is invalid. Please re-enter")
          check = False
        else:
          print("Answer is invalid. Please re-enter")
    else:
      check = True
      while check == True:
        turns = input("How many turns would you like? (1-"+str(int(dimension)-1)+"): ").strip("!@#$%^&*()_+ ")
        if(turns == ""):
          print("Answer is invalid. Please re-enter")
        elif(0<=int(turns)<=int(dimension)-1):
          check = False
        else:
          print("Answer is invalid. Please re-enter")
    print("\n")

    turnCycle = int(turns)
    turnCounter = 1
    turnUsed = 0
    turnCheck = True
    while turnCheck == True:
      if(turnCycle==0):
        turnCheck = False
      else:
        print("Turn: "+str(turnCounter))
        if(answ=="ai"):
          print("\nIt's your turn!")
        print("\nWhere would you like your digit? (-1 if you want no more turns)")
        check = True
        while check == True:
          row = input("Row# (0-"+str(dimension-1)+"): ").strip("!@#$%^&*()_+ ")
          col = input("Col# (0-"+str(dimension-1)+"): ").strip("!@#$%^&*()_+ ")
          if(row == "" or col == ""):
            print("Answer is invalid. Please re-enter")
          elif(-1<=int(row)<=int(dimension)-1 and -1<=int(col)<=int(dimension)-1 ):
            check = False
          else:
            print("Answer is invalid. Please re-enter")
        
        if(int(row)>=0):
          check = True
          while check == True:
            num = input("Digit: ").strip("!@#$%^&*()_+ ")
            if(num == ""):
              print("Answer is invalid. Please re-enter")
            elif(0<=int(num)<=9):
              check = False
            else:
              print("Answer is invalid. Please re-enter")
          board = c.changeBoard(board,num,row,col)
          print("\nBoard:\n")
          c.showBoard(board)
          turnUsed+=1
        elif(int(row)==-1):
          turnCheck = False

        if(answ == "ai" and int(row)!=-1):
          print("AI's turn:\n")
          input("Press enter to continue...")
          board = c.ai(board)
          print("\nBoard:\n")
          c.showBoard(board)
        
        turnCycle-=1
        turnCounter+=1
        if(turnCycle<=0):
          turnCheck = False
    
    print("\nYou have used all your turns. Game is over!")
    print("\nGame Results:\n")

    finalLine = c.totalCol(board)
    finalColum = c.totalRow(board)

    print("Sum of all colums, Final Line: ["+str(finalLine)[1:-1]+"]")
    print("Sum of all rows, Final Column: ["+str(finalColum)[1:-1]+"]")

    gainedPoints = c.calcPoints(finalColum,finalLine,turnUsed)

    outcome = c.outcome(finalColum,finalLine)
    if(outcome==True):
      print("\nYou Win! All numbers in the final line and column are even!")
      print("You will be added "+str(gainedPoints)+" points!")
      points+=int(gainedPoints)
    else:
      print("\nYou Lost! Not all numbers in the final line and column are even.")
      print("You will be subtracted "+str(gainedPoints)+" points.")
      points-=int(gainedPoints)

    print("\nPoints so far: "+str(points))

    print("\nIn preparation for the images for the final line and column...")
    check = True
    while check == True:
      pix = input("How many pixels (columns) would you like per square? (40-60): ").strip("!@#$%^&*()_+ ")
      if(pix == ""):
        print("Answer is invalid. Please re-enter")
      elif(int(pix)<40):
        print("Pixels entered is too small. Please re-enter.")
      elif(int(pix)>60):
        print("Pixels entered is too big. Please re-enter.")
      else:
        check = False

    input("Press enter to continue...")
    c.FinalLineImage(finalLine,pix,board)
    input("Press enter to continue...")
    c.FinalColImage(finalColum,pix,board)

    check = True
    while check == True:
      answ = input("\nWould you like to keep playing? (y/n): ").lower().strip("!@#$%^&*()_+ ")
      if(answ=="y" or answ=="n"):
        check = False
      else:
        print("Answer is invalid. Please re-enter")

    if(answ=="n"):
      play = False
      print("\nThanks for playing! See you next time!")