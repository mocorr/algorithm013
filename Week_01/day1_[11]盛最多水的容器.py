# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, 
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。 
# 
#  说明：你不能倾斜容器，且 n 的值至少为 2。 
# 
#  
# 
#  
# 
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 
# 
#  
# 
#  示例： 
# 
#  输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 
#  Related Topics 数组 双指针 
#  👍 1676 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAreaBad(self, height: List[int]) -> int:
        """
        暴力法 两层循环 时间复杂度高o(n^2) 空间复杂度O(1)
        """
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                max_area = max(min(height[i], height[j]) * (j - i), max_area)
        return max_area

    def maxArea(self, height: List[int]) -> int:
        """
        双指针法 向内移动较短的线 时间复杂度O(n) 空间复杂度O(1)
        """
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            max_area = max(min(height[i], height[j]) * (j - i), max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
# leetcode submit region end(Prohibit modification and deletion)
