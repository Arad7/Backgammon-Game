import random
import math
from graphics import *
class cube():
    
    def __init__(self):
        self.value = 0
    
    def roll(self):
        self.value = random.randrange(1,7)
        
    def get_value(self):
        return self.value
    
def create_board(win, board):
    """Draws the board to the GraphWin object given.
    
    Parameters:
        win: a GraphWin object
        board: a list of lists
    
    Returns:
        Nothing; called for the side effect
    
    Postconditions:
        - Sets the color of the board and create the Rectangle
          separates the left and right side of each row at the
          board.
        - Calls to create_tris(tri,win) that creates the 24 triangels
          on the board
        - Calls to create_pawns(win,board) that takes the board and
          print the pawn of each color on the board
        
    """
    rec2 = Rectangle(Point(0,0),Point(620,400))
    rec2.setFill("peru")
    rec2.draw(win)
    tri = Polygon(Point(-50,0) , Point(0,0) , Point(-25,175))
    create_tris(tri,win)
    rec = Rectangle(Point(300,0),Point(320,400))
    rec.setFill("chocolate")
    rec.draw(win)
    create_pawns(win,board)
    
def create_pawns(win,board):
    """Draws the pawns from the board on the GraphWin object given.
    
    Parameters:
        win: a GraphWin object
        board: a list of lists
    
    Returns:
        Nothing; called for the side effect
    
    Postconditions:
        - Running on each list of the board and and then in each
          pawn in of the list. Print the pawns from the board on
          the GraphWin accordingly to the color listed for each pawn in the board.
    """
    index = 0
    base_low = 620 - 620/24
    # The middle of the of the first tringle
    base_top = 620/24
    for line in board:
        
        x = 20
        y = 380
        for i in range(line[1]):
            
            if index < 13:
                # if the index is less that 13 that means we are in the buttom half. if its
                # if its more that means we are in the top of the board
                pawn = Circle(Point(base_low,x), 15)
                x += 30
                # the Y value
            else:
                pawn = Circle(Point(base_top,y), 15)
                y -= 30
            if line[0] == "empty":
                print(board)
            pawn.setFill(line[0])
            pawn.draw(win)
        if index !=0 and index != 25:
            if index < 13:
                base_low -= 50
                # the distance between center of ine triangle to another, the x value
                if index == 6:
                    # because of the line in the middle of the board
                    base_low -= 20
            else:
                base_top += 50
                if index == 18:
                    base_top += 20
        index += 1
    
    
def is_me_there(board,index,color): 
    if board[index][0] == color:
        return True
    else:
        return False
    

def is_valid_move(board, index, color):
    
    """ checking if a move is valid in terms of what pawn are in the place the pawn supposed
        to go to + if it is in the limits of the board

        Parameters:
        board: a list
        index: an int
        color: a string
    
    Returns:
        False if the color in the gives index different than the color of the currect player or if the
        index is outside the board (what will lead to an error)
        True otherwise

    """

    if (board[index][0] != color and board[index][1] > 0) or (index < 1) or (index > 24):
        return False
    else:
        return True

def create_tris(tri,win):
    """Create and draws the Triangles on the GraphWin object given.
    
    Parameters:
        tri: a Polygon
        win: a GraphWin object
        
    
    Returns:
        Nothing; called for the side effect
    
    Postconditions:
        - Running on a loop of 2 (2 rows) and then in a loop of 12
          (12 triangels in each row, top and buttom)
          Draws each triangle in a different color from the color of the
          triangle that preceded it. The color of the first triangle is saddlebrown,
          the next is firebrick, the following will be saddlebrown again and so on.
          
    """
    previous = tri
    x = 1
    for i in range(2):
        
        for i in range(12):
    
            p1, p2, p3 = previous.getPoints()
            p1.move(50,0)
            p2.move(50,0)
            p3.move(50,0)
            if p1.getX() == 300:
                # because of the rectunglar in the middle of the board
                p1.move(20,0)
                p2.move(20,0)
                p3.move(20,0)
            
            tri2 = Polygon(p1 ,p2, p3)
            if x % 2 == 0:
                tri2.setFill("saddlebrown")
            else:
                tri2.setFill("firebrick")
            x += 1
            tri2.draw(win)
            previous = tri2
            
        x = 0
        previous = Polygon(Point(-50,400) ,Point(0,400), Point(-25,225))


def check_winner(board):
    """cheking if there is a winner to the game, if so return the name
    
    Parameters:
        board: list of lists
            
    Returns:
        returns the color of the winner as a string
        if there is no winner returns the an empty string
    
    Preconditions:
        - There are exactly 15 pawns to each player
        
        Postconditions:
        - Running on the board and fir each player add every pawn that in
          is the player's base.
        - if one of them have all the pawn in the base its return the color
          of the player
              
    """
    white = 0
    black = 0
    for i in range(len(board)):
        if i < 7:
        # The white base is until the index 6
            if board[i][0] == "white":
                white += board[i][1]
        if i > 18:
            # the Black's base is from index 18
            if board[i][0] == "black":
                black += board[i][1]
    if white == 15:
        return "white"
    elif black == 15:
        return "black"
    else:
        return ""

def main():

    win = GraphWin("BackGammon", 1000, 600)
    win.setCoords(0,0,620,400)
    board = [["empty",0],["black", 2],["empty",0],["empty",0],["empty",0],["empty",0],["white",5],["empty",0],["white",3],["empty",0],["empty",0],["empty",0],["black", 5],["white", 5],["empty",0],["empty",0],["empty",0],["black",3],["empty",0],["black", 5],["empty",0],["empty",0],["empty",0],["empty",0],["white",2]]
    # right buttom index 1. right top index 24
    create_board(win, board)
    
    players = ["white","black"]
    color_turn = 0
    winner = ""
    cube1 = cube()
    cube2 = cube()
    
    while winner == "": 
        
        cube1.roll()
        cube2.roll()
            
        cubes = Text(Point(480,200), ("your cubes are: " +str(cube1.get_value()) + " and " + str(cube2.get_value())))
        cubes.setSize(18)
        cubes.setTextColor(players[color_turn])
        cubes.draw(win)
        steps = int(win.getKey()) 
        for tern in range(2):
            # A loop that runs twice. first time the first cube
            # the player has chosen and then the second
            if tern == 1:
            # Changing the cubes after the first one is done
                if steps == cube1.get_value():
                    steps = cube2.get_value()
                else:
                    steps = cube1.get_value()
            print("you'r cube is:", steps)
            condition = False
            while condition == False:
                # The condition turn to True if the move is valid and the player
                # have a pawn where he clicked.
                pawnChoose = win.getMouse()
                while 230 > pawnChoose.getY() > 170 or 310 > pawnChoose.getX() > 290 :
                    # Making sure the player did not clicked in the middle (y value) of the
                    # board where there is nothing + did not clicked at the rectangle  in the middle
                    pawnChoose = win.getMouse()
                    print("please click a valid place") 
                
                if pawnChoose.getX() > 290:
                    pawnChoose.move(-20,0)
                    # Because of the rectangle in the middle
                movePlace = pawnChoose.getX()/50
                # 600 / 12 = 50. there are 12 triangles (places where the pawns can be) in each part
                # (buttom or top)
                movePlace = math.ceil(movePlace)
            
                if pawnChoose.getY() > 170:
                    # If the player clicked in the top part, the indexs there from left to right
                    # starts at 13 and thats why the plus 12
                    movePlace = movePlace + 12
                else:
                    movePlace = 13 - movePlace
                    # In contrast to the upper part where the indexes go up from left to right,
                    # in the lower part the indexes go up from right to left
                    
                if players[color_turn] == "white":
                    dstIndex = movePlace - steps
                    # White moves high indexes to low indexes
                else:
                    dstIndex = movePlace + steps
                    # Black moves low indexes to high indexes
                    
                if is_me_there(board, movePlace, players[color_turn]) == True and is_valid_move(board, dstIndex, players[color_turn]) == True: #making sure the player acually have a pawn where he clicked and that the move is valid(the opposite has less than 2 pawn if he is there and the pawn not moving outside of the board
                    condition = True
                else:
                    print("please click a valid place")
            
            board[dstIndex][0] = players[color_turn]
            # changing the color in the place where the pawn land
             
            board[dstIndex][1] += 1
            # Updating the number of pawn in the index where the pawn moved too
            board[movePlace][1] -= 1
            # Substracting from the index where the pawn moved from
           
            if board[movePlace][1] == 0:
                # If there are no pawns anymore it will change the color to: empty
                board[movePlace][0] = "empty"
                    

            create_board(win,board)            
            winner = check_winner(board)
            if winner != "":
                break
       
        color_turn = 1 - color_turn
        # Switches the Players turns
        
    WinnerMessage = Text(Point(140,200), ("the winner is: " + str(winner)))
    WinnerMessage.setSize(18)
    WinnerMessage.setTextColor(players[1 - color_turn])
    WinnerMessage.draw(win)
    print("The winner is", winner)
            
main()
