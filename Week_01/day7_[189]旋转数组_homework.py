# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
# 
#  示例 2: 
# 
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100] 
# 
#  说明: 
# 
#  
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。 
#  要求使用空间复杂度为 O(1) 的 原地 算法。 
#  
#  Related Topics 数组 
#  👍 640 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    k要对n取模 k=n时等效于不操作 ①节省操作次数 ②避免越界
    """
    def rotateBad(self, nums: List[int], k: int) -> None:
        """
        暴力遍历法 时间复杂度o(n*k) 空间复杂度o(1)
        """
        for i in range(k):
            tail = nums[-1]
            for j in range(len(nums) - 1, 0, -1):
                nums[j] = nums[j - 1]
            nums[0] = tail

    def rotate(self, nums: List[int], k: int) -> None:
        """
        三次反转 时间复杂度o(n) 空间复杂度o(1)
        """
        n = len(nums)
        k = k % n
        self.swap(nums, 0, n-1)
        self.swap(nums, 0, k-1)
        self.swap(nums, k, n-1)

    def swap(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

# leetcode submit region end(Prohibit modification and deletion)
