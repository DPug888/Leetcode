class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_count = 0
        set_list = set()
        for right in range(len(s)):
            while s[right] in set_list:
                set_list.remove(s[left])
                left+=1
            set_list.add(s[right])
            max_count = max(right-left +1, max_count)
        return max_count









        # for char in range(len(s)):
        #     if char in seen:
        #         seen.remove(char)
        #         curr_len-=1
        #     else:
        #         seen.add(char)
        #         curr_len+=1
        #         max_len = max(max_len, curr_len)
        # return max_len
