class Solution(object):
    def uniqueOccurrences(self, arr):
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
        values = []
        for x in freq:
            values.append(freq[x])
        if len(values) == len(set(values)):
            return True
        return False