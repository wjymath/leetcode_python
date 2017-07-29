class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = bin(n)

        result = 0
        for i in tmp[::-1]:
            if i == '1':
                result += 1
            if i == 'b':
                return result

if __name__ == '__main__':
    print Solution().hammingWeight(0)