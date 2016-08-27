

def solvepuzzle():
	puzzle = raw_input("Enter a puzzle: ")
	split_puzzle = puzzle.split()

	# parsing the input into sections
	puzzle_string = list(split_puzzle[1])
	procedure_name = split_puzzle[2]
	output_file = split_puzzle[3]
	flag = split_puzzle[4]

	state = [puzzle_string, white_number(puzzle_string), current_empty_pos(puzzle_string)]
	stateList = [state]


	if procedure_name == "BK":
		backtrack(puzzle_string,stateList)

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
def backtrack(puzzle,stateList):

	state = stateList.pop(0)
	bound = 4

	# if the current state of the puzzle is the solution
	if found_solution(state[0]):
		return True

	# if visiting an already visited state
	if state in stateList:
		return False

	# if bound reached
	if len(stateList) > bound:
		return False

	operators = possible_moves(state[0])
	flag = True
	while flag:
		if len(operators) == 0:
			return False

		op = operators.pop()
		new_empty_pos = empty_pos + op
		new_state = move(new_empty_pos, state)

		stateList.insert(0, new_state)

		path = backtrack(puzzle, stateList)

		if path:
			flag = False

		print path
		return path


################
# Move the empty tile accordingly
#
# @param: 	new_empty_pos - new position of the empty tile
#			state - current state of the puzzle
# @return: 	[new_state, white, new_empty_pos]
def move(new_empty_pos, state):
	new_state = state[0]
	old_empty_pos = state[2]
	new_state[old_empty_pos], new_state[new_empty_pos] = new_state[old_empty_pos], new_state[new_empty_pos]

	white = white_number(new_state)
	return [new_state, white, new_empty_pos]

################
# Find all the possbile movements the empty tile can make of the current state of puzzle
#
# @param: 	puzzle - list, the current puzzle
#
def possible_moves(puzzle):
	lower_bound = 0
	upper_bound = 6
	possible_moves = []
	current_empty = current_empty_pos(puzzle)
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
	if check[0] == 3:
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
# @return: 	state - dict, dictionary contains number of whites and blacks
#
def white_number(puzzle):
	state = []

	# if black starts
	if puzzle[0] == "B":
		state.append(0)
		return state

	# if white starts
	elif puzzle[0] == "W":
		white_count = 1
		for i  in range(1,len(puzzle)):
			if puzzle[i] == "W":
				white_count += 1
			else:
				state.append(white_count)
				return state
	else:
		puzzle.pop(0)
		white_number(puzzle)


# def graph_search(puzzle):

solvepuzzle()
