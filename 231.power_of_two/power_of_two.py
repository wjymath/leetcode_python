class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        return bin(n).count('1') == 1

if __name__ == '__main__':
    print Solution().isPowerOfTwo(8)