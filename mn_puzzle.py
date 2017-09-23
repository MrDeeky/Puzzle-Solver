from puzzle import Puzzle
import copy


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    def __eq__(self, other):
        """
        Return True if and only if MNPuzzle self is equivalent to other.

        @type self: MNPuzzle
        @type other: MNPuzzle|Any
        @rtype: bool

        >>> target_grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid1 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mnp1 = MNPuzzle(start_grid1, target_grid1)
        >>> target_grid2 = (("1", "4", "5"), ("3", "2", "*"))
        >>> start_grid2 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mnp2 = MNPuzzle(start_grid2, target_grid2)
        >>> target_grid3 = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid3 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mnp3 = MNPuzzle(start_grid3, target_grid3)
        >>> mnp1 == mnp2
        False
        >>> mnp1 == mnp3
        True
        """
        return (type(self) == type(other) and
                self.from_grid == other.from_grid and
                self.to_grid == other.to_grid)

    def __str__(self):
        """
        Return a user-friendly representation of MNPuzzle self.

        @type self: MNPuzzle
        @rtype: str

        >>> target_grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid1 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mnp1 = MNPuzzle(start_grid1, target_grid1)
        >>> print(mnp1)
        * 2 3
        1 4 5
        """
        puzzle = ""
        for rows in self.from_grid:
            for row in rows:
                puzzle += row + " "
            puzzle = puzzle[0:-1]
            puzzle += "\n"
        return puzzle[0:-1]

    def index_of_space(self):
        """
        Return a the location of the empty space in MNPuzzle self.

        @type self: MNPuzzle
        @rtype: tuple

        >>> target_grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid1 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mnp1 = MNPuzzle(start_grid1, target_grid1)
        >>> mnp1.index_of_space()
        (0, 0)
        """
        for i in range(self.n):
            for j in range(self.m):
                if self.from_grid[i][j] == "*":
                    return tuple([i, j])

    def convert_tuple(self):
        """
        Convert the from_grid self into a list and return it.

        @type self: MNPuzzle
        @rtype: list

        >>> target_grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid1 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mnp1 = MNPuzzle(start_grid1, target_grid1)
        >>> print(mnp1.convert_tuple())
        [['*', '2', '3'], ['1', '4', '5']]
        """
        puzzle_list = copy.deepcopy(self.from_grid)
        return [list(x) for x in puzzle_list]

    def convert_list(self, puzzle_list):
        """
        Convert a given puzzle_list into a tuple and return it.

        @type self: MNPuzzle
        @type puzzle_list: list
        @rtype: tuple

        >>> target_grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid1 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mnp1 = MNPuzzle(start_grid1, target_grid1)
        >>> print(mnp1.convert_list([[1,2,3], [4,5,6]]))
        ((1, 2, 3), (4, 5, 6))
        """
        puzzle_tuple = copy.deepcopy(puzzle_list)
        return tuple([tuple(x) for x in puzzle_tuple])

    def row_configs(self):
        """
        Return the configurations obtained by making horizontal changes.

        @type self: MNPuzzle
        @rtype: list[MNPuzzle]

        >>> target_grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid1 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mnp1 = MNPuzzle(start_grid1, target_grid1)
        >>> row_extensions = mnp1.row_configs()
        >>> for puzzles in row_extensions: print(puzzles)
        2 * 3
        1 4 5
        """
        configurations = []
        empty_index = self.index_of_space()
        n_value = empty_index[0]
        m_value = empty_index[1]
        if m_value + 1 < self.m:
            new_grid = self.convert_tuple()
            new_grid[n_value][m_value] = new_grid[n_value][m_value + 1]
            new_grid[n_value][m_value + 1] = "*"
            configurations.append(MNPuzzle(self.convert_list(new_grid),
                                           self.to_grid))
        if m_value - 1 >= 0:
            new_grid = self.convert_tuple()
            new_grid[n_value][m_value] = new_grid[n_value][m_value - 1]
            new_grid[n_value][m_value - 1] = "*"
            configurations.append(MNPuzzle(self.convert_list(new_grid),
                                           self.to_grid))
        return configurations

    def col_configs(self):
        """
        Return the configurations obtained by making vertical changes.

        @type self: MNPuzzle
        @rtype: list[MNPuzzle]

        >>> target_grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid1 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mnp1 = MNPuzzle(start_grid1, target_grid1)
        >>> col_extensions = mnp1.col_configs()
        >>> for puzzles in col_extensions: print(puzzles)
        1 2 3
        * 4 5
        """
        configurations = []
        empty_index = self.index_of_space()
        n_value = empty_index[0]
        m_value = empty_index[1]
        if n_value + 1 < self.n:
            new_grid = self.convert_tuple()
            new_grid[n_value][m_value] = new_grid[n_value + 1][m_value]
            new_grid[n_value + 1][m_value] = "*"
            configurations.append(MNPuzzle(self.convert_list(new_grid),
                                           self.to_grid))
        if n_value - 1 >= 0:
            new_grid = self.convert_tuple()
            new_grid[n_value][m_value] = new_grid[n_value - 1][m_value]
            new_grid[n_value - 1][m_value] = "*"
            configurations.append(MNPuzzle(self.convert_list(new_grid),
                                           self.to_grid))
        return configurations

    def extensions(self):
        """
        Return legal extensions of MNPuzzle self by swapping one symbol to
        the left, right, above, or below "*" with "*".

        @type self: MNPuzzle
        @rtype: list[MNPuzzle]

        >>> target_grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid1 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mnp1 = MNPuzzle(start_grid1, target_grid1)
        >>> len(mnp1.extensions())
        2
        """
        return self.row_configs() + self.col_configs()

    def is_solved(self):
        """
        Return True if and only if the current configuration of MNPuzzle self
        is solved (from_grid is equivalent to to_grid).

        @type self: MNPuzzle
        @rtype: bool

        >>> target_grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid1 = (("*", "2", "3"), ("1", "4", "5"))
        >>> mnp1 = MNPuzzle(start_grid1, target_grid1)
        >>> target_grid2 = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid2 = (("1", "2", "3"), ("4", "5", "*"))
        >>> mnp2 = MNPuzzle(start_grid2, target_grid2)
        >>> mnp1.is_solved()
        False
        >>> mnp2.is_solved()
        True
        """
        return self.from_grid == self.to_grid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
