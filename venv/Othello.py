import random
from tkinter import *
import tkinter.ttk as ttk
import easygui

class Player:
    def __init__(self, name, wins, tokens):
        self.name = name
        self.wins = wins
        self.tokens = tokens

class Board():
    def __init__(self):
        self.board = [["Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank"],
                      ["Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank"],
                      ["Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank"],
                      ["Blank", "Blank", "Blank", "White", "Black", "Blank", "Blank", "Blank"],
                      ["Blank", "Blank", "Blank", "Black", "White", "Blank", "Blank", "Blank"],
                      ["Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank"],
                      ["Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank"],
                      ["Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank", "Blank"]]

def changePiece(GameBoard, row, col, playerTurn, Player1, Player2):
    if GameBoard.board[row][col] == "Blank":
        if playerTurn == Player1:
            GameBoard.board[row][col] = "Black"
            button = Button(root, height=70, image=pixel, width=69, bg="#000000", command = claimedTile)
            button.grid(row=row, column=col)
        elif playerTurn == Player2:
            GameBoard.board[row][col] = "White"
            button = Button(root, height=70, image=pixel, width=69, bg="#ffffff", command = claimedTile)
            button.grid(row=row, column=col)
    elif GameBoard.board[row][col] == "Black":
            GameBoard.board[row][col] = "White"
            button = Button(root, height=70, image=pixel, width=69, bg="#ffffff", command=claimedTile)
            button.grid(row=row, column=col)
    elif GameBoard.board[row][col] == "White":
        GameBoard.board[row][col] = "Black"
        button = Button(root, height=70, image=pixel, width=69, bg="#000000", command=claimedTile)
        button.grid(row=row, column=col)


def claimedTile():
    easygui.msgbox("This tile has already been claimed!", title = "Error!")


def changeTurn(Player1, Player2):
    global playerTurn
    if playerTurn == Player1:
        playerTurn = Player2
    elif playerTurn == Player2:
        playerTurn = Player1


def isLegal(GameBoard,i,j,playerTurn,Player1,Player2):
    if playerTurn == Player1:
        # Check pieces south of the selected piece
        southChange = []
        south = i + 1
        # check for white piece in south if not too close to edge (tile is at index 6 or 7)
        while south < 7:
            if GameBoard.board[south][j] == "Black":
                # makes empty list to check if all black
                southList = []
                southCoordList = []
                # adds all pieces between selected and found white to list
                for l in range(i + 1, south):
                    southList.append(GameBoard.board[l][j])
                    southCoordList.append([l, j])
                    # check if all pieces in list are black
                if all(i == "White" for i in southList):
                    southChange = southCoordList
                    break
            south += 1

        # Checks pieces north of selected piece
        northChange = []
        north = i - 1
        # check for white piece in north if not too close to edge (tile is at index 0 or 1)
        while north > 0:
            if GameBoard.board[north][j] == "Black":
                # makes empty list to check if all black
                northList = []
                northCoordList = []
                # adds all pieces between selected and found white to list
                for l in range(north+1, i):
                    northList.append(GameBoard.board[l][j])
                    northCoordList.append([l, j])
                # check if all pieces in list are black
                if all(i == "White" for i in northList):
                    northChange = northCoordList
                    break
            north -= 1

        # Checks pieces west of selected piece
        westChange = []
        west = j - 1
        # check for white piece in west if not too close to edge (tile is at index 0 or 1)
        while west > 0:
            if GameBoard.board[i][west] == "Black":
                # makes empty list to check if all black
                westList = []
                westCoordList = []
                # adds all pieces between selected and found white to list
                for l in range(west+1, j):
                    westList.append(GameBoard.board[i][l])
                    westCoordList.append([i, l])
                # check if all pieces in list are black
                if all(i == "White" for i in westList):
                    westChange = westCoordList
                    break
            west -= 1

        # Checks pieces east of selected piece
        eastChange = []
        east = j + 1
        # check for white piece in east if not too close to edge (tile is at index 6 or 7)
        while east < 7:
            if GameBoard.board[i][east] == "Black":
                # makes empty list to check if all black
                eastList = []
                eastCoordList = []
                # adds all pieces between selected and found white to list
                for l in range(j + 1, east):
                    eastList.append(GameBoard.board[i][l])
                    eastCoordList.append([i, l])
                # check if all pieces in list are black
                if all(i == "White" for i in eastList):
                    eastChange = eastCoordList
                    break
            east += 1

        #Check pieces north east of selected piece
        northEastChange = []
        northE = i - 1
        nEast = j + 1
        #Check for edge of board
        while northE > 0 and nEast < 7:
            #check for other black pieces
            if GameBoard.board[northE][nEast] == "Black":
                #makes empty list to check if all white
                northEastList = []
                # adds all pieces between selected and found black to list
                l = northE + 1
                k = nEast - 1
                while l < i and k > j:
                    northEastList.append(GameBoard.board[l][k])
                    l += 1
                    k -= 1
                #check if all pieces in list are white
                if all(i == "White" for i in northEastList):
                    northEastChange = northEastList
                    break
            northE -= 1
            nEast += 1

        # Check pieces north west of selected piece
        northWestChange = []
        northW = i - 1
        nWest = j - 1
        # Check for edge of board
        while northW > 0 and nWest > 0:
            # check for other black piece in row
            if GameBoard.board[northW][nWest] == "Black":
                # makes empty list to check if all white in between
                northWestList = []
                # adds all pieces between selected and found black to list
                l = northW + 1
                k = nWest + 1
                while l < i and k < j:
                    northWestList.append(GameBoard.board[l][k])
                    l += 1
                    k += 1
                # check if all pieces in list are black
                if all(i == "White" for i in northWestList):
                    northWestChange = northWestList
                    break
            northW -= 1
            nWest -= 1

        # Check pieces south east of selected piece
        southEastChange = []
        southE = i + 1
        sEast = j + 1
        # Check for edge of board
        while southE < 7 and sEast < 7:
            if GameBoard.board[southE][sEast] == "Black":
                # makes empty list to check if all black
                southEastList = []
                # adds all pieces between selected and found white to list
                l = southE - 1
                k = sEast - 1
                while l > i and k > j:
                    southEastList.append(GameBoard.board[l][k])
                    l -= 1
                    k -= 1
                # check if all pieces in list are black
                if all(i == "White" for i in southEastList):
                    southEastChange = southEastList
                    break
            southE += 1
            sEast += 1

        # Check pieces south west of selected piece
        southWestChange = []
        southW = i + 1
        sWest = j - 1
        # Check for edge of board
        while southW < 7 and sWest < 7:
            if GameBoard.board[southW][sWest] == "Black":
                # makes empty list to check if all black
                southWestList = []
                # adds all pieces between selected and found white to list
                l = southW - 1
                k = sWest + 1
                while l > i and k < j:
                    southWestList.append(GameBoard.board[l][k])
                    l -= 1
                    k += 1
                # check if all pieces in list are black
                if all(i == "White" for i in southWestList):
                    southWestChange = southWestList
                    break
            southW += 1
            sWest -= 1

    elif playerTurn == Player2:
        #Check pieces south of the selected piece
        southChange = []
        south = i + 1
        #check for white piece in south if not too close to edge (tile is at index 6 or 7)
        while south < 7:
             if GameBoard.board[south][j] == "White":
                 #makes empty list to check if all black
                 southList = []
                 southCoordList = []
                 #adds all pieces between selected and found white to list
                 for l in range(i+1, south):
                     southList.append(GameBoard.board[l][j])
                     southCoordList.append([l, j])
                     #check if all pieces in list are black
                 if all(i == "Black" for i in southList):
                     southChange = southCoordList
                     break
             south += 1

        #Checks pieces north of selected piece
        northChange = []
        north = i - 1
        #check for white piece in north if not too close to edge (tile is at index 0 or 1)
        while north > 0:
             if GameBoard.board[north][j] == "White":
                 #makes empty list to check if all black
                 northList = []
                 northCoordList = []
                 #adds all pieces between selected and found white to list
                 for l in range(north+1, i ):
                     northList.append(GameBoard.board[l][j])
                     northCoordList.append([l, j])
                 #check if all pieces in list are black
                 if all(i == "Black" for i in northList):
                     northChange = northCoordList
                     break
             north -= 1

        # Checks pieces west of selected piece
        westChange = []
        west = j - 1
        # check for white piece in west if not too close to edge (tile is at index 0 or 1)
        while west > 0:
            if GameBoard.board[i][west] == "White":
                # makes empty list to check if all black
                westList = []
                westCoordList = []
                # adds all pieces between selected and found white to list
                for l in range(west+1, j):
                    westList.append(GameBoard.board[i][l])
                    westCoordList.append([i, l])
                # check if all pieces in list are black
                if all(i == "Black" for i in westList):
                    westChange = westCoordList
                    break
            west -= 1

        # Checks pieces east of selected piece
        eastChange = []
        east = j + 1
        # check for white piece in east if not too close to edge (tile is at index 6 or 7)
        while east < 7:
            if GameBoard.board[i][east] == "White":
                # makes empty list to check if all black
                eastList = []
                eastCoordList = []
                # adds all pieces between selected and found white to list
                for l in range(j + 1, east):
                    eastList.append(GameBoard.board[i][l])
                    eastCoordList.append([i, l])
                # check if all pieces in list are black
                if all(i == "Black" for i in eastList):
                    eastChange = eastCoordList
                    break
            east += 1

        # Check pieces north east of selected piece
        northEastChange = []
        northE = i - 1
        nEast = j + 1
        # Check for edge of board
        while northE > 0 and nEast < 7:
            # check for other black pieces
            if GameBoard.board[northE][nEast] == "White":
                # makes empty list to check if all black
                northEastList = []
                # adds all pieces between selected and found white to list
                l = northE + 1
                k = nEast - 1
                while l < i and k > j:
                    northEastList.append(GameBoard.board[l][k])
                    l += 1
                    k -= 1
                # check if all pieces in list are white
                if all(i == "Black" for i in northEastList):
                    northEastChange = northEastList
                    break
            northE -= 1
            nEast += 1

        # Check pieces north west of selected piece
        northWestChange = []
        northW = i - 1
        nWest = j - 1
        # Check for edge of board
        while northW > 0 and nWest > 0:
            # check for other black piece in row
            if GameBoard.board[northW][nWest] == "White":
                # makes empty list to check if all black in between
                northWestList = []
                # adds all pieces between selected and found white to list
                l = northW + 1
                k = nWest + 1
                while l < i and k < j:
                    northWestList.append(GameBoard.board[l][k])
                    l += 1
                    k += 1
                # check if all pieces in list are black
                if all(i == "Black" for i in northWestList):
                    northWestChange = northWestList
                    break
            northW -= 1
            nWest -= 1

        # Check pieces south east of selected piece
        southEastChange = []
        southE = i + 1
        sEast = j + 1
        # Check for edge of board
        while southE < 7 and sEast < 7:
            if GameBoard.board[southE][sEast] == "White":
                # makes empty list to check if all black in between
                southEastList = []
                # adds all pieces between selected and found white to list
                l = southE - 1
                k = sEast - 1
                while l > i and k > j:
                    southEastList.append(GameBoard.board[l][k])
                    l -= 1
                    k -= 1
                # check if all pieces in list are black
                if all(i == "Black" for i in southEastList):
                    southEastChange = southEastList
                    break
            southE += 1
            sEast += 1

        # Check pieces south west of selected piece
        southWestChange = []
        southW = i + 1
        sWest = j - 1
        # Check for edge of board
        while southW < 7 and sWest > 0:
            if GameBoard.board[southW][sWest] == "White":
                # makes empty list to check if all black in between
                southWestList = []
                # adds all pieces between selected and found white to list
                l = southW - 1
                k = sWest + 1
                while l > i and k < j:
                    southWestList.append(GameBoard.board[l][k])
                    l -= 1
                    k += 1
                # check if all pieces in list are black
                if all(i == "Black" for i in southWestList):
                    southWestChange = southWestList
                    break
            southW += 1
            sWest -= 1

    changeList = eastChange + westChange + southChange + northChange +northEastChange + northWestChange + southEastChange + southWestChange
    if len(changeList) == 0:
        #Checks if a move is legal and informs the player if it isn't
        easygui.msgbox("This is not a legal move!", title = "Error!")
    else:
        changeList += [[i, j]]
        for i in range(len(changeList)):
            coord = changeList[i]
            changePiece(GameBoard, coord[0], coord[1], playerTurn, Player1, Player2)
        changeTurn(Player1, Player2)

    legalMoves(GameBoard, Player1, Player2)


def legalMoves(GameBoard, Player1, Player2):
    moves = 0
    for i in range(8):
        for j in range(8):
            if GameBoard.board[i][j] == "Blank":
                if playerTurn == Player1:
                    # Check pieces south of the selected piece
                    southChange = []
                    south = i + 1
                    # check for white piece in south if not too close to edge (tile is at index 6 or 7)
                    while south < 7:
                        if GameBoard.board[south][j] == "Black":
                            # makes empty list to check if all black
                            southList = []
                            southCoordList = []
                            # adds all pieces between selected and found white to list
                            for l in range(i + 1, south):
                                southList.append(GameBoard.board[l][j])
                                southCoordList.append([l, j])
                                # check if all pieces in list are black
                            if all(i == "White" for i in southList):
                                southChange = southCoordList
                                break
                        south += 1

                    # Checks pieces north of selected piece
                    northChange = []
                    north = i - 1
                    # check for white piece in north if not too close to edge (tile is at index 0 or 1)
                    while north > 0:
                        if GameBoard.board[north][j] == "Black":
                            # makes empty list to check if all black
                            northList = []
                            northCoordList = []
                            # adds all pieces between selected and found white to list
                            for l in range(north + 1, i):
                                northList.append(GameBoard.board[l][j])
                                northCoordList.append([l, j])
                            # check if all pieces in list are black
                            if all(i == "White" for i in northList):
                                northChange = northCoordList
                                break
                        north -= 1

                    # Checks pieces west of selected piece
                    westChange = []
                    west = j - 1
                    # check for white piece in west if not too close to edge (tile is at index 0 or 1)
                    while west > 0:
                        if GameBoard.board[i][west] == "Black":
                            # makes empty list to check if all black
                            westList = []
                            westCoordList = []
                            # adds all pieces between selected and found white to list
                            for l in range(west + 1, j):
                                westList.append(GameBoard.board[i][l])
                                westCoordList.append([i, l])
                            # check if all pieces in list are black
                            if all(i == "White" for i in westList):
                                westChange = westCoordList
                                break
                        west -= 1

                    # Checks pieces east of selected piece
                    eastChange = []
                    east = j + 1
                    # check for white piece in east if not too close to edge (tile is at index 6 or 7)
                    while east < 7:
                        if GameBoard.board[i][east] == "Black":
                            # makes empty list to check if all black
                            eastList = []
                            eastCoordList = []
                            # adds all pieces between selected and found white to list
                            for l in range(j + 1, east):
                                eastList.append(GameBoard.board[i][l])
                                eastCoordList.append([i, l])
                            # check if all pieces in list are black
                            if all(i == "White" for i in eastList):
                                eastChange = eastCoordList
                                break
                        east += 1

                    # Check pieces north east of selected piece
                    northEastChange = []
                    northE = i - 1
                    nEast = j + 1
                    # Check for edge of board
                    while northE > 0 and nEast < 7:
                        # check for other black pieces
                        if GameBoard.board[northE][nEast] == "Black":
                            # makes empty list to check if all white
                            northEastList = []
                            # adds all pieces between selected and found black to list
                            l = northE + 1
                            k = nEast - 1
                            while l < i and k > j:
                                northEastList.append(GameBoard.board[l][k])
                                l += 1
                                k -= 1
                            # check if all pieces in list are white
                            if all(i == "White" for i in northEastList):
                                northEastChange = northEastList
                                break
                        northE -= 1
                        nEast += 1

                    # Check pieces north west of selected piece
                    northWestChange = []
                    northW = i - 1
                    nWest = j - 1
                    # Check for edge of board
                    while northW > 0 and nWest > 0:
                        # check for other black piece in row
                        if GameBoard.board[northW][nWest] == "Black":
                            # makes empty list to check if all white in between
                            northWestList = []
                            # adds all pieces between selected and found black to list
                            l = northW + 1
                            k = nWest + 1
                            while l < i and k < j:
                                northWestList.append(GameBoard.board[l][k])
                                l += 1
                                k += 1
                            # check if all pieces in list are black
                            if all(i == "White" for i in northWestList):
                                northWestChange = northWestList
                                break
                        northW -= 1
                        nWest -= 1

                    # Check pieces south east of selected piece
                    southEastChange = []
                    southE = i + 1
                    sEast = j + 1
                    # Check for edge of board
                    while southE < 7 and sEast < 7:
                        if GameBoard.board[southE][sEast] == "Black":
                            # makes empty list to check if all black
                            southEastList = []
                            # adds all pieces between selected and found white to list
                            l = southE - 1
                            k = sEast - 1
                            while l > i and k > j:
                                southEastList.append(GameBoard.board[l][k])
                                l -= 1
                                k -= 1
                            # check if all pieces in list are black
                            if all(i == "White" for i in southEastList):
                                southEastChange = southEastList
                                break
                        southE += 1
                        sEast += 1

                    # Check pieces south west of selected piece
                    southWestChange = []
                    southW = i + 1
                    sWest = j - 1
                    # Check for edge of board
                    while southW < 7 and sWest < 7:
                        if GameBoard.board[southW][sWest] == "Black":
                            # makes empty list to check if all black
                            southWestList = []
                            # adds all pieces between selected and found white to list
                            l = southW - 1
                            k = sWest + 1
                            while l > i and k < j:
                                southWestList.append(GameBoard.board[l][k])
                                l -= 1
                                k += 1
                            # check if all pieces in list are black
                            if all(i == "White" for i in southWestList):
                                southWestChange = southWestList
                                break
                        southW += 1
                        sWest -= 1

                elif playerTurn == Player2:
                    # Check pieces south of the selected piece
                    southChange = []
                    south = i + 1
                    # check for white piece in south if not too close to edge (tile is at index 6 or 7)
                    while south < 7:
                        if GameBoard.board[south][j] == "White":
                            # makes empty list to check if all black
                            southList = []
                            southCoordList = []
                            # adds all pieces between selected and found white to list
                            for l in range(i + 1, south):
                                southList.append(GameBoard.board[l][j])
                                southCoordList.append([l, j])
                                # check if all pieces in list are black
                            if all(i == "Black" for i in southList):
                                southChange = southCoordList
                                break
                        south += 1

                    # Checks pieces north of selected piece
                    northChange = []
                    north = i - 1
                    # check for white piece in north if not too close to edge (tile is at index 0 or 1)
                    while north > 0:
                        if GameBoard.board[north][j] == "White":
                            # makes empty list to check if all black
                            northList = []
                            northCoordList = []
                            # adds all pieces between selected and found white to list
                            for l in range(north + 1, i):
                                northList.append(GameBoard.board[l][j])
                                northCoordList.append([l, j])
                            # check if all pieces in list are black
                            if all(i == "Black" for i in northList):
                                northChange = northCoordList
                                break
                        north -= 1

                    # Checks pieces west of selected piece
                    westChange = []
                    west = j - 1
                    # check for white piece in west if not too close to edge (tile is at index 0 or 1)
                    while west > 0:
                        if GameBoard.board[i][west] == "White":
                            # makes empty list to check if all black
                            westList = []
                            westCoordList = []
                            # adds all pieces between selected and found white to list
                            for l in range(west + 1, j):
                                westList.append(GameBoard.board[i][l])
                                westCoordList.append([i, l])
                            # check if all pieces in list are black
                            if all(i == "Black" for i in westList):
                                westChange = westCoordList
                                break
                        west -= 1

                    # Checks pieces east of selected piece
                    eastChange = []
                    east = j + 1
                    # check for white piece in east if not too close to edge (tile is at index 6 or 7)
                    while east < 7:
                        if GameBoard.board[i][east] == "White":
                            # makes empty list to check if all black
                            eastList = []
                            eastCoordList = []
                            # adds all pieces between selected and found white to list
                            for l in range(j + 1, east):
                                eastList.append(GameBoard.board[i][l])
                                eastCoordList.append([i, l])
                            # check if all pieces in list are black
                            if all(i == "Black" for i in eastList):
                                eastChange = eastCoordList
                                break
                        east += 1

                    # Check pieces north east of selected piece
                    northEastChange = []
                    northE = i - 1
                    nEast = j + 1
                    # Check for edge of board
                    while northE > 0 and nEast < 7:
                        # check for other black pieces
                        if GameBoard.board[northE][nEast] == "White":
                            # makes empty list to check if all black
                            northEastList = []
                            # adds all pieces between selected and found white to list
                            l = northE + 1
                            k = nEast - 1
                            while l < i and k > j:
                                northEastList.append(GameBoard.board[l][k])
                                l += 1
                                k -= 1
                            # check if all pieces in list are white
                            if all(i == "Black" for i in northEastList):
                                northEastChange = northEastList
                                break
                        northE -= 1
                        nEast += 1

                    # Check pieces north west of selected piece
                    northWestChange = []
                    northW = i - 1
                    nWest = j - 1
                    # Check for edge of board
                    while northW > 0 and nWest > 0:
                        # check for other black piece in row
                        if GameBoard.board[northW][nWest] == "White":
                            # makes empty list to check if all black in between
                            northWestList = []
                            # adds all pieces between selected and found white to list
                            l = northW + 1
                            k = nWest + 1
                            while l < i and k < j:
                                northWestList.append(GameBoard.board[l][k])
                                l += 1
                                k += 1
                            # check if all pieces in list are black
                            if all(i == "Black" for i in northWestList):
                                northWestChange = northWestList
                                break
                        northW -= 1
                        nWest -= 1

                    # Check pieces south east of selected piece
                    southEastChange = []
                    southE = i + 1
                    sEast = j + 1
                    # Check for edge of board
                    while southE < 7 and sEast < 7:
                        if GameBoard.board[southE][sEast] == "White":
                            # makes empty list to check if all black in between
                            southEastList = []
                            # adds all pieces between selected and found white to list
                            l = southE - 1
                            k = sEast - 1
                            while l > i and k > j:
                                southEastList.append(GameBoard.board[l][k])
                                l -= 1
                                k -= 1
                            # check if all pieces in list are black
                            if all(i == "Black" for i in southEastList):
                                southEastChange = southEastList
                                break
                        southE += 1
                        sEast += 1

                    # Check pieces south west of selected piece
                    southWestChange = []
                    southW = i + 1
                    sWest = j - 1
                    # Check for edge of board
                    while southW < 7 and sWest > 0:
                        if GameBoard.board[southW][sWest] == "White":
                            # makes empty list to check if all black in between
                            southWestList = []
                            # adds all pieces between selected and found white to list
                            l = southW - 1
                            k = sWest + 1
                            while l > i and k < j:
                                southWestList.append(GameBoard.board[l][k])
                                l -= 1
                                k += 1
                            # check if all pieces in list are black
                            if all(i == "Black" for i in southWestList):
                                southWestChange = southWestList
                                break
                        southW += 1
                        sWest -= 1

                changeList = eastChange + westChange + southChange + northChange + northEastChange + northWestChange + southEastChange + southWestChange
                if len(changeList) != 0:
                    moves += 1

    if moves == 0:
        black = 0
        white = 0
        for i in range(8):
            for j in range(8):
                if GameBoard.board[i][j] == "Black":
                    black += 1
                elif GameBoard.board[i][j] == "White":
                    white += 1

        if black > white:
            easygui.msgbox("The game is over! Player 1 " + Player1 + " is the winner! Press play above to start again", title="Game End")
        elif white > black:
            easygui.msgbox("The game is over! Player 2 " + Player2 + " is the winner! Press play above to start again", title="Game End")
        elif white == black:
            easygui.msgbox("The game is over! It is a tie! Press play above to start again", title="Game End")

def GamePVP():
    GameBoard = Board()
    global playerTurn
    playerTurn = Player1.name
    for i in range(8):
        for j in range(8):
            if GameBoard.board[i][j] == "Blank":
                button = Button(root, height = 70, image=pixel, width = 69, bg = "#c9b493", text = "Blank", command = lambda i=i, j = j: isLegal(GameBoard,i,j,playerTurn,Player1.name,Player2.name))
                button.grid(row = i, column = j)
            elif GameBoard.board[i][j] == "Black":
                button = Button(root, height = 70, image=pixel, width = 69, bg = "#000000", command = claimedTile)
                button.grid(row = i, column = j)
            elif GameBoard.board[i][j] == "White":
                button = Button(root, height = 70, image=pixel, width = 69, bg = "#ffffff", command = claimedTile)
                button.grid(row = i, column = j)


root = Tk()
root.title("Othello")
root.geometry("600x700")
root.resizable(width = False, height = False)
welcome = Label(root, text="WELCOME! Press play in the menu above to start")
welcome.pack()
Player1 = Player(name="Player1", wins=0, tokens=2)
Player2 = Player(name="Player2", wins=0, tokens=2)

playerTurn = Player1.name
pixel = PhotoImage(width = 1, height = 1)
menubar = Menu(root)
menubar.add_command(label="Play Human vs. Human", command = lambda: [welcome.pack_forget(), GamePVP()])
menubar.add_command(label="Exit", command = root.destroy)
root.config(menu=menubar)
root.mainloop()