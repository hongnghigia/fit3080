

def solvepuzzle():
	puzzle = raw_input("Enter a puzzle: ")
	split_puzzle = puzzle.split()
	
	# parsing the input into sections
	puzzle_string = split_puzzle[1]
	procedure_name = split_puzzle[2]
	output_file = split_puzzle[3]
	flag = split_puzzle[4]
	visited_state = []
	
	if procedure_name == "BK":
		backtrack(puzzle_string,visited_state)
		
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
def backtrack(puzzle,visited_state):

	# (#W, #B, pos(E))
	# number of whites, number of blacks, position of E
	# if number of whites == 3 --> terminate and return the solution
	"""
	state = count_first_colour(puzzle)
	empty_pos = current_empty_pos(puzzle)
	state["E"] = empty_pos
	"""
	move_list = possible_moves(puzzle)
	state = [count_first_colour(puzzle), current_empty_pos(puzzle)]
	
	# if the current state of the puzzle is the solution
	if found_solution(puzzle):
		return True
	
	# if visiting an already visited state
	if state in visited
	for i in range(len(move_list)):
		move = move_list.pop()
		
	
	print move_list


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
###################
def found_solution(puzzle):
	check = count_first_colour(puzzle)
	if check[0] == 3:
		return True
	else:
		return False

####################
# Finding the position of the empty tile in the puzzle
#
# @param:	puzzle - list, the current puzzle
# @return: 	i - int, the position in the puzzle
####################
def current_empty_pos(puzzle):
	for i in range(len(puzzle)):
		if puzzle[i] == "E":
			return i


###################
# Counting the number of whites until first black if puzzle starts with white
# and vice versa
#
# @param:	puzzle - list, the current puzzle
# @return: 	state - dict, dictionary contains number of whites and blacks
###################
def count_first_colour(puzzle):
	state = []
	
	# if black starts
	if puzzle[0] == "B":
		black_count = 1
		for i in range(1,len(puzzle)):
			if puzzle[i] == "B":
				black_count += 1
			else:
				state.append(0)
				state.append(black_count)
				return state
				
	# if white starts			
	elif puzzle[0] == "W":
		white_count = 1
		for i  in range(1,len(puzzle)):
			if puzzle[i] == "W":
				white_count += 1
			else:
				state.append(white_count)
				state.append(0)
				return state
	else:
		puzzle.pop(0)
		count_first_colour(puzzle)
				
 	
# def graph_search(puzzle):

solvepuzzle()
