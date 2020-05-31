class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        result = [[ 0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                line_add = int((j + k) / n)
                new_i = (i + line_add) % m
                new_j = (j + k) % n
                result[new_i][new_j] = grid[i][j]
        return result

# print(Solution().shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1))
# print(Solution().shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 4))
print(Solution().shiftGrid([[1],[2],[3],[4],[7],[6],[5]], 23))