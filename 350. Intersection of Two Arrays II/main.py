from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        result = []
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        for key in cnt1:
            if key in cnt2:
                tmp_num = min(cnt1[key], cnt2[key])
                result.extend([key] * tmp_num)
        return result