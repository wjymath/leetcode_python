# leetcode_python
leetcode solution in python

build in 2017/06/30 1:00 for leetcode

1.set & list funciton return new object with different address
set和list内置函数会返回一个新的object而不是修改原先地址的值，这里需要特别注意！

2.如何能够高效简洁的使用正则表达式？比如要匹配两种格式的电话？(xxx) xxx-xxxx or xxx-xxx-xxxx
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt 开头结尾的个数限制以及格式应该怎么写，需要思考

3.no.258（每位数字相加之和不大于10）绝妙的计算方式：
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 0 if num == 0 else (num - 1) % 9 + 1
        
4.检测单链表中是否有环 no.141 两个指针，一个指针快一个指针慢，如果均为None则表示无环，否则必相等