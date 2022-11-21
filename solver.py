""" Defines a class Solver that takes a sudoku puzzle as a parameter
and has a method solve() that returns either the solved puzzle (if it's solvable)
or an empty array (if it's not). """

class Solver:
    def __init__(self, puzzle) -> None:
        self._puzzle = puzzle
    
    def solve(self):
        for i in range(len(self._puzzle)):
            for i in range(1, 10):
                pass
    
    """ An important operation will be checking if the puzzle 
    is in a valid state. A valid state is defined as one in which there are no
    'contradictions,' i.e. for all rows, columns, and houses, there do not exist 
    any duplicate values. """
    def puzzle_is_valid(self) -> bool:
        pass


