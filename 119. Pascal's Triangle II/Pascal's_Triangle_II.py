class Solution(object):
    def next_level(self, input):
        l = len(input)
        result = []
        for i in range(l):
            if i == 0:
                result.append(1)
            else:
                result.append(input[i - 1] + input[i])
        result.append(1)
        return result

    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return [1]
        result = [1]
        for i in range(1, numRows + 1):
            result = self.next_level(result)
        return result


print(Solution().getRow(0))
