"""Automate the Boring Stuff didn't finish the tic-tac-toe program in its
dictionaries section. Someone had to answer the call...
...It shouldn't have been me."""

import sys, time

# we'll just leave this here
ttt_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
	     'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
	     'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def print_board(ttt_board):
	"""
	Prints the tic-tac-toe board to the player(s). Updates after player(s)
	input their move.

	:param ttt_board: A dictionary where keys are spaces and values are ' '
	:return: string_board, the tic-tac-toe board
	"""
	string_board = \
		f"""
{ttt_board['top-L']}|{ttt_board['top-M']}|{ttt_board['top-R']}
-+-+-
{ttt_board['mid-L']}|{ttt_board['mid-M']}|{ttt_board['mid-R']}
-+-+-
{ttt_board['low-L']}|{ttt_board['low-M']}|{ttt_board['low-R']}
"""

	return string_board


def check_win(print_board, ttt_board):
	"""
	Refactor this horrendous function. Also, checks to see if either player
	X or player O has won (because Automate the Boring Stuff stopped at this
	point in coding the game).

	:param print_board: Displays board, X, and O positions to player(s)
	:param ttt_board: Argument passed into print_board w/ position keys/values
	:return: None, sys.exit() if is_winner == True
	"""
	is_winner = False
	player = ''

	def winner(player):
		winner_print = [
			"* * * * * * * * * * *",
			"* * * * * * * * * * *",
			f"   Player {player} wins!",
			"* * * * * * * * * * *",
			"* * * * * * * * * * *"
		]
		for line in winner_print:
			time.sleep(.5)
			print(line)
		sys.exit()

	# check X
	if ttt_board['top-L'] == 'X' and ttt_board['top-M'] == 'X' and ttt_board[
		'top-R'] == 'X':
		player = 'X'
		is_winner = True
	if ttt_board['mid-L'] == 'X' and ttt_board['mid-M'] == 'X' and ttt_board[
		'mid-R'] == 'X':
		player = 'X'
		is_winner = True
	if ttt_board['low-L'] == 'X' and ttt_board['low-M'] == 'X' and ttt_board[
		'low-R'] == 'X':
		player = 'X'
		is_winner = True
	if ttt_board['top-L'] == 'X' and ttt_board['mid-L'] == 'X' and ttt_board[
		'low-L'] == 'X':
		player = 'X'
		is_winner = True
	if ttt_board['top-M'] == 'X' and ttt_board['mid-M'] == 'X' and ttt_board[
		'low-M'] == 'X':
		player = 'X'
		is_winner = True
	if ttt_board['top-R'] == 'X' and ttt_board['mid-R'] == 'X' and ttt_board[
		'low-R'] == 'X':
		player = 'X'
		is_winner = True
	if ttt_board['top-L'] == 'X' and ttt_board['mid-M'] == 'X' and ttt_board[
		'low-R'] == 'X':
		player = 'X'
		is_winner = True
	if ttt_board['top-R'] == 'X' and ttt_board['mid-M'] == 'X' and ttt_board[
		'low-L'] == 'X':
		player = 'X'
		is_winner = True

	# check O
	if ttt_board['top-L'] == 'O' and ttt_board['top-M'] == 'O' and ttt_board[
		'top-R'] == 'O':
		player = 'O'
		is_winner = True
	if ttt_board['mid-L'] == 'O' and ttt_board['mid-M'] == 'O' and ttt_board[
		'mid-R'] == 'O':
		player = 'O'
		is_winner = True
	if ttt_board['low-L'] == 'O' and ttt_board['low-M'] == 'O' and ttt_board[
		'low-R'] == 'O':
		player = 'O'
		is_winner = True
	if ttt_board['top-L'] == 'O' and ttt_board['mid-L'] == 'O' and ttt_board[
		'low-L'] == 'O':
		player = 'O'
		is_winner = True
	if ttt_board['top-M'] == 'O' and ttt_board['mid-M'] == 'O' and ttt_board[
		'low-M'] == 'O':
		player = 'O'
		is_winner = True
	if ttt_board['top-R'] == 'O' and ttt_board['mid-R'] == 'O' and ttt_board[
		'low-R'] == 'O':
		player = 'O'
		is_winner = True
	if ttt_board['top-L'] == 'O' and ttt_board['mid-M'] == 'O' and ttt_board[
		'low-R'] == 'O':
		player = 'O'
		is_winner = True
	if ttt_board['top-R'] == 'O' and ttt_board['mid-M'] == 'O' and ttt_board[
		'low-L'] == 'O':
		player = 'O'
		is_winner = True

	if is_winner:
		print(print_board(ttt_board))
		winner(player)


def main(ttt_board, print_board, check_win):
	"""
	PleasestopmewhyIamIcreatingthismonster.
	Also, this function starts the game.
	
	:param print_board: Displays board, X, and O positions to player(s)
	:param ttt_board: Argument passed into print_board w/ position keys/values
	:param check_win: Function that checks if either player has won.
	:return: None. sys.exit() if winner.
	"""
	print("""
WELCOME...
...to tacode's terribly written tic-tac-toe game!
___________________________________________________

Board positions:

 top-L  |  top-M  |  top-R 
--------+---------+--------
 mid-L  |  mid-M  |  mid-R 
--------+---------+--------
 low-L  |  low-M  |  low-R 

Example: To move on the middle space, enter mid-M	

___________________________________________________

	""")
	turn = 'X'
	position_error = 0
	move_number = 0
	positions_list = ['top-L', 'top-M', 'top-R',
			  'mid-L', 'mid-M', 'mid-R',
			  'low-L', 'low-M', 'low-R']

	for i in range(9):
		print(print_board(ttt_board))

		while True:
			while True:
				move = input(f"Turn for player {turn}. Move on which space? ")
				
				# pro error handling
				if ttt_board[move] not in ['X', 'O']:
					break
				else:
					print("That space is taken. Try again.")
					
			# more pro error handling		
			if move not in positions_list:
				position_error += 1
				if position_error == 3:
					print("""				
				Moves not recognized, key in one of the following:

					'top-L' | 'top-M' | 'top-R'
					--------+---------+--------
					'mid-L' | 'mid-M' | 'mid-R'
					--------+---------+--------
					'low-L' | 'low-M' | 'low-R'		

					""")

					position_error = 0
			else:
				position_error = 0
				ttt_board[move] = turn
				move_number += 1
				break

		# check for winner
		if move_number >= 5:
			check_win(print_board, ttt_board)

		# check for draw
		if move_number == 9:
			print(print_board(ttt_board))
			print('...Wait, wut?')
			sys.exit()

		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'
	print(print_board(ttt_board))


if __name__ == "__main__":
	main(ttt_board, print_board, check_win)

# Congratulations, your programming skills have decreased by reading this
