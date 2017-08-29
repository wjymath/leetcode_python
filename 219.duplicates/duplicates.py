class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i,v in enumerate(nums):
            if v in d and i - d.get(v) <= k:
                return True
            d[v] = i
        return False

if __name__ == '__main__':
    print Solution().containsNearbyDuplicate([1,2,3,4,5,1],4)