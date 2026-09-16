class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = set()
        for i, x in enumerate(nums):
            if x in seen:
                return True
            seen.add(x)
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False