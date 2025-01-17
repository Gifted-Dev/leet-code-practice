# Problem: https://leetcode.com/problems/move-zeroes/description/
# Category: Array
# Solution: Two pointers technique
# Time Complexity: O(n)
# Space Complexity: O(1)

### First Approach
class my_solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)

'''
The issue with the code above is I am modifying the list while iterating over it.
also .remove() is an O(n) operation which is not efficient in shifting elements.

The code below is the best and optimized solution.
- The code tracks the initial indexes and then tracks the list for non_zeros elements
- It iterates over the list without modifying its size
- Instead of appending and removing elements, it swaps non_zero elements
'''

# The Best Approach
class solution:
    def moveZeroes(self, nums):
       non_zero = 0
       
       for i in range(len(nums)):
           if nums[i] != 0:
               nums[non_zero], nums[i] = nums[i], nums[non_zero]
               non_zero += 1

