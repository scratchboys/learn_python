- Game: Sonar Treasure Hunting

- Setups and procedures:
  NumOfTreasures = 3
  SonarDevices = 20           # player has only 20 sonar devices to find 3 treasures to win !!!  
  PreviousMoves = []          # store the positions player put sonar devices, to make sure not a same positon to put device again
  TheBoard = getNewBoard()    # initial ocean area, 60 columns (x=0..59) and 15 rows (y=0..14);
                              # save shapes (~ and `) in a two-dimensiona array
  TheChests = getRandomChests(NumOfTreasures)  # randomly select Treasures' position on the board (ocean area) 
  drawBoard(TheBoard)
  
  while SonarDevices > 0:
    x, y = enterPlayerMove(PreviousMoves)   # Need to make sure player pick the location on the board (the specific ocean area)
    makeMove(TheBoard, TheChests, x, y)     # calculate the distance (x,y) to the treasures, if 0, remove the found treasure from 
                                            # TheChests. if <= 9, display the digit,  if > 9, display X on the board. 
    drawBoard(TheBoard)
    
  
