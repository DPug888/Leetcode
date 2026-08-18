class Solution(object):
    def longestPalindrome(self, s):
        max_len= 0
        ans= ""

        for i in range(len(s)):
            for j in range (i, len(s)):
                sub = s[i:j+1]
                
                if sub == sub[::-1]:
                    if len(sub) > max_len:
                        max_len = len(sub)
                        ans = sub
        return ans