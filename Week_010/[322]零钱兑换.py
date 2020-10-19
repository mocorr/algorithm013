# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  你可以认为每种硬币的数量是无限的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  
# 输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：coins = [1], amount = 0
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：coins = [1], amount = 1
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：coins = [1], amount = 2
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 231 - 1 
#  0 <= amount <= 104 
#  
#  Related Topics 动态规划 
#  👍 868 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        """
        DP
        """
        # 特判已包含在DPTable的边界里
        # if not coins:
        #     return -1
        # if amount == 0:
        #     return 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                # dp[i] = min(之前的硬币组合的最佳方案，最后一个硬币用当前的coin)
                dp[i] = min(dp[i - coin] + 1, dp[i])
        return -1 if dp[-1] == float('inf') else dp[-1]

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        贪心 递归 超时
        不能采用大头尽量多、不行再次大的思路 因为尾数不正好
        """
        if not coins:
            return -1
        if amount == 0:
            return 0
        self.res = float('inf')
        coins.sort(reverse=True)

        # @functools.lru_cache(None) 没用
        def dfs(rest, index, cnt):
            if rest == 0:
                self.res = min(self.res, cnt)
                return
            if index == len(coins):
                return

            k = rest // coins[index]  # k >= 0
            for i in range(min(self.res - cnt, k), -1, -1):  # 能剪掉大部份枝
                dfs(rest - i * coins[index], index + 1, cnt + i)

        dfs(amount, 0, 0)
        return -1 if self.res == float('inf') else self.res

# leetcode submit region end(Prohibit modification and deletion)
