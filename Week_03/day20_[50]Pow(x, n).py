# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。 
# 
#  示例 1: 
# 
#  输入: 2.00000, 10
# 输出: 1024.00000
#  
# 
#  示例 2: 
# 
#  输入: 2.10000, 3
# 输出: 9.26100
#  
# 
#  示例 3: 
# 
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25 
# 
#  说明: 
# 
#  
#  -100.0 < x < 100.0 
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。 
#  
#  Related Topics 数学 二分查找 
#  👍 465 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myPowBad(self, x: float, n: int) -> float:
        """
        暴力法 时间复杂度O(n) 空间复杂度O(1)
        """
        if n < 0:
            n = - n
            x = 1 / x
        ans = 1
        for i in range(n):
            ans *= x
        return ans

    def myPow(self, x: float, n: int) -> float:
        """
        快速幂 时间复杂度O(log n) 空间复杂度O(log n)
        """
        if n < 0:
            n = -n
            x = 1/x
        if n == 0:
            return 1
        if n == 1:
            return x
        half = self.myPow(x, n // 2)
        if n % 2 == 1:
            return half * half * x
        return half * half


# leetcode submit region end(Prohibit modification and deletion)
