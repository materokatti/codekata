from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # If the list is empty, return 0
        if not nums:
            return 0
        
        # Initialize the left pointer to 0
        left = 0
        # Initialize a variable to keep track of the current sum of the subarray
        current_sum = 0
        # Initialize a variable to keep track of the minimum length of the subarray (initialized to infinity so any valid length will be smaller)
        min_length = float('inf')
        
        # Move the right pointer from the start to the end of the array
        for right in range(len(nums)):
            # Add the current element to the current sum
            current_sum += nums[right]
            # While the current sum is greater or equal to the target, keep moving the left pointer to find the minimum length subarray
            while current_sum >= target:
                # Update the minimum length if a smaller length is found
                min_length = min(min_length, right - left + 1)
                # Subtract the value at the left pointer from the current sum and move the left pointer by one position
                current_sum -= nums[left]
                left += 1
        
        # If a valid subarray was found (min_length is not infinity), return the minimum length found, otherwise return 0 (no valid subarray found)
        return min_length if min_length != float('inf') else 0
