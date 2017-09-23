from puzzle import Puzzle
import copy


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    def __eq__(self, other):
        """
        Return whether GridPegSolitairePuzzle self is equivalent to other.

        @type self: GridPegSolitairePuzzle
        @type other: GridPegSolitairePuzzle | Any
        @rtype: bool

        >>> grid1 = [["*", "*", "*", "*", "*"], \
                     ["*", "*", "*", "*", "*"], \
                     ["*", "*", "*", "*", "*"], \
                     ["*", "*", ".", "*", "*"], \
                     ["*", "*", "*", "*", "*"]]
        >>> gpsp1 = GridPegSolitairePuzzle(grid1, {"*", ".", "#"})
        >>> grid2 = [["*", "*", "*", "*", "*"], \
                     ["*", "*", "*", "*", "*"], \
                     ["*", "*", "*", "*", "*"], \
                     ["*", "*", ".", "*", "*"], \
                     ["*", "*", "*", "*", "*"]]
        >>> gpsp2 = GridPegSolitairePuzzle(grid2, {"*", ".", "#"})
        >>> gpsp1 == gpsp2
        True
        >>> grid3 = [["*", "*", "*", "*", "*"], \
                     ["*", "*", "*", "*", "*"], \
                     ["*", "*", ".", "*", "*"], \
                     ["*", ".", ".", ".", "*"], \
                     ["*", "*", "*", "*", "*"]]
        >>> gpsp3 = GridPegSolitairePuzzle(grid3, {"*", ".", "#"})
        >>> gpsp1 == gpsp3
        False
        """
        return (type(self) == type(other) and self._marker == other._marker and
                self._marker_set == other._marker_set)

    def __str__(self):
        """
        Return a user friendly representation of GridPegSolitairePuzzle self.

        @type self: GridPegSolitairePuzzle
        @rtype: str

        >>> grid = [["*", "*", "*", "*", "*"], \
                    ["*", "*", "*", "*", "*"], \
                    ["*", "*", "*", "*", "*"], \
                    ["*", "*", ".", "*", "*"], \
                    ["*", "*", "*", "*", "*"]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> print(gpsp)
        * * * * *
        * * * * *
        * * * * *
        * * . * *
        * * * * *
        """
        puzzle = ""
        for rows in self._marker:
            for row in rows:
                puzzle += row + " "
            puzzle = puzzle[0:-1]
            puzzle += "\n"
        return puzzle[0:-1]

    def row_configs(self, cols, rows):
        """
        Return the configurations obtained by moving pegs horizontally.

        @type self: GridPegSolitairePuzzle
        @type cols: int
        @type rows: int
        @rtype: list[GridPegSolitairePuzzle]

        >>> grid = [["*", "*", "*", "*", "*"], \
                    ["*", "*", "*", "*", "*"], \
                    ["*", "*", "*", "*", "*"], \
                    [".", "*", "*", "*", "*"], \
                    ["*", "*", "*", "*", "*"]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> row_extensions = gpsp.row_configs(5, 5)
        >>> for puzzles in row_extensions: print(puzzles)
        * * * * *
        * * * * *
        * * * * *
        * . . * *
        * * * * *
        """
        configs = []
        for i in range(cols):
            for j in range(rows):
                if self._marker[i][j] == ".":
                    if (j - 2 >= 0 and self._marker[i][j - 2] == "*" and
                       self._marker[i][j - 1] == "*"):
                        new_marker = copy.deepcopy(self._marker)
                        new_marker[i][j] = "*"
                        new_marker[i][j-2] = "."
                        new_marker[i][j-1] = "."
                        configs.append(GridPegSolitairePuzzle(new_marker,
                                                              self._marker_set))
                    if (j + 2 < rows and self._marker[i][j+2] == "*" and
                       self._marker[i][j+1] == "*"):
                        new_marker = copy.deepcopy(self._marker)
                        new_marker[i][j] = "*"
                        new_marker[i][j+2] = "."
                        new_marker[i][j+1] = "."
                        configs.append(GridPegSolitairePuzzle(new_marker,
                                                              self._marker_set))
        return configs

    def col_configs(self, cols, rows):
        """
        Return the configurations obtained by moving pegs vertically.

        @type self: GridPegSolitairePuzzle
        @type cols: int
        @type rows: int
        @rtype: list[GridPegSolitairePuzzle]

        >>> grid = [["*", "*", "*", "*", "*"], \
                    ["*", "*", "*", "*", "*"], \
                    ["*", "*", "*", "*", "*"], \
                    ["*", "*", ".", "*", "*"], \
                    ["*", "*", "*", "*", "*"]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> col_extensions = gpsp.col_configs(5, 5)
        >>> for puzzles in col_extensions: print(puzzles)
        * * * * *
        * * . * *
        * * . * *
        * * * * *
        * * * * *
        """
        configs = []
        for i in range(cols):
            for j in range(rows):
                if self._marker[i][j] == ".":
                    if (i - 2 >= 0 and self._marker[i - 2][j] == "*" and
                       self._marker[i - 1][j] == "*"):
                        new_marker = copy.deepcopy(self._marker)
                        new_marker[i][j] = "*"
                        new_marker[i - 2][j] = "."
                        new_marker[i - 1][j] = "."
                        configs.append(GridPegSolitairePuzzle(new_marker,
                                                              self._marker_set))
                    if (i + 2 < cols and self._marker[i + 2][j] == "*" and
                       self._marker[i + 1][j] == "*"):
                        new_marker = copy.deepcopy(self._marker)
                        new_marker[i][j] = "*"
                        new_marker[i + 1][j] = "."
                        new_marker[i + 2][j] = "."
                        configs.append(GridPegSolitairePuzzle(new_marker,
                                                              self._marker_set))
        return configs

    def extensions(self):
        """
        Return all possible configurations that can be reached by making a
        single jump from GridPegSolitairePuzzle self.

        @type self: GridPegSolitairePuzzle
        @rtype: list[GridPegSolitairePuzzle]
        >>> grid = [["*", "*", "*", "*", "*"], \
                    ["*", "*", "*", ".", "*"], \
                    ["*", "*", "*", "*", "*"], \
                    ["*", "*", ".", "*", "*"], \
                    [".", "*", "*", "*", "*"]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> len(gpsp.extensions())
        7
        """
        m = len(self._marker)
        n = len(self._marker[0])
        return self.row_configs(m, n) + self.col_configs(m, n)

    def is_solved(self):
        """
        Return True if and only if GridPegSolitairePuzzle self is solved.

        @type self: GridPegSolitairePuzzle
        @rtype: bool

        >>> grid = [[".", ".", ".", ".", "."], \
                    [".", ".", ".", ".", "."], \
                    [".", ".", "*", ".", "."], \
                    [".", ".", ".", ".", "."], \
                    [".", ".", ".", ".", "."]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> gpsp.is_solved()
        True
        >>> grid2 = [["*", "*", "*", "*", "*"], \
                    ["*", "*", "*", "*", "*"], \
                    ["*", "*", "*", "*", "*"], \
                    ["*", "*", ".", "*", "*"], \
                    ["*", "*", "*", "*", "*"]]
        >>> gpsp2 = GridPegSolitairePuzzle(grid2, {"*", ".", "#"})
        >>> gpsp2.is_solved()
        False
        """
        m = len(self._marker)
        n = len(self._marker[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if self._marker[i][j] == "*":
                    count += 1
        return count == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
