# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。 
# 
#  示例: 
# 
#  输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  说明: 
# 
#  假设你总是可以到达数组的最后一个位置。 
#  Related Topics 贪心算法 数组 
#  👍 671 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump1(self, nums: List[int]) -> int:
        """
        贪心 反向查找 每次直接取首个能跳到目标位置的（即最远的）
        时间复杂度O(n^2) 空间复杂度O(1)
        """
        aim = len(nums) - 1
        steps = 0
        while aim > 0:
            for i in range(aim):
                if nums[i] + i >= aim:
                    steps += 1
                    aim = i
                    break
        return steps

    def jump(self, nums: List[int]) -> int:
        """
        贪心 正向查找 每次都选收益最大的
        时间复杂度O(n) 空间复杂度O(1)
        """
        curr_max, pre_max, steps = 0, 0, 0
        for i in range(len(nums) - 1):
            if i <= pre_max:
                curr_max = max(curr_max, i + nums[i])
                if i == pre_max:
                    steps += 1
                    pre_max = curr_max
        return steps
# leetcode submit region end(Prohibit modification and deletion)
