HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x == 0:
        return 0
    return (1 if x % 10 == 8 else 0) + num_eights(x // 10)   #pay attention  to the ternary operator priorities


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    '''if n <= 2:  不让赋值TLE了.... dp[i] = dp[i - 2] if check() == True else 2 * dp[i - 1] - dp[i - 2]：
        return n
    if num_eights(n - 1) or (n - 1) % 8 == 0:
        return pingpong(n - 2)
    else:
        return 2 * pingpong(n - 1) - pingpong(n - 2)'''

    def help(idx, ans, factor):    #新建一个help函数, 想不到啊...nb!
        if idx == n:
            return ans
        if num_eights(idx) or idx % 8 == 0:
            return help(idx + 1, ans - factor, -factor)
        else:
            return help(idx + 1, ans + factor, factor)
    return help(1, 1, 1)


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def help(pre_number, now_value):  #新建help函数如此好用hh
        if now_value == 0:
            return 0
        return max(0, pre_number - now_value % 10 - 1) + help(now_value % 10, now_value // 10)
        #for the case that pre_number would equal to the now_value mod 10, so use the max function to avoid negative value
    return help(n % 10, n // 10)


def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    '''reference: textbook 1.7 count_partitions 照着写就ok'''
    '''use the minimum OR without the minimum'''

    def help(n, m):  #n:总数， m:最小分割数
        if n == 0:
            return 1
        if n < 0:
            return 0
        if m == None:
            return 0
        return help(n - m, m) + help(n, next_largest_coin(m))
    return help(total, 1)




from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda n: f(f, n))(
            lambda a, n: mul(n, a(a, sub(n, 1))) if n > 1 else 1)
