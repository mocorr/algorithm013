# 实现 int sqrt(int x) 函数。 
# 
#  计算并返回 x 的平方根，其中 x 是非负整数。 
# 
#  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。 
# 
#  示例 1: 
# 
#  输入: 4
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
#      由于返回类型是整数，小数部分将被舍去。
#  
#  Related Topics 数学 二分查找 
#  👍 486 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        平方根问题，x>=4才满足 x//2 >= sqrt(x)，所以 x<4需要特殊讨论；
        但此题x in [0,2,3]时，right恰为解(不进入循环)，仅需特判x == 1的情况.
        """
        # if x == 0:
        #     return 0
        # if x < 4:
        #     return 1
        if x == 1:
            return 1
        left, right = 2, x // 2
        while left <= right:  # 相当于停止条件是left > right
            mid = left + (right - left) // 2
            mid_square = mid * mid
            if mid_square == x:
                return mid
            elif mid_square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
# leetcode submit region end(Prohibit modification and deletion)
