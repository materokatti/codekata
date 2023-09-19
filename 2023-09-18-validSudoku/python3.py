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

        # Row validation
        for row in board :
            if not is_valid(row) :
                return False
            
        # Column validation
        for col in zip(*board):
            if not is_valid(col):
                return False
    
        # Subgrid validation
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # Extracting each 3x3 subgrid and storing it in the 'subgrid' variable
                subgrid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                # Checking the validity of the current subgrid
                if not is_valid(subgrid):
                    return False
                
        # If all columns and subgrids are valid, return True
        return True

