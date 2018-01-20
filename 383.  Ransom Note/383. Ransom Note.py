class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote == "":
            return True
        if magazine == "":
            return False
        dic = {}
        for i in ransomNote:
            cnt = dic.get(i,0) + 1
            dic.update({i:cnt})
        for i in dic.keys():
            if magazine.count(i) >= dic[i]:
                pass
            else:
                return False
        return True
if __name__ == "__main__":
    print Solution().canConstruct("aa", "ab")