# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。 
# 
#  注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  示例 1: 
# 
#  输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。 
# 
#  示例 2: 
# 
#  输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#  
# 
#  示例 3: 
# 
#  输入: [7,6,4,3,1] 
# 输出: 0 
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。 
#  Related Topics 数组 动态规划 
#  👍 526 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfitDp3(self, prices: List[int]) -> int:
        """
        三维DP 可以降为2维or滚动数组 但是正常人不可能直接写出
        dp[i][j][l]：第i天 j次已完成交易（卖出才完成） l表示是否持有股票
        dp[i][0][0] = 0
        dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][0][0] - prices[i])
        dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][1] + prices[i])
        dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][1][0] - prices[i])
        dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][1][1] + prices[i])
        dp[i][2][1] 不存在也用不到
        """
        if not prices:
            return 0
        dp = [[[0] * 2 for _ in range(2 + 1)] for _ in range(len(prices))]
        dp[0][0][1], dp[0][1][1] = -prices[0], -prices[0]
        for i in range(1, len(prices)):
            for j in range(1, 2 + 1):  # 很有技巧
                dp[i][j - 1][1] = max(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0] - prices[i])
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
        return dp[-1][-1][0]

    def maxProfitDp2(self, prices: List[int]) -> int:
        """
        二维DP
        """
        if not prices:
            return 0
        dp = [[0] * 5 for _ in range(len(prices))]
        dp[0][1], dp[0][3] = -prices[0], -prices[0]
        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        return dp[-1][4]

    def maxProfit(self, prices: List[int]) -> int:
        """
        滚动数组
        """
        if not prices:
            return 0
        dp0, dp1, dp2, dp3, dp4 = 0, -prices[0], 0, -prices[0], 0
        for i in range(1, len(prices)):
            tmp1 = max(dp1, dp0 - prices[i])
            tmp2 = max(dp2, dp1 + prices[i])
            tmp3 = max(dp3, dp2 - prices[i])
            tmp4 = max(dp4, dp3 + prices[i])
            dp1, dp2, dp3, dp4 = tmp1, tmp2, tmp3, tmp4
        return dp4
# leetcode submit region end(Prohibit modification and deletion)
