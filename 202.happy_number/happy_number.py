class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = [n]
        tmp = n
        while 1:
            tmp = sum(int(i) ** 2 for i in str(tmp))
            if tmp == 1:
                return True
            if tmp in result:
                return False
            result.append(tmp)