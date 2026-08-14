class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        maximum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]

            maximum = max(maximum, window_sum)

        return float(maximum) / k