class Solution(object):
    def str_add(self, str1, str2,n):
        str2 = str2 + '0' * n
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        if len(str1) == 0:
            return str2
        # print "str1 : " + str1
        # print "str2 : " + str2
        count = 0
        result = ''
        for i in range(-1, -(len(str1)+1), -1):
            num1 = int(str1[i])
            num2 = int(str2[i])
            result += str((num1 + num2 + count) % 10)
            count = (num1 + num2 + count) / 10
        # print result
        if count == 0:
            result += str2[i-1:-(len(str2)+1):-1]
            return result[-1:-(len(result)+1):-1] # reverse
        tmp = self.str_add(str(count), str2[0:len(str2)+i], 0)
        result += tmp[-1:-(len(tmp)+1):-1]
        return result[-1:-(len(result)+1):-1] # reverse

    def str_mul(self, char, str1):
        count = 0
        num = int(char)
        result = ''
        for i in range(-1, -(len(str1)+1), -1):
            tmp = (int(str1[i])*num+count) % 10
            result += str(tmp)
            count = (int(str1[i])*num+count) / 10
        if count:
            result += str(count)
        return result[-1:-(len(result)+1):-1]

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        result = [''] * len(num1)
        for i in range(-1, -(len(num1)+1), -1):
            result[i] = self.str_mul(num1[i], num2)
        # print result
        result.reverse()
        print result
        out = ''
        for i in range(0,len(result)):
            #print i
            out = self.str_add(out, result[i], i)
            # print "out : " + out
        if out[0] == '0':
            return '0'
        return out

if __name__ == '__main__':
    print Solution().multiply('63738', '51')