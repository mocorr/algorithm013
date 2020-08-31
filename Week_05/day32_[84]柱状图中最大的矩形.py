# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  
# 
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
# 
#  
# 
#  
# 
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
# 
#  
# 
#  示例: 
# 
#  输入: [2,1,5,6,2,3]
# 输出: 10 
#  Related Topics 栈 数组 
#  👍 872 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleAreaBad(self, heights: List[int]) -> int:
        """
        暴力法 对于每一个柱形找出左右最大边界 超时
        """
        res = 0
        for i in range(len(heights)):
            left = i - 1
            right = i + 1
            width = 1
            while left >= 0 and heights[left] >= heights[i]:
                width += 1
                left -= 1
            while right < len(heights) and heights[right] >= heights[i]:
                width += 1
                right += 1
            res = max(res, heights[i] * width)
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        单调栈 维护一个单调栈，单调时入栈，不单调时出栈并计算面积
        """
        stack = []
        heights = [0] + heights + [0]  # 头加0可以少写一个特判，尾不加0会漏算一些情况
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        return res

# leetcode submit region end(Prohibit modification and deletion)
