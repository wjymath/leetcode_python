class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # use loop and break early will be faster! have a try later
        try:
            result = haystack.index(needle)
        except:
            result = -1
        return result