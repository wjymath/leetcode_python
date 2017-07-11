class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s) > 0:
            a = s.find('()')
            if a != -1:
                s = s[:a] + s[(a+2):]
            b = s.find('[]')
            if b != -1:
                s = s[:b] + s[(b+2):]
            c = s.find('{}')
            if c != -1:
                s = s[:c] + s[(c+2):]
            if (a + b + c) == -3:
                return False
        return True

if __name__ == '__main__':
    print Solution().isValid('(){}[(]')
