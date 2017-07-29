class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        tmp = n * (n-1) / 2
        result = tmp - sum(nums)
        return result

if __name__ == '__main__':
    print Solution().missingNumber([1])