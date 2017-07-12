class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip(' ')
        return len(s.split(" ")[-1])

if __name__ == '__main__':
    print Solution().lengthOfLastWord(' ')