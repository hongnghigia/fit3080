#!/usr/bin/python2.7

import sys
import writer

def solvepuzzle():
	split_puzzle = sys.argv

	# parsing the input into sections
	puzzle_string = split_puzzle[1]

	procedure_name = split_puzzle[2]

	output_file = split_puzzle[3]
	flag = split_puzzle[4]

	# 0 is for the cost of the path at the current state
	state = [puzzle_string, white_number(puzzle_string), current_empty_pos(puzzle_string), 0]
	stateList = [state]

	# global Writer = new Writer(output_file)

	if procedure_name == "BK":
		backtrack(stateList)

	"""
	else procedure_name == "DLS":
		graph_search(puzzle)
	"""



####################
# The backtracking algorithm
#
# @param: 	white - int, the number of whites on the left of the first black
#			black - int, the number of blacks on the left of the first white
#			empty - int, the position of the current empty tile in the array
#			operator - list, the list of possible moves the empty tile can make
#
def backtrack(stateList):

	state = list(stateList[0])
	bound = 10
	total = state[3]

	# if the current state of the puzzle is the solution
	if found_solution(state[1]):
		print "Solution found"
		print state
		return True

	# if visiting an already visited state
	if state in stateList[1:]:
		return False

	# if bound reached
	if len(stateList) > bound:
		return False

	operators = possible_moves(state[2])

	while len(stateList) != 0:
		if len(operators) == 0:
			return False

		op = operators.pop()
		new_empty_pos = state[2] + op

		if op == 3 | op == -3:
			total = total + 2
		else:
			total += 1

		new_state = move(new_empty_pos, state, total)

		stateList.insert(0, new_state)

		path = backtrack(stateList)

		if path:
			print state
			# print op
			return path
		else:
			del stateList[0]


################
# Move the empty tile accordingly
#
# @param: 	new_empty_pos - new position of the empty tile
#			state - current state of the puzzle
# @return: 	[new_state, white, new_empty_pos]
def move(new, state, cost):
	new_state = list(state[0])
	old = state[2]

	new_state[old], new_state[new] = new_state[new], new_state[old]

	white = white_number(new_state)
	return [new_state, white, new, cost]


################
# Find all the possbile movements the empty tile can make of the current state of puzzle
#
# @param: 	puzzle - list, the current puzzle
#
def possible_moves(current_empty):
	lower_bound = 0
	upper_bound = 6
	possible_moves = []

	for i in range(1,4):
		if not (current_empty-i < lower_bound):
			possible_moves.append(-i)

		if not (current_empty+i > upper_bound):
			possible_moves.append(i)


	return possible_moves



###################
# Check whether the current state of the puzzle is the solution
#
# @param:	puzzle - list, the current puzzle
# @return: 	True - if current state is the solution
#			False - if current state is not  the solution
#
def found_solution(check):
	if check == 3:
		return True
	else:
		return False

####################
# Finding the position of the empty tile in the puzzle
#
# @param:	puzzle - list, the current puzzle
# @return: 	i - int, the position in the puzzle
#
def current_empty_pos(puzzle):
	for i in range(len(puzzle)):
		if puzzle[i] == "E":
			return i


###################
# Counting the number of whites until first black if puzzle starts with white
#
# @param:	puzzle - list, the current puzzle
# @return: 	state - dict, dictionary contains number of whites on far left
#
def white_number(puzzle):
	# clone the puzzle list
	tmp = list(puzzle)
	tmp.remove("E")

	# if black starts
	if tmp[0] == "B":
		return 0

	# if white starts
	elif tmp[0] == "W":
		white_count = 0
		for i  in range(0,len(puzzle)):
			if tmp[i] == "W":
				white_count += 1
			else:
				return white_count


# def graph_search(puzzle):

solvepuzzle()
