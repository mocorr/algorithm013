# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  问总共有多少条不同的路径？ 
# 
#  
# 
#  例如，上图是一个7 x 3 的网格。有多少可能的路径？ 
# 
#  
# 
#  示例 1: 
# 
#  输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
#  
# 
#  示例 2: 
# 
#  输入: m = 7, n = 3
# 输出: 28 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m, n <= 100 
#  题目数据保证答案小于等于 2 * 10 ^ 9 
#  
#  Related Topics 数组 动态规划 
#  👍 707 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsDp(self, m: int, n: int) -> int:
        """
        DP 其实左上/右下/左下/右上为坐标原点皆可，右下为原点无需逆序
        """
        if min(m, n) <= 0:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePathsDp1(self, m: int, n: int) -> int:
        """
        DP化简 初始化为全1可以少算最末行，且最末列始终为1
        """
        if min(m, n) <= 0:
            return 0
        dp = [1] * n
        for i in range(1, m):  # 注意范围
            for j in range(1, n):  # 注意范围
                dp[j] += dp[j - 1]
        return dp[n - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        """
        排列组合
        m-1次向下，n-1次向右，共m-1+n-1步，其中需要取出m-1步向下（余下n-1步自然给出）或n-1步向右
        组合转化为阶乘 C(n+m-2, n-1) = (m+n-2)! / ((n-1)! * (m-1)!)
        有大量重复计算
        """
        return int(math.factorial(m + n - 2) / math.factorial(n - 1) / math.factorial(m - 1))

    def uniquePaths(self, m: int, n: int) -> int:
        """
        排列组合优化
        C(a,b) = [a * (a-1) * (a-2)*...* (a-b+1) ] / b!
        """
        def c(a, b):
            up, down = 1, 1
            for i in range(a - b + 1, a + 1):
                up *= i
            for j in range(1, b + 1):
                down *= j
            return up // down

        return c(m + n - 2, min(m - 1, n - 1))
# leetcode submit region end(Prohibit modification and deletion)
