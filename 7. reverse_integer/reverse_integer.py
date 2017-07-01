class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 2147483647 #sys.maxint in 32bits system
        result = 0
        count = 1 if x >= 0 else -1
        x *= count
        while x:
            result = 10 * result + x % 10
            x /= 10

        if not (-max_int - 1) <= result <= max_int:
            return 0
        return result * count

# a = Solution()
# print a.reverse(-1474836479)