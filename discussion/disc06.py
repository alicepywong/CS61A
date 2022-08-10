class Pet():
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

# Q1: Cat


class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        print(f'{self.name} says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        "*** YOUR CODE HERE ***"
        if self.is_alive:
            self.lives -= 1
        if self.lives == 0:
            self.is_alive = False
            print('This cat has no more lives to lose.')


# Q2: NoisyCat
'''
More cats! Fill in this implementation of a class called NoisyCat, which is 
just like a normal Cat. However, NoisyCat talks a lot: in fact, it talks twice 
as much as a regular Cat! If you'd like to test your code, feel free to copy over 
your solution to the Cat class above.
'''


class NoisyCat(Cat):  # Fill me in!
    """A Cat that repeats things twice."""

    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner, lives)

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        super().talk()
        super().talk()


# Q3: High Score
def best_k_segmenter(k, score):
    """
    >>> largest_digit_getter = best_k_segmenter(1, lambda x: x)
    >>> largest_digit_getter(12345)
    5
    >>> largest_digit_getter(245351)
    5
    >>> largest_pair_getter = best_k_segmenter(2, lambda x: x)
    >>> largest_pair_getter(12345)
    45
    >>> largest_pair_getter(245351)
    53
    >>> best_k_segmenter(1, lambda x: -x)(12345)
    1
    >>> best_k_segmenter(3, lambda x: (x // 10) % 10)(192837465)
    192
    """
    def partitioner(x): return (x//10, x % (10**k))

    def best_getter(n):
        assert n > 0
        best_seg = None
        while n >= 10**k//10:
            n, seg = partitioner(n)
            if best_seg == None or score(seg) > score(best_seg):
                best_seg = seg
        return best_seg
    return best_getter


# Q4: Ten-pairs
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if not n:
        return 0
    return count_digit(n//10, 10-n % 10) + ten_pairs(n//10)


def count_digit(n, digit):
    """Return how many times digit appears in n.
    >>> count_digit(55055, 5)
    4
    """
    "*** YOUR CODE HERE ***"
    if not n:
        return 0
    elif n % 10 == digit:
        return 1+count_digit(n//10, digit)
    else:
        return count_digit(n//10, digit)


# Q5: Making Onions TODO
def make_onion(f, g):
    """
    Write a function make_onion that takes in two one-argument 
    functions, F and G, and returns a function that will take in 
    X, Y, and LIMIT and return True if it is possible to reach Y 
    from X in LIMIT steps or less, via only repeated applications 
    of F and G, and False otherwise.

    >>> add_one = lambda x: x + 1
    >>> mul_by_two = lambda y: y * 2
    >>> can_reach = make_onion(add_one, mul_by_two)
    >>> can_reach(0, 5, 4)      # 5 = add_one(mul_by_two(mul_by_two(add_one(0))))
    True
    >>> can_reach(0, 5, 3)      # Not possible
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)      # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)      # Not possible
    False
    """
    def can_reach(x, y, limit):
        if limit < 0:
            return False
        elif x == y:
            return True
        else:
            return can_reach(f(x), y, limit - 1) or can_reach(g(x), y, limit - 1)
    return can_reach


# Q6: Paths List
def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    >>> paths(5, 3) # There is no valid path from x to y
    []
    """
    if x == y:
        return [[x]]
    elif x > y:
        return []
    else:
        a = paths(x + 1, y)
        b = paths(x * 2, y)
        return [[x] + i for i in a + b]
