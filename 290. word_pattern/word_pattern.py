class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        if len(str) != len(pattern):
            return False
        dic = {}
        for i in range(len(pattern)):
            if dic.get(pattern[i], -1) == -1:
                dic[pattern[i]] = str[i]
            elif dic.get(pattern[i], -1) == str[i]:
                continue
            else:
                return False
        for i in dic.keys():
            for j in dic.keys():
                if i != j:
                    if dic[i] == dic[j]:
                        return False

        return True