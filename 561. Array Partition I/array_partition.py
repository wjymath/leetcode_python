class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = sorted(nums)
        cnt = 0
        for i in range(0, len(result), 2):
            cnt += result[i]
        return cnt

print Solution().arrayPairSum([1, 4, 2, 3])