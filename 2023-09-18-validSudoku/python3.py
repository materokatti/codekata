class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def is_valid(arr):
            # Create a new list 'nums' by filtering out '.' and
            # numbers greater than 9 from the input array 'arr'
            nums = [x for x in arr if x != '.' and (1 <= int(x) <= 9)]
            
            # Return True if the length of the set of 'nums' is equal to the length of the list 'nums'
            # Converting 'nums' to a set removes duplicates, 
            # so if any duplicates were present, the lengths will not match
            return len(nums) == len(set(nums))

        #check row
        for row in board :
            if not is_valid(row) :
                return False
            
        #check column

        #check grid
