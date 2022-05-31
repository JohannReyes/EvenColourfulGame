import random as r
import cmpt120imageWeek9 as image

def opening(name):
  print("\nHello "+name+"! Welcome to the Even Colourful Game!\n")

  print("With this system you will be able to play as many games as you want!\nThe objective of this game is that all columns and rows in the board add to an even number.\n")

  print("For each game:\n- you will be able to choose to play 'solo' or against the computer ('AI')\n- you will be able to choose an initial board\n- at the end of each game you will win (or lose) points\n- you will see a colorful representation of the game final board results\nHave Fun!")

def createBoard(id):
  if(id==1):
    file = open("board1.csv")
    firstLine = file.readline()
    b = []
    for data in file:
      board = data.split(",")
      b.append([board[0],board[1],board[2].strip("\n")])
  elif(id==2):
    file = open("board2.csv")
    firstLine = file.readline()
    b = []
    for data in file:
      board = data.split(",")
      b.append([board[0],board[1],board[2],board[3].strip("\n")])
  else:
    file = open("board3.csv")
    firstLine = file.readline()
    b = []
    for data in file:
      board = data.split(",")
      b.append([board[0],board[1],board[2],board[3].strip("\n")]) 
  
  return b

def showBoard(b):
  if(int(len(b))==3):
    for i in range(int(len(b))):
      if(i==0):
        print("\t\tCol 0\tCol 1\tCol 2\n")
      print("Row "+str(i)+"\t  "+b[i][0]+"\t\t  "+b[i][1]+"\t\t  "+b[i][2]+"\n")
  else:
    for i in range(int(len(b))):
      if(i==0):
        print("\t\tCol 0\tCol 1\tCol 2\tCol 3\n")
      print("Row "+str(i)+"\t  "+b[i][0]+"\t\t  "+b[i][1]+"\t\t  "+b[i][2]+"\t\t  "+b[i][3]+"\n")

def changeBoard(b,n,r,c):
  for i in range(int(len(b))):
    if(int(r)==i):
      b[i][int(c)] = str(n)

  return b

def totalRow(b):
  rowSum = []

  for r in range(int(len(b))):
    total = 0
    for c in range(int(len(b))):
      total+=int(b[r][c])

    rowSum.append(total)
  
  return rowSum

def totalCol(b):
  colSum = []

  for c in range(int(len(b))):
    total = 0
    for r in range(int(len(b))):
      total+=int(b[r][c])

    colSum.append(total)
  
  return colSum

def calcPoints(rl,cl,t):
  points = 0
  max = 0
  holder = 0

  if(int(t)>0):
    for i in range(int(len(rl))):
      if(int(rl[i]) > int(cl[i])):
        holder = int(rl[i])
      else:
        holder = int(cl[i])
    
      if(max < holder):
        max = holder
    
    points = max//int(t)
  else:
    points = 0

  print("Points Gained: "+str(points))
  print("Calculated by max("+str(max)+") divided by # of turns("+str(t)+")")

  return points

def outcome(rl,cl):
  gameEnd = True
  for i in range(int(len(rl))):
    if((int(rl[i]) % 2) != 0 ):
      gameEnd = False
    elif((int(cl[i]) % 2) != 0 ):
      gameEnd = False

  return gameEnd

def ai(b):
  num = r.randint(0,9)
  row = r.randint(0,int(len(b))-1)
  col = r.randint(0,int(len(b))-1)

  newBoard = changeBoard(b,num,row,col)

  return newBoard

def colorCoding(l):
  colorList = []

  for p in range(int(len(l))):
    file = open("colorcoding.csv")
    firstLine = file.readline()
    for data in file:
      board = data.split(",")
      if(board[0] == str(l[p])):
        colorList.append([board[1],board[2],board[3].strip("\n")])
   
  return colorList

def FinalLineImage(cl,p,b):
  width = (10*int(len(b))) + (int(len(b))*int(p))
  height = int(p)
  img = image.createBlackImage(width,height)
  colorList = colorCoding(cl)

  for i in range(int(len(b))):
    start = (i*int(p))+(10*i)
    end = ((i+1)*int(p)) + (10*(i+1))

    for w in range(start,end):      # width
      for h in range(height):      # hieght 
      
        pix = img[w][h]
        if((end-int(w))<=10):      #black seperators 
          for b in range(3):        
            pix[b] = 0
        else:                       #color in terms of number list
          for b in range(3):         
            pix[b] = int(colorList[i][b])
  
  image.saveImage(img,"FinalLine.jpg")
  image.showImage(img,"FinalLine.jpg")

def FinalColImage(rl,p,b):
  height = (10*int(len(b))) + (int(len(b))*int(p))
  width = int(p)
  img = image.createBlackImage(width,height)
  colorList = colorCoding(rl)
  
  for i in range(int(len(b))):
    start = (i*int(p))+(10*i)
    end = ((i+1)*int(p)) + (10*(i+1))
    for w in range(width):      # height
      for h in range(start,end):       # width 
      
        pix = img[w][h]
        if((end-int(h))<=10):      #black seperators 
          for b in range(3):        
            pix[b] = 0
        else:               #color in terms of number list
          for b in range(3):         
            pix[b] = int(colorList[i][b])
  
  image.saveImage(img,"FinalColumn.jpg")
  image.showImage(img,"FinalColumn.jpg")