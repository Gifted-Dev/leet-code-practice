# Problem: https://leetcode.com/problems/product-of-array-except-self/description/
# Category: Array
# Solution: Prefix and Suffix Array Manipulation
# Time Complexity: O(n)
# Space Complexity: O(1)
# Difficulty Level: Medium

"""
could not solve this problem at first try, I had to study the solution
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        prefix = 1
        for i in range(n):
            answer[i] *= prefix
            prefix *= nums[i]
            
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            
        return answer
    
# --------------- TESTING SOLUTION --------------- #
solution = Solution()

nums = [1,5,4,3,2]

answer = solution.productExceptSelf(nums)
print(answer)

nums1 = [1, 2, 3, 4]
answer1 = solution.productExceptSelf(nums1)
print(answer1)


# --------------- HOW DOES THIS TECHNIQUE WORK --------------- #
"""
The Prefix and Suffix Array Manipulation Technique works by taking the sum or products of elements before and after
each position in the list.

It works by performing the Prefix Array (Left Side) and the Suffix Array, the right side.

Prefix Array: As you go from left side to right side, the prefix array contains the product (or sum) of all element
to the left of nums[i]

Suffix Array: As you go from the right sidt to the left, the suffix array contains the product (or sum) of all element
to rigth side of nums[i]

The final result is usually gotten from the combination of the prefix and suffix array.

"""