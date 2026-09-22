class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        total = 0
        count = 0
        for i in range(k):
            total += arr[i]
        if total >= k * threshold:
            count += 1
        for r in range(k, len(arr)):
            total += arr[r]
            total -= arr[r - k]
            if total >= k * threshold:
                count += 1
        return count