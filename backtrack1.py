class Backtrack:
    # initial variable
    def __init__(self, puzzle, output, flag, start_operator):
        self.puzzle = []
        for letter in range(len(puzzle)):
            self.puzzle.append(puzzle[letter])
        self.past_positions = list([self.puzzle])
        self.start_op = start_operator
        self.past_ops = list([self.start_op])
        self.bound = 10
        self.output = output
        self.flag = int(flag)
        self.final_path = None
        self.final_ops = None

        self.node = 0

    def check_whites(self, check_puzzle):
        # getting total whites
        number_of_whites = 0
        for i in range(len(check_puzzle)):
            if check_puzzle[i] == 'W':
                number_of_whites += 1
        # checking if whites are on the left
        count = 0
        for i in range(len(check_puzzle)):
            if check_puzzle[i] == 'W':
                count += 1
            elif check_puzzle[i] == 'B':
                break
        if count == number_of_whites:
            print('Found a solution:')
            return True
        else:
            return False

    def operators(self, puzzle, op):
        new_puzzle = list(puzzle)
        position_e = new_puzzle.index('E')
        if op == '1L':
            new_puzzle[position_e], new_puzzle[position_e-1] = new_puzzle[position_e-1], new_puzzle[position_e]
        elif op == '2L':
            new_puzzle[position_e], new_puzzle[position_e-2] = new_puzzle[position_e-2], new_puzzle[position_e]
        elif op == '3L':
            new_puzzle[position_e], new_puzzle[position_e-3] = new_puzzle[position_e-3], new_puzzle[position_e]
        elif op == '1R':
            new_puzzle[position_e], new_puzzle[position_e+1] = new_puzzle[position_e+1], new_puzzle[position_e]
        elif op == '2R':
            new_puzzle[position_e], new_puzzle[position_e+2] = new_puzzle[position_e+2], new_puzzle[position_e]
        elif op == '3R':
            new_puzzle[position_e], new_puzzle[position_e+3] = new_puzzle[position_e+3], new_puzzle[position_e]
        return new_puzzle

    def find_possible_actions(self, puzzle):
        position_e = puzzle.index('E')
        prioritised_possible_actions = []

        if position_e == 0:
            prioritised_possible_actions = ['3R', '2R', '1R']
        elif position_e == 1:
            prioritised_possible_actions = ['3R', '2R', '1R', '1L']
        elif position_e == 2:
            prioritised_possible_actions = ['3R', '2R', '2L', '1R', '1L', ]
        elif position_e == 3:
            prioritised_possible_actions = ['3R', '3L', '2R', '2L', '1R', '1L']
        elif position_e == 4:
            prioritised_possible_actions = ['3L', '2R', '2L', 'R', '1L']
        elif position_e == 5:
            prioritised_possible_actions = ['3L', '2L', '1R', '1L']
        elif position_e == 6:
            prioritised_possible_actions = ['3L', '2L', '1L']

        return prioritised_possible_actions [::-1]

    def backtrack(self, new_positions, operator):
        # checking if current puzzle has been visited
        current_puzzle = new_positions[-1]
        # print('current puzzle', current_puzzle, 'new position', new_positions)
        for j in range(len(new_positions)-1):
            if current_puzzle == new_positions[j]:

                if self.flag != 0:
                    # print('ANCESTOR\n', file=self.output)
                    self.output.write("ANCESTOR\n")
                return False
        # checking if goal state reached
        if self.check_whites(current_puzzle) is True:
            #print(new_positions)
            return True

        # checking bound
        if len(new_positions) > self.bound:
            if self.flag != 0:
                # print('BOUND\n', file=self.output)
                self.output.write("BOUND\n")
            return False
        # getting all possible swaps for current puzzle
        possible_positions = self.find_possible_actions(current_puzzle)

        for ops in range(len(possible_positions)+1):
            if possible_positions == []:
                if self.flag != 0:
                    # print('NO MORE OPS\n', file=self.output)
                    self.output.write("NO MORE OPS\n")
                return False
            op = possible_positions.pop()

            new_puzzle = list(self.operators(current_puzzle, op))
            self.node += 1
            new_past_positions = list(new_positions)
            new_past_positions.append(new_puzzle)

            new_past_ops = list(operator)
            new_past_ops.append(op)



            if self.flag != 0:
                # print(op, 'N' + str(self.node), '\nAvailable:', possible_positions, '\nPast:', operator, '\n', file=self.output)
                self.output.write(str(op) + " N" + str(self.node) +  "\nAvailable:" + str(possible_positions) +  "\nPast:" + str(operator) +  "\n")
                self.flag -= 1
            #self.past_ops.append([op])
            path = self.backtrack(new_past_positions, new_past_ops)
            if path:
                if self.final_path is None:
                    self.final_path = new_positions
                    self.final_path.append(new_puzzle)
                    self.final_ops = new_past_ops
                    self.final_ops.append(op)
                else:
                    return True

                return True

    def output(self):
        return
