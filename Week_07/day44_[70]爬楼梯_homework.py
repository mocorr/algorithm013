# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 动态规划 
#  👍 1156 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    @functools.lru_cache(100)  # 缓存装饰器
    def climbStairsCur(self, n):
        """
        递归+缓存
        """
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs(self, n):
        """
        只存最近2个数 时间复杂度O(n) 空间复杂度O(1)
        """
        if n <= 2:
            return n
        tmp1, tmp2 = 1, 2
        for i in range(2, n):
            tmp1, tmp2 = tmp2, tmp1 + tmp2
        return tmp2

# leetcode submit region end(Prohibit modification and deletion)
