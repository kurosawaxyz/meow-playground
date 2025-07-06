from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Fit conditions
        cond1 = True if 2 <= len(nums) <= 10**4 else False
        cond2 = True if sum([True for i in range(len(nums)) if -10**9 <= nums[i] <= 10**9]) else False
        cond3 = True if -10**9 <= target <= 10**9 else False

        valid = cond1 and cond2 and cond3
        if valid: 
            from itertools import combinations

            enumerated = [list(i) for i in combinations(list(range(len(nums))), 2)]
            import numpy as np
            fitted = [
                enumerated[i] for i in range(len(enumerated)) if sum(np.array(nums)[enumerated[i]]) == target
            ]
            if len(fitted) > 1:
                raise ValueError("More than 1 solution possible")

            else: 
                return fitted[0]

        else: 
            raise ValueError("Invalid input")
            
        