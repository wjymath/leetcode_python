class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n -= count
            if n >= count + 1:
                count += 1
        return count
if __name__ == '__main__':
    print Solution().arrangeCoins(15)
