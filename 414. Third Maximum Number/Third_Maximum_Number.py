import sys

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        g_min = -(sys.maxint + 1)
        result = [g_min, g_min, g_min]

        for i in nums:
            if i > result[0]:
                result = [i, result[0], result[1]]
            elif i > result[1] and i < result[0]:
                result = [result[0], i, result[1]]
            elif i > result[2] and i < result[1]:
                result = [result[0], result[1], i]
        if g_min in result:
            return result[0]
        return result[2]

if __name__ == "__main__":
    print Solution().thirdMax([2, 2, 3, 1])