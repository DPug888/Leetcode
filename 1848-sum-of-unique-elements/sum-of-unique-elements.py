class Solution(object):
    def sumOfUnique(self, nums):
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        ans = 0
        for i in freq:
            if freq[i] == 1:
                ans += i
        return ans