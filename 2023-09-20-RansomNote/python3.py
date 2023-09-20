class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # First, check if the entire ransomNote is directly contained within the magazine.
        # If it is, return True immediately.
        if (ransomNote in magazine) :
            return True
        else:
            # If the ransomNote is not directly contained within the magazine,
            # initiate a dictionary to count the occurrence of each character in the magazine.
            magazine_char_count = {}
            
            # Iterate through each character in the magazine
            for char in magazine:
                # If the character is already in the dictionary, increment its count
                if char in magazine_char_count:
                    magazine_char_count[char] += 1
                else:
                    # If the character is not in the dictionary, add it with a count of 1
                    magazine_char_count[char] = 1
            
            # Print the dictionary to check
