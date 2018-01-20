class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
             return ""
        if len(strs) == 1:
            return strs[0]
        max_result = ""
        cnt = 1
        tmp = strs[0][:cnt]
        if tmp == "":
            return max_result
        while 1:
            for i in strs:
                if i.find(tmp) == 0:
                    pass
                else:
                    return max_result
            if max_result == tmp:
                return max_result
            max_result = tmp
            cnt += 1
            tmp = strs[1][:cnt]

        return max_result

if __name__ == "__main__":
    print  Solution().longestCommonPrefix(["c","c"])