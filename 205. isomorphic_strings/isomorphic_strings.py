class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tmp = {}
        for i in range(len(t)):
            if tmp.get(s[i], -1) == -1:
                tmp[s[i]] = t[i]
            elif tmp.get(s[i], -1) == t[i]:
                continue
            else:
                return False
        for i in tmp.keys():
            for j in tmp.keys():
                if i != j:
                    if tmp[i] == tmp[j]:
                        return False
        return True