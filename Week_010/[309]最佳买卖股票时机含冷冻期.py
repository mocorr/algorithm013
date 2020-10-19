# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。 
# 
#  设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）: 
# 
#  
#  你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
#  卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。 
#  
# 
#  示例: 
# 
#  输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出] 
#  Related Topics 动态规划 
#  👍 579 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfitDp3(self, prices: List[int]) -> int:
        """
        三维DP
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[[0] * 2 for _ in range(2)] for _ in range(n)]
        dp[0][1][0] = -prices[0]
        for i in range(1, n):
            # 前1持有 后1冷冻
            dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][0][1])
            dp[i][0][1] = dp[i - 1][1][0] + prices[i]
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][0] - prices[i])
        return max(dp[-1][0][0], dp[-1][0][1])

    def maxProfitDp2(self, prices: List[int]) -> int:
        """
        二维DP
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][2] = -prices[0]
        for i in range(1, n):
            # 0非冷冻 1冷冻 2持有
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][2] + prices[i]
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][0] - prices[i])
        return max(dp[-1][0], dp[-1][1])

    def maxProfit3(self, prices: List[int]) -> int:
        """
        滚动数组
        """
        if not prices:
            return 0
        n = len(prices)
        # dp1非冷冻 dp2冷冻 dp3持有
        dp1, dp2, dp3 = 0, 0, -prices[0]
        for i in range(1, n):
            tmp1 = max(dp1, dp2)
            tmp2 = dp3 + prices[i]
            tmp3 = max(dp3, dp1 - prices[i])
            dp1, dp2, dp3 = tmp1, tmp2, tmp3
        return max(dp1, dp2)
# leetcode submit region end(Prohibit modification and deletion)
