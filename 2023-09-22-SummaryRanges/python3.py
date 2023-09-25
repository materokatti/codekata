from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # If the input list is empty, return an empty list.
        if not nums:
            return []
        
        # Initialize the result list and the start and end pointers to the first element of the list.
        result = []
        start = end = nums[0]
        
        # Iterate over the elements of the list starting from the second element.
        for num in nums[1:]:
            # If the current number is consecutive to the previous one, move the end pointer to this number.
            if num == end + 1:
                end = num
            else:
                # If the start and end pointers are pointing to the same number, append this number as a string to the result list.
                if start == end:
                    result.append(str(start))
                else:
                    # If start and end are different, append the range in string format to the result list.
                    result.append(f"{start}->{end}")
                # Move the start and end pointers to the current number.
                start = end = num
        
        # After the iteration, append the last range or number to the result list.
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")
        
        # Return the result list containing the summary ranges.
        return result
