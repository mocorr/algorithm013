# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划 
#  👍 792 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProductDp(self, nums: List[int]) -> int:
        """
        Dp双状态
        """
        if not nums:
            return 0
        dp = [[0] * len(nums) for _ in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[0][i] = min(dp[0][i - 1] * nums[i], dp[1][i - 1] * nums[i], nums[i])
            dp[1][i] = max(dp[0][i - 1] * nums[i], dp[1][i - 1] * nums[i], nums[i])
        return max(dp[1])

    def maxProduct(self, nums: List[int]) -> int:
        """
        Dp空间优化
        """
        if not nums:
            return 0
        dp_max, dp_min, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            tmp_min = min(dp_min * nums[i], dp_max * nums[i], nums[i])
            tmp_max = max(dp_min * nums[i], dp_max * nums[i], nums[i])
            dp_min, dp_max = tmp_min, tmp_max
            res = max(res, dp_max)
        return res
# leetcode submit region end(Prohibit modification and deletion)
