from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # flip diagonally
        m = len(matrix)
        for i in range(m):
            for j in range(i + 1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # left to right
        for i in range(m):
            for j in range(int(m / 2)):
                matrix[i][j], matrix[i][m - 1 - j] = matrix[i][m - 1 - j], matrix[i][j]

# a = [[1,2,3],[4,5,6],[7,8,9]]
a = [[1,2], [3,4]]
a = [[ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16]]
print(Solution().rotate(a))
print(a)