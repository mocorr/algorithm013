# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 668 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroesBad(self, nums: List[int]) -> None:
        """
        时间复杂度o(n^2) 对0计数优于直接循环整个数组
        """
        zero_counts = nums.count(0)
        for i in range(zero_counts):
            nums.append(0)
            nums.remove(0)

    def moveZeroes(self, nums: List[int]) -> None:
        """
        快慢指针法 时间复杂度o(n) i主动遍历 j被动移动 i与j相同时不做多余交换
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = 0, nums[i]
                j += 1

# leetcode submit region end(Prohibit modification and deletion)
