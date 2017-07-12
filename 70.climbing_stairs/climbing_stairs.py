class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [1, 2]
        for i in range(2, n):
            l.append(l[i - 2] + l[i - 1])
        return l[n-1]

if __name__ == '__main__':
    print Solution().climbStairs(5)