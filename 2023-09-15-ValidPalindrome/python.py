class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Increment left index while ignoring non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            
            # Decrement right index while ignoring non-alphanumeric characters
            while left < right and not s[right].isalnum():
                right -= 1
            
            # If the characters at left and right are not equal (ignoring case), return false
            if s[left].lower() != s[right].lower():
                return False
            
            # Move towards the middle
            left += 1
            right -= 1
        
        # The string is a palindrome
        return True
