import random
import math

def cell_value(board):

	for i in range(len(board)):

		value = 0

		if board[i] == "M":
			continue
		else:
			rownum = i//10
			colnum = i%10
			for k in range(-1,2):
				for l in range(-1,2):
					if k == 0 and l == 0:
						continue
					elif -1 < (rownum + k)< 10 and -1 < (colnum + l)< 10:
						if board[((rownum + k)* 10) + (colnum+l)] == "M":
							value += 1

			board[i] = str(value)

def get_number_of_mines(boardSize):

	number_of_mines = int(input("Number of mines: "))

	if(number_of_mines > pow(boardSize,2) or number_of_mines < 0):
		get_number_of_mines(boardSize)

	return number_of_mines

def random_mine_position(number_of_mines,board,boardSize):
	
	for i in range(number_of_mines):
		random_position = random.randint(0,pow(boardSize,2)-1)
		while board[random_position] == "M":
			random_position = random.randint(0,pow(boardSize,2)-1)

		board[random_position] = "M"

def show_board(board):

	for i in range(int(math.sqrt(len(board)))):
		for j in range(int(math.sqrt(len(board)))):
			print(board[(i*10)+j] + " ", end =" ")
		print ("\n")

def init_game(board, boardSize):
	
	for i in range(pow(boardSize,2)):
		board.append("0")


	
board = []		
boardSize = 10	
number_of_mines=0
number_of_mines = get_number_of_mines(boardSize)
init_game(board,boardSize)
random_mine_position(number_of_mines,board,boardSize)
cell_value(board)
show_board(board)



