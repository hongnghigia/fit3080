#!/usr/bin/python3.5

import sys
from writer import Writer
from tree import Tree
from treenode import Node


def solvepuzzle():
	split_puzzle = sys.argv

	# parsing the input into sections
	puzzle_string = split_puzzle[1]

	procedure_name = split_puzzle[2]

	output_file = split_puzzle[3]
	

	# 0 is for the cost of the path at the current state, also the operator
	# [puzzle, op, cost]
	state = [puzzle_string, 0, 0]
	stateList = [state]

	global flag
	flag = int(split_puzzle[4])

	global total_white_no
	total_white_no = total_white(puzzle_string)

	global writer1
	writer1 = Writer(output_file)

	if procedure_name == "BK":
		backtrack(stateList)

	elif procedure_name == "DLS":
		tree_search(state)




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
	if found_solution(state[0]):
		print("Solution found")
		if flag >= 1:
			writer1.diagWrite(state[1], state[0], state[2], "SOLUTION FOUND")
		elif flag == 0:	
			for i in reversed(stateList):
				writer1.write(i[1], i[0], i[2])

		return True

	# ancestor
	for i in range(1, len(stateList)):
		if stateList[i][0] == state[0]:
			if flag == 0:
				pass
			else:
				writer1.diagWrite(state[1], state[0], state[2],"ANCESTOR")
			return False

	# if bound reached
	if len(stateList) >= bound:
		if flag == 0:
			pass
		else:
			writer1.diagWrite(state[1], state[0], state[2],"BOUND REACHED")
		return False

	operators = possible_moves(state[0])

	while True:
		if len(operators) == 0:
			if flag >= 1:
				writer1.diagWrite(state[1], state[0], state[2],"NO MORE OPS")
			return False

		total = state[2]

		op = operators.pop()
		new_empty_pos = current_empty_pos(state[0]) + op

		if op == 3 or op == -3:
			total = total + 2
		else:
			total += 1


		tmp_state = move(new_empty_pos, state[0])
		new_state = [tmp_state, op, total]

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
def move(new, state):
	new_state = list(state)
	old = current_empty_pos(state)

	new_state[old], new_state[new] = new_state[new], new_state[old]

	white = white_number(new_state)
	return "".join(new_state)


################
# Find all the possbile movements the empty tile can make of the current state of puzzle
#
# @param: 	puzzle - list, the current puzzle
#
def possible_moves(puzzle):
	lower_bound = 0
	upper_bound = 6
	current_empty = current_empty_pos(puzzle)
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
def found_solution(puzzle):
	check = white_number(puzzle)
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

####-*####*####*####*####*####*####*#####*#####*#####*#####*####*#####
# Tree Search algorithm
#
#@param:	puzzle: the puzzle

def tree_search(puzzle):
	frontier = []
	explored = []
	tree = Tree()
	node = tree.makeNode(puzzle[0], 0, 0, [], None)

	frontier.append(node)

	depth = 9
	while True:
		if len(frontier) == 0:
			print("WIEOF")
			return False

		currentNode = frontier.pop(0)

		if found_solution(currentNode.getState()):
			print(currentNode.getPath())
			print(currentNode.cost)
			if flag == 0:
				writer1.write(currentNode.op,currentNode.string, currentNode.cost)
				while currentNode.parent != None:
					writer1.write(currentNode.parent.op,currentNode.parent.string, currentNode.parent.cost)
					currentNode = currentNode.parent

				print("Hello")
			return True


		explored.append(currentNode)

		# print(currentNode.getPath())


		if len(currentNode.getPath()) < depth:
			operators = possible_moves(currentNode.getState())
			

			for i in operators:
				new_pos = current_empty_pos(currentNode.getState()) + i
				new_state = move(new_pos, currentNode.getState())


				new_node = tree.makeNode(new_state, i, currentNode.cost, currentNode.getPath(), currentNode)

				if hasSameAncestor(new_node):
					if flag >= 1:
						writer1.write(currentNode.getOp(),currentNode.getState(), currentNode.getCost(), "ANCESTOR")

				else:
					frontier.insert(0, new_node)
		else:
			if flag >= 1:
				writer1.diagWrite(currentNode.getOp(),currentNode.getState(), currentNode.getCost(), "BOUND REACHED")


def hasSameAncestor(node):
	string = node.getString()

	while node.parent != None:
		if node.parent.string == string:
			return True
		node = node.parent

	return False


solvepuzzle()
