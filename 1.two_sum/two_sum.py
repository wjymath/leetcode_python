class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = 0
        while 1:
            num = nums[0]
            nums.remove(num)
            if (target - num) in nums:
                return [count, nums.index(target - num) + 1 + count]
            count += 1

#a = Solution()
#nums = [2, 7, 11, 15]
#print a.twoSum(nums, 13)