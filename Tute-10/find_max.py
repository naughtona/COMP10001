from typing import List

def find_max_r(nums: List) -> int:
    ''' uses recursion to scan over `nums` in search of max
        
        `nums`:     a non-empty, unsorted list of numbers 
        returns:    the maximum number in `nums`
    '''
    # base case
    if len(nums) == 1:
        return nums[0]
    # recursive case
    else:
        # find the max on a subset of `nums`
        subset_max = find_max_r(nums[1:])

        # compare `subset_max` with nums[0]
        if nums[0] > subset_max:
            return nums[0]
        else:
            return subset_max

def find_max_i(nums: List) -> int:
    ''' uses iteration to scan over `nums` in search of max

        `nums`:     a non-empty, unsorted list of numbers
        returns:    the maximum number in `nums`
    '''
    # initially set max to first number in `nums`
    max_n = nums[0]

    for num in nums[1:]:
        # compare and update if new max found
        if num > max_n:
            max_n = num
    
    return max_n