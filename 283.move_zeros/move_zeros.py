class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = 0
        for i in range(0,n):
            if nums[i] != 0:
                nums[index] = nums[i]
                if i != index:
                    nums[i] = 0
                index += 1

if __name__ == '__main__':
    print Solution().moveZeroes([0,1,2,3,4,5,0,0,6])
