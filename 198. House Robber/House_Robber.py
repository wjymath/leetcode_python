class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if not l:
            return 0
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums)
        if l == 3:
            return max(nums[1], nums[0] + nums[2])
        return max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))

print(Solution().rob([2,7,9,3,1]))