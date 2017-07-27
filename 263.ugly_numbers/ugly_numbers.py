class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        result = num
        while result%5 == 0:
            result /= 5
        while result%3 == 0:
            result /= 3
        while result%2 == 0:
            result /= 2
        if result == 1:
            return True
        else:
            return False