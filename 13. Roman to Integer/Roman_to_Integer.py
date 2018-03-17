class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pro = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        l = len(s)
        result = pro[s[-1]]
        index = result
        for i in range(l-2,-1,-1):
            if pro[s[i]] >= index:
                result += pro[s[i]]
                index = pro[s[i]]
            else:
                result -= pro[s[i]]

        return result

if __name__ == "__main__":
    print Solution().romanToInt("MCMXCVI")


