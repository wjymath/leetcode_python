class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        result = nums[0]
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total > result:
                result = total
            if total < 0:
                total = 0
        return result

if __name__ == '__main__':
    print Solution().maxSubArray([-1, -2, 4])