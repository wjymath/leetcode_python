class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0
        result = ''
        while (len(s) - 2 *k * i) > 2*k:
            result += s[2*k*i:2*k*i+k][::-1]
            result += s[2*k*i+k:2*k*i+2*k]
            i += 1
        if (len(s) - 2 * k * i) > k:
            result += s[2*k*i:2*k*i+k][::-1]
            result += s[2*k*i+k::]
        else:
            result += s[2*k*i::][::-1]

        return result

if __name__ == '__main__':
    print Solution().reverseStr('abcdefg',2)
