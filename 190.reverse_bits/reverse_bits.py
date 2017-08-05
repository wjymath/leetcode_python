class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bi = bin(n)[2:]
        l = len(bi)
        bi = bi.zfill(32)
        return int(bi[::-1], 2)

if __name__ == '__main__':
    print Solution().reverseBits(2)
