# Q2: Jacket Weather?
def wears_jacket_with_if(temp, raining):
    """
    Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
    Write a function that takes in the current temperature and a boolean value telling 
    if it is raining. This function should return True if Alfonso will wear a jacket and 
    False otherwise.

    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    if temp < 60 or raining:
        return True
    else:
        return False


# Q4: Is Prime?
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    assert n > 0
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Q5: Fizzbuzz
def fizzbuzz(n):
    """Implement the fizzbuzz sequence, which prints out a single statement for 
    each number from 1 to n. For a number i,

    If i is divisible by 3 only, then we print "fizz".
    If i is divisible by 5 only, then we print "buzz".
    If i is divisible by both 3 and 5, then we print "fizzbuzz".
    Otherwise, we print the number i by itself.

    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

# Q6: Unique Digits


def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    cnt = 0
    while n:
        cnt += 1 if not has_digit(n // 10, n % 10) else cnt
        n //= 10
    return cnt


def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"
    while n:
        if n % 10 == k:
            return True
        n //= 10
    return False
