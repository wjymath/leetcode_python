class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s.find("A") != s.rfind("A"):
            return False
        if s.replace("LL", "L").find("LL") != -1:
            return False
        return True
