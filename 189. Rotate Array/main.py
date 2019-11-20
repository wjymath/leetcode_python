class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return []
        l = len(nums)
        k = k % len(nums)
        pre = nums[:l - k]
        suf = nums[l - k:]
        for i in range(k):
            nums[i] = suf[i]
        for i in range(len(pre)):
            nums[k + i] = pre[i]