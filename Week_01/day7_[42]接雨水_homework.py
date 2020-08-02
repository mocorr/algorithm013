# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。 
# 
#  示例: 
# 
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6 
#  Related Topics 栈 数组 双指针 
#  👍 1505 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trapBad(self, height: List[int]) -> int:
        """
        按列找 对每个柱子分别找出其左右侧最高值 时间复杂度O(n^2)
        找左侧最大值无需单独进行一次遍历
        """
        areas = 0
        max_left = 0
        for i in range(1, len(height) - 1):
            # max_left = 0
            # for j in range(0, i):  # 与上层for同向且步长相等，可优化
            #     max_left = max(height[j], max_left)
            max_left = max(max_left, height[i - 1])
            max_right = 0
            for j in range(i + 1, len(height)):
                max_right = max(height[j], max_right)
            max_lower = min(max_left, max_right)
            areas += max(max_lower - height[i], 0)
        return areas

    def trapGood(self, height: List[int]) -> int:
        """
        动态规划法 对法一找左右侧最大值的方式进行优化 时间复杂度O(n) 空间复杂度O(n)
        """
        areas = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        for i in range(1, len(height) - 1):
            max_left[i] = max(max_left[i - 1], height[i - 1])
        for i in range(len(height) - 2, 0, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        for i in range(1, len(height) - 1):
            areas += max(min(max_left[i], max_right[i]) - height[i], 0)
        return areas

    def trap(self, height: List[int]) -> int:
        """
        双指针法 结合上述两种方法 时间复杂度o(n)
        """
        if len(height) == 0:
            return 0
        areas = 0
        max_left, max_right = height[0], height[len(height) - 1]
        left, right = 1, len(height) - 2
        # max_left, max_right = 0, 0
        # left, right = 0, len(height) - 1
        while left <= right:
            if max_left < max_right:
                areas += max(0, max_left - height[left])
                max_left = max(max_left, height[left])
                left += 1
            else:
                areas += max(0, max_right - height[right])
                max_right = max(max_right, height[right])
                right -= 1
        return areas

# leetcode submit region end(Prohibit modification and deletion)
