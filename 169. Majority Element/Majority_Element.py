class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        tmp = []
        for i in nums:
            if i in tmp:
                continue
            if nums.count(i) > l/2:
                return i
            tmp.append(i)
if __name__ == "__main__":
    print Solution().majorityElement([1, 2, 1, 2, 2])
