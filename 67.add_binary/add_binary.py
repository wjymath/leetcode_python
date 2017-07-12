class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        count = 0
        if len(b) < len(a):
            a, b = b, a
        for i in range(-1, - 1 - len(a), -1):
            result = str((int(a[i]) + int(b[i]) + count) % 2) + result
            count = (int(a[i]) + int(b[i]) + count) / 2
        if count == 0:
            return b[0:(len(b) - len(a))] + result
        for i in range(len(b) - len(a) - 1, -1, -1):
            result = str((int(b[i]) + count) % 2) + result
            count = (int(b[i]) + count) / 2
            if count == 0:
                return b[0:i] + result
        if count:
            return '1' + result
        return result

if __name__ == '__main__':
    print Solution().addBinary("110010", "10111")