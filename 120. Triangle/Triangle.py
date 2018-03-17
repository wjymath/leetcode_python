class Solution(object):
    def func(self, m, n, dis, arr):
        if m == 0:
            return arr[0][0]
        if n == 0:
            return dis[m-1][n] + arr[m][n]
        if m == n:
            return dis[m-1][n-1] + arr[m][n]
        if m > n:
            return min(dis[m-1][n-1], dis[m-1][n]) + arr[m][n]


    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        l = len(triangle)
        tmp = triangle[:]

        for i in range(l):
            for j in range(i+1):
                tmp[i][j] = self.func(i, j, tmp, triangle)
        return min(tmp[i])
        # result = min(tmp[l-2][0] + triangle[l-1][0], tmp[l-2][l-2] + triangle[l-1][l-1])
        # for i in range(1, l-1):
        #     local_result = min(tmp[l-2][i-1], tmp[l-2][i]) + triangle[l-1][i]
        #     if local_result < result:
        #         result = local_result
        # return result

        # result = self.func(l-1, 0, triangle)
        # for i in range(1, l):
        #     tmp = self.func(l-1, i, triangle)
        #     if tmp < result:
        #         result = tmp
        # return result

if __name__ == "__main__":
    print Solution().minimumTotal([[2], [3,4], [6,5,7], [4,1,8,3]])