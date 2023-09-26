class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to hold the left parentheses, braces, and brackets.
        stack = []
        
        # Define a mapping of the right to the corresponding left parentheses, braces, and brackets.
        mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate over each character in the string.
        for char in s:
            # If the character is one of the left parentheses, braces, or brackets,
            # push it onto the stack.
            if char in mapping.values():
                stack.append(char)
            # If the character is one of the right parentheses, braces, or brackets,
            # pop the top element from the stack and check if it matches the corresponding left one.
            elif char in mapping.keys():
                # If the stack is not empty, pop the top element.
                # If the stack is empty, assign a placeholder that will never match any valid character.
                top_element = stack.pop() if stack else '#'
                
                # If the popped element does not match the corresponding left parenthesis, brace, or bracket,
                # the string is not valid.
                if mapping[char] != top_element:
                    return False
                    
        # If the stack is empty at the end, the string is valid.
        # Otherwise, there are unmatched left parentheses, braces, or brackets, and the string is not valid.
        return not stack
