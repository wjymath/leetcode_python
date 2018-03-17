class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        local_max = 0
        i = 0
        j = len(height) - 1

        while i < j:
            local_max = max([local_max, (j - i) * (min([height[i], height[j]]))])

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return local_max

if __name__ == "__main__":
    print Solution().maxArea([2,2,3,4,5])