class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while 1:
            try:
                nums.remove(val)
            except ValueError:
                break
        return len(nums)

if __name__ == "__main__":
    a = Solution()
    print a.removeElement([], [])