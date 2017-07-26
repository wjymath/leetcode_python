class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1
        if n%2:
            return x * self.myPow(x*x, n/2)
        else:
            return self.myPow(x*x, n/2)

if __name__ == "__main__":
    print Solution().myPow(-2.0, -3)

