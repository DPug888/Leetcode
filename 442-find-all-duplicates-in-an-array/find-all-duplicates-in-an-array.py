class Solution(object):
    def findDuplicates(self, nums):
        freq={}
        for x in nums:
            freq[x] = freq.get(x,0) + 1
        arr = []
        for i in freq:
            if freq[i] >= 2:
                arr.append(i)
        return arr
        