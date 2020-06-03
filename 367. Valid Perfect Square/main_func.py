class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        tmp = num
        while tmp * tmp > num:
            tmp = int((tmp + int(num / tmp)) / 2)
        return tmp * tmp == num