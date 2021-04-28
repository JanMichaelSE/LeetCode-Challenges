"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = ""
        substringLength = 0
        maxSubstringLength = 0
        
        characters = list(s)
        for ch in characters:
            if ch not in longestSubstring:
                longestSubstring += ch
                substringLength += 1
                if substringLength > maxSubstringLength:
                    maxSubstringLength = substringLength
            else:
                longestSubstring = ""
                substringLength = 0
                longestSubstring += ch
                substringLength += 1
        
        return maxSubstringLength
                

# if __name__ == '__main__':
            