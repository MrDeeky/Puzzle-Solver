from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

    def __eq__(self, other):
        """
        Return True if and only if WordLadderPuzzle self is equivalent to other.

        @type self: WordLadderPuzzle
        @type other: WordLadderPuzzle|Any
        @rtype: bool

        >>> set1 = {'life', 'eternal', 'universe'}
        >>> w1 = WordLadderPuzzle("same", "cost", set1)
        >>> set2 = {'tom', 'harry', 'bob'}
        >>> w2 = WordLadderPuzzle("time", "real", set2)
        >>> set3 = {'life', 'eternal', 'universe'}
        >>> w3 = WordLadderPuzzle("same", "cost", set3)
        >>> w1 == w2
        False
        >>> w1 == w3
        True
        """
        return (type(self) == type(other) and
                self._from_word == other._from_word and
                self._to_word == other._to_word and
                self._word_set == other._word_set)

    def __str__(self):
        """
        Return a user friendly representation of WordLadderPuzzle self.

        @type self: WordLadderPuzzle
        @rtype: str

        >>> set1 = {'life', 'eternal', 'universe'}
        >>> w1 = WordLadderPuzzle("same", "cost", set1)
        >>> print(w1)
        same -> cost
        >>> w2 = WordLadderPuzzle("cost", "cost", set1)
        >>> print(w2)
        cost -> cost
        """
        word_ladder = self._from_word + " -> " + self._to_word
        return word_ladder

    def extensions(self):
        """
        Return a list of all possible legal extensions of WordLadderPuzzle self
        that can be reached by changing a single letter in the existing
        _from_word.

        @type self: WordLadderPuzzle
        @rtype: list[WordLadderPuzzle]

        >>> set1 = {'lame', 'came', 'some', 'word', 'lost'}
        >>> w1 = WordLadderPuzzle("same", "cost", set1)
        >>> len(w1.extensions())
        3
        """
        configurations = []
        for i in range(len(self._from_word)):
            configurations += \
                [WordLadderPuzzle(self._from_word[:i] + x +
                                  self._from_word[i+1:],
                                  self._to_word, self._word_set)
                 for x in set(self._chars) - set(self._from_word[i])
                 if self._from_word[:i] + x +
                 self._from_word[i+1:] in self._word_set]
        return configurations

    def is_solved(self):
        """
        Return True if and only if WordLadderPuzzle self is solved (_from_word
        is equivalent to _to_word).

        @type self: WordLadderPuzzle
        @rtype: bool

        >>> set1 = {'time', 'space', 'travel', 'world', 'stars'}
        >>> w1 = WordLadderPuzzle("same", "cost", set1)
        >>> w1.is_solved()
        False
        >>> w2 = WordLadderPuzzle("cost", "cost", set1)
        >>> w2.is_solved()
        True
        """
        return self._from_word == self._to_word


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words.txt", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("heaps", "sheep", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
