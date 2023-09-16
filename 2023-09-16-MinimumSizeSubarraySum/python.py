from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sort the input list nums in decreasing order
        nums.sort(reverse=True)
        
        # Initialize an empty list named stack
        self.stack = []
        
        # Print the sorted list
        print(nums)
        
        # If the sum of all numbers in nums is greater than or equal to the target
        if sum(nums) >= target:
            
            # Iterate through each number in nums
            for i in nums:
                
                # If the current number is greater than or equal to the target, return 1 
                # as we have found a subarray of length 1 that satisfies the condition
                if i >= target:
                    return 1
                else:
                    # If the current number is less than the target, add it to the stack
                    self.stack.append(i)
                
                # If the sum of numbers in the stack is greater than or equal to the target,
                # return the length of the stack as we have found a subarray that satisfies the condition
                if sum(self.stack) >= target:
                    return len(self.stack)
        
        # If no subarray is found that satisfies the condition, return 0
        return 0
