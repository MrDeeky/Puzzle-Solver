"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque
# set higher recursion limit
# which is needed in PuzzleNode.__str__
# you may uncomment the next lines on a unix system such as CDF
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)


def get_parent(bottom_node):
    """
    Continuously establishes a link between a PuzzleNode and its parent until a
    node is found that does not have a parent. That node is then returned.

    @type bottom_node: PuzzleNode
    @rtype: PuzzleNode
    """
    x = bottom_node
    while bottom_node.parent is not None:
        bottom_node = bottom_node.parent
        bottom_node.children = [x]
        x = bottom_node
    return bottom_node


def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    extensions = deque()
    extensions.append(PuzzleNode(puzzle))
    done = False
    configuration = PuzzleNode()
    visited = set()
    while len(extensions) != 0 and not done:
        configuration = extensions.pop()
        if str(configuration.puzzle) not in visited:
            if configuration.puzzle.is_solved():
                done = True
            else:
                configs = configuration.puzzle.extensions()
                for i in range(len(configs)-1, -1, -1):
                    extensions.append(PuzzleNode(configs[i],
                                                 parent=configuration))
            visited.add(str(configuration.puzzle))
    if done:
        return get_parent(configuration)
    else:
        return None


def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    extensions = deque()
    extensions.append(PuzzleNode(puzzle))
    done = False
    configuration = PuzzleNode()
    visited = set()
    while len(extensions) != 0 and not done:
        configuration = extensions.popleft()
        if str(configuration.puzzle) not in visited:
            if configuration.puzzle.is_solved():
                done = True
            else:
                for configs in configuration.puzzle.extensions():
                    extensions.append(PuzzleNode(configs, parent=configuration))
            visited.add(str(configuration.puzzle))
    if done:
        return get_parent(configuration)
    else:
        return None


# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.
class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether Puzzle self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))
