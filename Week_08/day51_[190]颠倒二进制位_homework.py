# 颠倒给定的 32 位无符号整数的二进制位。 
# 
#  
# 
#  示例 1： 
# 
#  输入: 01001010000011110100111000000001
# 输出: 00111001011110000010100101000000
# 解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
#      因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。 
# 
#  示例 2： 
# 
#  输入：11111111111111111111111111111101
# 输出：10111111111111111111111111111111
# 解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
#      因此返回 3221225471 其二进制表示形式为 10111111111111111111111111111111 。 
# 
#  
# 
#  提示： 
# 
#  
#  请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的
# 还是无符号的，其内部的二进制表示形式都是相同的。 
#  在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 2 中，输入表示有符号整数 -3，输出表示有符号整数 -10737418
# 25。 
#  
# 
#  
# 
#  进阶: 
# 如果多次调用这个函数，你将如何优化你的算法？ 
#  Related Topics 位运算 
#  👍 206 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseBitsAnd1(self, n: int) -> int:
        """
        & 1 只取最后一位
        << 左移不会使最左侧的位消失，右移会使最右侧的位消失
        """
        ans = 0
        steps = 31
        while n:
            ans += (n & 1) << steps
            steps -= 1
            n >>= 1
        return ans

    def reverseBits2(self, n: int) -> int:
        """
        & 1 只取最后一位
        """
        ans = 0
        for i in range(32):
            ans <<= 1  # i == 0时此步骤不产生实际影响
            ans += n & 1
            n >>= 1
        return ans

    def reverseBits(self, n: int) -> int:
        """
        掩码Mask
        0xff00ff00 = 1111 1111 0000 0000 1111 1111 0000 0000
        0x00ff00ff = 0000 0000 1111 1111 0000 0000 1111 1111
        0xf0f0f0f0 = 1111 0000 1111 0000 1111 0000 1111 0000
        0x0f0f0f0f = 0000 1111 0000 1111 0000 1111 0000 1111
        0xcccccccc = 1100 1100 1100 1100 1100 1100 1100 1100
        0x33333333 = 0011 0011 0011 0011 0011 0011 0011 0011
        0xaaaaaaaa = 1010 1010 1010 1010 1010 1010 1010 1010
        0x55555555 = 0101 0101 0101 0101 0101 0101 0101 0101
        初始: abcdefghijklmnopqrstuvwxyz012345
        第一步结果:  qrstuvwxyz012345  abcdefghijklmnop
        第二步结果:  yz012345 qrstuvwx   ijklmnop abcdefgh
        第三步结果:  2345 yz01 uvwx qrst  mnop  ijkl efgh abcd
        第四步结果:  45 23 01 yz wx uv st qr  op mn kl ij gh ef cd ab
        第五步结果:  5 4 3 2 1 0 z y x w v u t s r q  p o n m l k j i h g f e d c b a
        """
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


        
# leetcode submit region end(Prohibit modification and deletion)
