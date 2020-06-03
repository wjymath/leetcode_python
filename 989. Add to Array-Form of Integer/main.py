from matplotlib.mathtext import List


class Solution:
    def addToArrayForm(self, A, K):
        num = int("".join(map(str, A)))
        num += K
        result = []
        if num == 0:
            return [0]
        while num // 10 != 0:
            result = [num % 10] + result
            num = num // 10
        if num != 0:
            result = [num] + result
        return result


print(Solution().addToArrayForm([1,2,0,0], 34))
print(Solution().addToArrayForm([9,9,9,9,9,9,9,9,9,9], 1))
print(Solution().addToArrayForm([9], 349))