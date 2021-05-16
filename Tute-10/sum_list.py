from typing import List

def sum_list_r(nums: List) -> int:
    ''' uses recursion to scan over `nums` in search of sum
        
        `nums`:     a list of numbers 
        returns:    the sum of numbers in `nums`
    '''
    # base case
    if len(nums) == 0:
        return 0
    # recursive case
    else:
        # separate out into first element and rest of list
        head, rest = nums[0], nums[1:]

        # recursive call
        return head + sum_list_r(rest)

def sum_list_i(nums: List) -> int:
    ''' uses iteration to scan over `nums` in search of sum

        `nums`:     a list of numbers
        returns:    the sum of numbers in `nums`
    '''
    # initially set sum to 0
    sum_n = 0

    for num in nums:
        sum_n += num
    
    return sum_n