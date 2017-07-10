class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for item in nums:
            if item < target:
                continue
            if item == target:
                return nums.index(item)
            if item > target:
                return nums.index(item)
        return len(nums)