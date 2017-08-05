class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 0:
            return num2
        if len(num2) == 0:
            return num1
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        value = 0
        result = ''
        for i in range(len(num2)):
            tmp = int(num1[i]) + int(num2[i]) + value
            result += str(tmp % 10)
            value = tmp / 10
        if value == 0:
            return (result + num1[len(num2):])[::-1]

        for i in range(len(num2), len(num1)):
            tmp = int(num1[i]) + value
            result += str(tmp % 10)
            value = tmp / 10

        if value == 1:
            result += '1'
        return result[::-1]
if __name__ == '__main__':
    print Solution().addStrings('999', '1')