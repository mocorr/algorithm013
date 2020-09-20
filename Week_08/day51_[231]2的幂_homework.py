# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。 
# 
#  示例 1: 
# 
#  输入: 1
# 输出: true
# 解释: 20 = 1 
# 
#  示例 2: 
# 
#  输入: 16
# 输出: true
# 解释: 24 = 16 
# 
#  示例 3: 
# 
#  输入: 218
# 输出: false 
#  Related Topics 位运算 数学 
#  👍 241 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfTwoWhile(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

    def isPowerOfTwo1(self, n: int) -> bool:
        """
        n & (n - 1) 将n最右边的1设置为0，故无需加 n > 0 的判断
        若n为2的幂，则只有一个1.
        """
        if n == 0:
            return False
        return n & (n - 1) == 0

    def isPowerOfTwo(self, n: int) -> bool:
        """
        n & (-n) 获取n最右边的1，故无需加 n > 0 的判断
        若n为2的幂，则只有一个1.
        """
        if n == 0:
            return False
        return n & (-n) == n


# leetcode submit region end(Prohibit modification and deletion)
