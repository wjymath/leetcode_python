class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = 0
        for i in range(len(s)):
            count -= ord(s[i])
            count += ord(t[i])
        count += ord(t[-1])
        return chr(count)

if __name__ == '__main__':
    print Solution().findTheDifference("abrcdet", "abcderte")