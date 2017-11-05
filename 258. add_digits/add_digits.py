class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        while num / 10:
            result += num % 10
            num /= 10
        result += num
        if result / 10:
            return self.addDigits(result)
        else:
            return result

if __name__ == "__main__":
    print Solution().addDigits(19)