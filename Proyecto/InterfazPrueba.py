"""
    Autores: 
        María Camila Aguirre Collante
        Jessica Tatiana Naizaque Guevara
"""
import copy
import random
from colorama import *

init(autoreset=True)
pathR = []
pathG = []
pathY = []
pathB = []
pathW = []
pathC = []
pathP = []
#definir colores que serán usados
yellow = Back.YELLOW
blue = Back.BLUE
red = Back.RED
green = Back.GREEN
cyan = Back.CYAN
purple = Back.MAGENTA
white = Back.WHITE

'''
@Entradas -> dim=dimensiones del tablero de juego
@Salida -> creación del tablero de juego
'''
def createBoard(dim):
    if dim == 9:
        numBoard = random.randint(1, 7)
    else:
        numBoard =  random.randint(1, 10)
    #end if
    path = "Niveles" + str(dim) + "X" + str(dim) + "/" + str(numBoard) + ".txt"
    path = "Niveles5X5/1.txt"
    board = []
    with open(path, "r") as file:
        for lines in file:
            board.append(lines.split())
        #end for
    return board
#end-def

'''
@Entradas -> board: tablero de juego
@Salida -> mostrar el tablero de juego
'''
def showBoard(board):
    boardTemp = copy.deepcopy(board)
    print("-"*(7 * len(boardTemp)+1))
    for i in range(len(boardTemp)):
        for j in range(len(boardTemp)):
            if boardTemp[i][j] == "R" or boardTemp[i][j] == "R!":
                boardTemp[i][j]= str(i)+str(j)
                print("| ", end = "")
                print(red + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "G" or boardTemp[i][j] == "G!":
                boardTemp[i][j]= str(i)+str(j)
                print("| ", end = "")
                print(green + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "B" or boardTemp[i][j] == "B!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(blue + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "Y" or boardTemp[i][j] == "Y!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(yellow + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "W" or boardTemp[i][j] == "W!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(white + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "C" or boardTemp[i][j] == "C!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(cyan + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "P" or boardTemp[i][j] == "P!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(purple + " {:3}".format(boardTemp[i][j]), end = " ")
            else:
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(Back.BLACK + " {:3}".format(boardTemp[i][j]), end = " ")
            #end if
        #end for
        print("|")
        print("-"*(7 * len(boardTemp)+1))
    #end for
#end def

def checkPath(initial, path, dim):
    win1 = False
    win2 = False
    if (int(initial[0][0]) > 0) or (int(initial[1][0]) > 0): #Casilla Arriba
        new = str(int(initial[0][0])-1) + initial[0][1]
        if new in path:
            win1 = True
        new = str(int(initial[1][0])-1) + initial[1][1]
        if new in path:
            win2 = True
    #end if
    if (int(initial[0][0]) < dim-1) or (int(initial[1][0]) < dim-1): #Casilla Abajo
        new = str(int(initial[0][0])+1) + initial[0][1]
        if new in path:
            win1 = True
        new = str(int(initial[1][0])+1) + initial[1][1]
        if new in path:
            win2 = True
    #end if
    if (int(initial[0][1]) > 0) or (int(initial[1][1]) > 0): #Casilla Izquierda
        new = initial[0][0] + str(int(initial[0][1])-1)
        if new in path:
            win1 = True
        new = initial[1][0] + str(int(initial[1][1])-1)
        if new in path:
            win2 = True
    #end if
    if (int(initial[0][1]) < dim-1) or (int(initial[1][1]) < dim-1): #Casilla Derecha
        new = initial[0][0] + str(int(initial[0][1])+1)
        if new in path:
            win1 = True
        new = initial[1][0] + str(int(initial[1][1])+1)
        if new in path:
            win2 = True
    #end if
    if win1 and win2:
        return True
    #end if
#end def
'''
@Entradas ->
@Salida -> 
'''
def checkWinner(board):
    dim = len(board)
    rInitial = []
    bInitial = []
    yInitial = []
    gInitial = []
    wInitial = []
    cInitial = []
    pInitial = []
    for i in range(dim):
        for j in range(dim):
            if board[i][j] == "R!":
                rInitial.append(str(i)+str(j))
            elif board[i][j] == "B!":
                bInitial.append(str(i)+str(j))
            elif board[i][j] == "Y!":
                yInitial.append(str(i)+str(j))
            elif board[i][j] == "G!":
                gInitial.append(str(i)+str(j))
            elif board[i][j] == "W!":
                wInitial.append(str(i)+str(j))
            elif board[i][j] == "C!":
                cInitial.append(str(i)+str(j))
            elif board[i][j] == "P!":
                pInitial.append(str(i)+str(j))
            #end if
        #end for
    #end for
    if (len(pathR)) > 0:
        winR = checkPath(rInitial, pathR, dim)
    else:
        winR = True
    if (len(pathB)) > 0:
        winB = checkPath(bInitial, pathB, dim)
    else:
        winB = True
    if (len(pathY)) > 0:
        winY = checkPath(yInitial, pathY, dim)
    else:
        winY = True
    if (len(pathG)) > 0:
        winG = checkPath(gInitial, pathG, dim)
    else:
        winG = True
    if (len(pathW)) > 0:
        winW = checkPath(wInitial, pathW, dim)
    else:
        winW = True
    if (len(pathC)) > 0:
        winC = checkPath(cInitial, pathC, dim)
    else:
        winC = True
    if (len(pathP)) > 0:
        winP = checkPath(pInitial, pathP, dim)
    else:
        winP = True
    if winR and winB and winY and winG and winW and winC and winP:
        return True
    return False
#end def

'''
@Entradas ->
@Salida -> 
'''
def checkFinished(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "0":
                return False    
            #end if
        #end for
    #end for
    return True
#end def

'''
@Entradas ->
@Salida -> 
'''
def checkBox(board, color, coordenate):
    i = int(coordenate[0])
    j = int(coordenate[1])
    n = len(board)
    if board[i][j] == "0" or "!" not in board[i][j]:
        if i > 0:
            if board[i-1][j] == color or board[i-1][j] == color+"!": #Si su casilla de arriba es del mismo color
                return [str(i-1) + "," + str(j), True]
            #end if
        #end if
        if j > 0:
            if board[i][j-1] == color or board[i][j-1] == color+"!": #Si su casilla izquierda es del mismo color
                return [str(i) + "," + str(j-1), True]
            #end if
        #end if
        if i < n-1:
            if board[i+1][j] == color or board[i+1][j] == color+"!": #Si su casilla de abajo es del mismo color
                return [str(i+1) + "," + str(j), True]
            #end if
        #end if
        if j < n-1:
            if board[i][j+1] == color or board[i][j+1] == color+"!": #Si su casilla derecha es del mismo color
                return [str(i) + "," + str(j+1), True]
            #end if
        #end if
        print("******No hay casillas adyacentes del color seleccionado.\n")
    if "!" in board[i][j]:
        print("******No puede cambiar una casilla inicial.\n")
    #end if
    return ['F', False]
#end def

def checkE(element, board):
    if len(pathR) > 0:
        if element in pathR:
            for r in range (len(pathR)):
                board[int(pathR[r][0])][int(pathR[r][1])] = '0'
            #end for
            pathR.clear()
            return True
        #end if
    #end if
    if len(pathB) > 0:
        if element in pathB:
            for b in range (len(pathB)):
                board[int(pathB[b][0])][int(pathB[b][1])] = '0'
            #end for
            pathB.clear()
            return True
        #end if
    #end if
    if len(pathY) > 0:
        if element in pathY:
            for y in range (len(pathY)):
                board[int(pathY[y][0])][int(pathY[y][1])] = '0'
            #end for
            pathY.clear()
            return True
        #end if
    #end if
    if len(pathG) > 0:    
        if element in pathG:
            for g in range (len(pathG)):
                board[int(pathG[g][0])][int(pathG[g][1])] = '0'
            #end for
            pathG.clear()
            return True
        #end if
    #end if
    if len(pathW) > 0:
        if element in pathW:
            for w in range (len(pathW)):
                board[int(pathW[w][0])][int(pathW[w][1])] = '0'
            #end for
            pathW.clear()
            return True
        #end if
    #end if
    if len(pathC) > 0:
        if element in pathC:
            for c in range (len(pathC)):
                board[int(pathC[c][0])][int(pathC[c][1])] = '0'
            #end for
            pathC.clear()
            return True
        #end if
    #end if
    if len(pathP) > 0:
        if element in pathP:
            for p in range (len(pathP)):
                board[int(pathP[p][0])][int(pathR[p][1])] = '0'
            #end for
            pathP.clear()
            return True
        #end if
    #end if
#end def

def addPath(color, coordenate, board):
    checkE(coordenate, board)
    if color == 'R':
        pathR.append(coordenate)
    elif color == 'G':
        pathG.append(coordenate)
    elif color == 'Y':
        pathY.append(coordenate)
    elif color == 'W':
        pathW.append(coordenate)
    elif color == 'B':
        pathB.append(coordenate)
    elif color == 'C':
        pathC.append(coordenate)
    elif color == 'P':
        pathP.append(coordenate)
    #end if
#end def

'''
@Entradas ->
@Salida -> 
'''
def selectMove(board):
    finished = False #Verificar que el juego no haya finalizado (cuando todas las casillas tienen color)
    win = False
    while not finished:
        parameters = False #Verificar que los parámetros estén correctos y que haya seleccionado una casilla correcta
        while not parameters:
            print("Recuerde que los colores son:  ", red + " {:4}".format("Red"), green + " {:6}".format("Green"), blue + " {:5}".format("Blue"), yellow + " {:7}".format("Yellow"), white + " {:6}".format("White"), cyan + " {:5}".format("Cyan"), purple + " {:7}".format("Purple"), end = " ")
            print("\n")
            move = str(input("Digite la inicial del color que desea utilizar y la casilla que desea jugar (Ej: R 34): "))
            movements = move.split()
            if len(movements) == 2:
                if movements[0].isalpha():
                    if movements[1].isnumeric():
                        if movements[0].upper() == "R" or movements[0].upper() == "G" or movements[0].upper() == "B" or movements[0].upper() == "Y" or movements[0].upper() == "W" or movements[0].upper() == "C" or movements[0].upper() == "P": 
                            if len(movements[1])  == 2:
                                if (int(movements[1][0]) >= 0) and (int(movements[1][0]) < len(board)) and (int(movements[1][1]) >= 0) and (int(movements[1][1]) < len(board)):
                                    boxChecked = checkBox(board, movements[0].upper(), movements[1])
                                    addPath(movements[0].upper(), movements[1], board)
                                    #if boxChecked[0] != 'F':
                                        #checkAdjacents(board, boxChecked[0])
                                    parameters = boxChecked[1]
                                    #Verificar que no tenga más de dos adyacentes
                                else:
                                    print("******Número de casilla incorrecta.\n")
                                #end if
                            else:
                                print("******Número de casilla incorrecta.\n")
                            #end if
                        else:
                            print("******Inicial de color inválida.\n")
                        #end if
                    else:
                        print ("******Parámetro casilla incorrecto.\n")
                    #end if
                else:
                    print ("******Parámetro color incorrecto.\n")
                #end if
            else:
                print("******Cantidad de parámetros enviados incorrecta.\n")
            #end if
        #end while
        board[int(movements[1][0])][int(movements[1][1])] = movements[0].upper()
        showBoard(board)
        finished = checkFinished(board)
        #print(finished)
        if finished:
            win = checkWinner(board)
            if win == False:
                finished = False
                print("\t\tNo ha completado de manera correcta el nivel :(")
                print("\t\t\t\nPor favor, siga intentando :D")
            else:
                finished = True
                pathR.clear()
                pathB.clear()
                pathG.clear()
                pathY.clear()
                pathW.clear()
                pathC.clear()
                pathP.clear()
                print("\t\tHa superado el nivel con éxito! ")
            #end if
        #end if
    #end while
#end def