# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。 
# 
#  说明：不要使用任何内置的库函数，如 sqrt。 
# 
#  示例 1： 
# 
#  输入：16
# 输出：True 
# 
#  示例 2： 
# 
#  输入：14
# 输出：False
#  
#  Related Topics 数学 二分查找 
#  👍 165 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left = 2
        right = num // 2
        while left <= right:
            mid = left + (right - left) // 2
            mid_square = mid * mid
            if mid_square == num:
                return True
            elif mid_square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
