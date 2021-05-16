
def fibonacci_r(n: int) -> int:
    ''' uses recursion to calculate fibonacci number

        `n`:        a non-negative integer
        returns:    the fibonacci number for `n`
    '''
    # base case #1
    if n == 0:
        return 1
    # base case # 2
    elif n == 1:
        return 1
    # recursive case
    else:
        # each `n` is the sum of two preceding ones
        return fibonacci_r(n - 1) + fibonacci_r(n - 2)

def fibonacci_i(n: int) -> int:
    ''' uses iteration to calculate fibonacci number

        `n`:        a non-negative integer
        returns:    the fibonacci number for `n`
    '''
    # fibonacci number accumulator
    fib_n = 1

    fib_0 = f_two_back = 1
    fib_1 = f_one_back = 1

    for _ in range(2, n + 1):
        # each `n` is the sum of two preceding ones
        fib_n = f_one_back + f_two_back

        # update `f_one_back` and `f_two_back`
        f_one_back, f_two_back = fib_n, f_one_back
    
    return fib_n