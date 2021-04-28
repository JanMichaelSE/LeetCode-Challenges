import unittest
from LongestSubstring import *

class Test_LongestSubstringMethods(unittest.TestCase):

    def test_example_1(self):
        # --- Arrange ---
        test_String = 'abcabcbb'

        # --- Act ---
        result = Solution.lengthOfLongestSubstring(Solution, test_String)

        # --- Assert ----
        self.assertEquals(result, 3)

    def test_example_2(self):
        # --- Arrange ---
        test_String = 'dvdf'

        # --- Act ---
        result = Solution.lengthOfLongestSubstring(Solution, test_String)

        # --- Assert ----
        self.assertEquals(result, 1)

    def test_example_3(self):
        # --- Arrange ---
        test_String = 'pwwkew'

        # --- Act ---
        result = Solution.lengthOfLongestSubstring(Solution, test_String)

        # --- Assert ----
        self.assertEquals(result, 3)

    def test_example_4(self):
        # --- Arrange ---
        test_String = ''

        # --- Act ---
        result = Solution.lengthOfLongestSubstring(Solution, test_String)

        # --- Assert ----
        self.assertEquals(result, 0)

    def test_string_with_spaces(self):
        # --- Arrange ---
        test_String = ' '

        # --- Act ---
        result = Solution.lengthOfLongestSubstring(Solution, test_String)

        # --- Assert ----
        self.assertEquals(result, 1)
        

if __name__ == '__main__':
    unittest.main()