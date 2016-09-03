#!/usr/bin/python2.7

import sys
from writer import Writer


def solvepuzzle():
	split_puzzle = sys.argv

	# parsing the input into sections
	puzzle_string = split_puzzle[1]

	procedure_name = split_puzzle[2]

	output_file = split_puzzle[3]
	flag = split_puzzle[4]

	# 0 is for the cost of the path at the current state, also the operator
	# [puzzle, no_white, e_pos, op, cost]
	state = [puzzle_string, white_number(puzzle_string), current_empty_pos(puzzle_string), 0, 0]
	stateList = [state]

	global total_white_no
	total_white_no = total_white(puzzle_string)

	global writer1
	writer1 = Writer(output_file)

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

	# if the current state of the puzzle is the solution
	if found_solution(state[1]):
		print "Solution found"
		for i in reversed(stateList):
			op = ""
			if i[3] == 0:
				op = "START"
			elif i[3] == 1:
				op = "1R"
			elif i[3] == 2:
				op = "2R"
			elif i[3] == 3:
				op = "3R"
			elif i[3] == -1:
				op = "1L"
			elif i[3] == -2:
				op = "2L"
			elif i[3] == -3:
				op = "3L"

			writer1.write(op, i[0], i[4])

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

		total = state[4]

		op = operators.pop()
		new_empty_pos = state[2] + op

		if op == 3 or op == -3:
			total = total + 2
		else:
			total += 1


		new_state = move(new_empty_pos, state, op, total)

		stateList.insert(0, new_state)

		path = backtrack(stateList)
		if path:
			return path
		else:
			del stateList[0]


################
# Move the empty tile accordingly
#
# @param: 	new_empty_pos - new position of the empty tile
#			state - current state of the puzzle
# @return: 	[new_state, white, new_empty_pos]
def move(new, state, op, cost):
	new_state = list(state[0])
	old = state[2]

	new_state[old], new_state[new] = new_state[new], new_state[old]

	white = white_number(new_state)
	return ["".join(new_state), white, new, op, cost]


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
	if check == total_white_no:
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


def total_white(puzzle):
	white = 0
	for i in puzzle:
		if i == "W":
			white += 1

	return white

# def graph_search(puzzle):

solvepuzzle()
