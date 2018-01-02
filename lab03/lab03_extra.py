from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: 10*y+x%10
    while x > 0:
        x, y =x//10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <=2:
        return n
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        "*** YOUR CODE HERE ***"
        if i<=n:
            print(i)
            counter(i+1)
    counter(1)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n==2:
        return True
    def helper(k):
        if n%k==0:
            return False
        elif k*k>=n:
            return True
        else:
            return helper(k+1)
    return helper(2)

    

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if i==1:
            return odd_term(i)
        else:
            if i%2==0:
                this_term=even_term(i)
            else:
                this_term=odd_term(i)
            return this_term+helper(i-1)
    return helper(n)


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
    if n<19:
        return 0
    else:
        return check_last_digit(n//10,n%10)+ten_pairs(n//10)
def check_last_digit(n,digit):
    if n==0:
        return 0
    else:
        if n%10+digit==10:
            return 1+check_last_digit(n//10,digit)
        else:
            return check_last_digit(n//10,digit)
