class Solution(object):
    def isPalindrome(self, s):
        phrase=[c.lower() for c in s if c.isalnum()]
        return phrase == phrase[::-1]
