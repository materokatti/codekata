class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Initialize a dictionary to hold the character count for magazine
        magazine_char_count = {}
        
        # Count the characters in the magazine
        for char in magazine:
            if char in magazine_char_count:
                magazine_char_count[char] += 1
            else:
                magazine_char_count[char] = 1
        
        # Count the characters in the ransomNote and check against the magazine count
        for char in ransomNote:
            if char not in magazine_char_count or magazine_char_count[char] == 0:
                return False
            magazine_char_count[char] -= 1
        
        return True

        
