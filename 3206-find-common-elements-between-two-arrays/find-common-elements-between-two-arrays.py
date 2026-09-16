class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        a = 0
        b = 0
        for x in nums1:
            if x in nums2:
                a += 1
        for x in nums2:
            if x in nums1:
                b += 1
        return [a, b]