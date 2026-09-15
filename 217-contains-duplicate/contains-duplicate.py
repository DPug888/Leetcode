class Solution(object):
    def containsDuplicate(self, nums):
        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0) + 1
        for i in freq:
            if freq[i] >= 2:
                return True
        else:
            return False
        