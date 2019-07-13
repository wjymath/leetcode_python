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

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1]]
        for i in range(1, numRows):
            result.append(self.next_level(result[i - 1]))
        return result


print(Solution().generate(5))
