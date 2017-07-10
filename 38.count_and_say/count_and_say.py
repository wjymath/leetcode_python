class Solution(object):
    def count(self, data):
        data = list(data)
        #print "data is : " + str(data)
        count = 1
        result = ""
        value = data.pop(0)
        while data:
            tmp = data.pop(0)
            if tmp == value:
                count += 1
            else:
                result += str(count)
                result += str(value)
                value = tmp
                count = 1
        result += str(count)
        result += str(value)
        return result

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        data = str(1)
        if n == 1:
            return data
        for i in range(1,n):
            #print i
            data = self.count(data)
        return data

if __name__ == "__main__":
    print Solution().countAndSay(4)