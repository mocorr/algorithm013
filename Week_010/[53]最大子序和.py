# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  示例: 
# 
#  输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶: 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 2517 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArrayDp(self, nums: List[int]) -> int:
        """
        DP
        """
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        return max(dp)

    def maxSubArray(self, nums: List[int]) -> int:
        """
        DP空间优化
        """
        if not nums:
            return 0
        pre, res = 0, nums[0]
        for i in range(len(nums)):  # 注意这里从头开始
            pre = max(pre, 0) + nums[i]
            res = max(res, pre)
        return res
# leetcode submit region end(Prohibit modification and deletion)
