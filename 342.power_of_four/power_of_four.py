class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num != 1:
            if num % 4:
                return False
            num /= 4
        if num == 1:
            return True
if __name__ == '__main__':
    print Solution().isPowerOfFour(16)