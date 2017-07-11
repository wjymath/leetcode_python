class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        count = 1
        tmp = nums[0]
        while count < len(nums):
            if tmp == nums[count]:
                nums.pop(count)
            else:
                tmp = nums[count]
                count += 1
        print nums
        return len(nums)

if __name__ == '__main__':
    print Solution().removeDuplicates([1,1,1,2,3,3])