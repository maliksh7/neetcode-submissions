import unittest

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        for c in s:
            count[c] += 1
        
        for i,c in enumerate(s):
            if count[c] == 1:
                return i
        return -1 

# class TestSolution(unittest.TestCase):
#     def setUp(self):
#         self.sol = Solution()

#     def test_example_2(self):
#         self.assertEqual(self.sol.firstUniqChar("neetcodeislove"), 0)

#     def test_no_unique_char(self):
#         self.assertEqual(self.sol.firstUniqChar("baab"), -1)


# if __name__ == "__main__":
#     unittest.main()

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(1) since we have at most 26 different characters.