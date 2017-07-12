class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        count = (digits[-1] + 1) / 10
        digits[-1] = (digits[-1] + 1) % 10
        if count == 0:
            return digits
        for i in range(len(digits) - 2, -1, -1):
            tmp = digits[i] + count
            digits[i] = tmp % 10
            count = tmp / 10
            if count == 0:
                return digits
        if count:
            digits = [1] + digits
        return digits

if __name__ == '__main__':
    print Solution().plusOne([9,9,9,8])