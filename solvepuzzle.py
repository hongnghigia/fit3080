#!/usr/bin/python3.5
import sys
from writer import Writer
from tree import Tree
from treenode import Node
from backtrack1 import Backtrack


def solvepuzzle():
	split_puzzle = sys.argv

	# parsing the input into sections
	puzzle_string = split_puzzle[1]

	procedure_name = split_puzzle[2]

	o_file = split_puzzle[3]

	output_file = open(o_file+".txt", "a")


	# 0 is for the cost of the path at the current state, also the operator
	# [puzzle, op, cost]
	state = [puzzle_string, 0, 0]
	stateList = [state]

	global flag
	flag = int(split_puzzle[4])

	global total_white_no
	total_white_no = total_white(puzzle_string)

	global writer1
	writer1 = Writer(o_file)

	if procedure_name == "BK":

	    print("backtrack")
	    start_op = ["start"]
	    solve_puzzle = Backtrack(puzzle_string, output_file, flag, start_op)
	    solve_puzzle.backtrack(solve_puzzle.past_positions, solve_puzzle.start_op)
	    cost = 0
	    for i in range(len(solve_puzzle.final_path)):
			string1 = ''.join(solve_puzzle.final_path[i])
			# print(solve_puzzle.final_ops[i], '\t', string1,'\t', cost, file=output_file)
			output_file.write(str(solve_puzzle.final_ops[i])+ '\t'+ str(string1)+'\t'+ str(cost))

			print(solve_puzzle.final_ops[i], string1, cost)
			try:
				calc_cost = abs(solve_puzzle.final_path[i].index('E') - solve_puzzle.final_path[i+1].index('E'))
				if calc_cost > 1:
				    cost += calc_cost - 1
				else:
				    cost += calc_cost
			except IndexError:
				pass
			print(solve_puzzle.final_ops)

	elif procedure_name == "DLS":
		tree_search(state)

	elif procedure_name == "A":
		a(state)




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
	bound = 7

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

	depth = 10
	while True:
		if len(frontier) == 0:
			print("No solution")
			return False

		currentNode = frontier.pop(0)

		if flag >= 1:
			writer1.writeNode(node,frontier,explored, "EXPANDED")

		# if found solution
		if found_solution(currentNode.getState()):
			print("Solution found")
			print(currentNode.getPath())
			print(currentNode.cost)
			if flag == 0:
				writer1.write(currentNode.op,currentNode.string, currentNode.cost)
				while currentNode.parent != None:
					writer1.write(currentNode.parent.op,currentNode.parent.string, currentNode.parent.cost)
					currentNode = currentNode.parent

			return True




		explored.append(currentNode)


		if len(currentNode.getPath()) < depth:
			operators = possible_moves(currentNode.getState())


			for i in operators:
				new_pos = current_empty_pos(currentNode.getState()) + i
				new_state = move(new_pos, currentNode.getState())


				new_node = tree.makeNode(new_state, i, currentNode.cost, currentNode.getPath(), currentNode)
				new_node.heuristic()

				writer1.writeNewNode(new_node)

				# if state has already been explored
				if not hasSameAncestor(new_node):
					frontier.insert(0, new_node)

"""
	A/A* algorithm, it's the same as tree_search except the frontier list is ordered in a different way using some heuristic function
	@param: 	puzzle - the initial state
"""
def a(puzzle):
	frontier = []
	explored = []
	tree = Tree()
	node = tree.makeNode(puzzle[0], 0, 0, [], None)

	frontier.append(node)

	depth = 10
	while True:
		if len(frontier) == 0:
			print("No solution")
			return False

		frontier = heuristicFuction(frontier)
		currentNode = frontier.pop(0)

		if flag >= 1:
			writer1.writeNode(node,frontier,explored, "EXPANDED")

		# if found solution
		if found_solution(currentNode.getState()):
			print("Solution found")
			print(currentNode.getPath())
			print(currentNode.cost)
			if flag == 0:
				writer1.write(currentNode.op,currentNode.string, currentNode.cost)
				while currentNode.parent != None:
					writer1.write(currentNode.parent.op,currentNode.parent.string, currentNode.parent.cost)
					currentNode = currentNode.parent

			return True




		explored.append(currentNode)


		if len(currentNode.getPath()) < depth:
			operators = possible_moves(currentNode.getState())


			for i in operators:
				new_pos = current_empty_pos(currentNode.getState()) + i
				new_state = move(new_pos, currentNode.getState())


				new_node = tree.makeNode(new_state, i, currentNode.cost, currentNode.getPath(), currentNode)
				new_node.heuristic()

				writer1.writeNewNode(new_node)

				# if state has already been explored
				if not hasSameAncestor(new_node):
					frontier.insert(0, new_node)




def heuristicFuction(frontier):
	frontier.sort(key=lambda x:x.f, reverse=False)

	return frontier


def hasSameAncestor(node):
	string = node.getString()

	while node.parent != None:
		if node.parent.string == string:
			return True
		node = node.parent

	return False


solvepuzzle()
