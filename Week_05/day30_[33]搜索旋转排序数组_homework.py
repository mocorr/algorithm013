# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。 
# 
#  你可以假设数组中不存在重复的元素。 
# 
#  你的算法时间复杂度必须是 O(log n) 级别。 
# 
#  示例 1: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#  
# 
#  示例 2: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1 
#  Related Topics 数组 二分查找 
#  👍 911 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 选择左闭右闭
        while left <= right:  # 由左闭右闭得终止条件
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:  # if左半边较正常
                if nums[left] <= target < nums[mid]:  # 且目标值在左半边
                    right = mid - 1
                else:  # 且目标值在右半边
                    left = mid + 1
            elif nums[mid] <= nums[right]:  # if右半边较正常
                if nums[mid] < target <= nums[right]:  # 且目标值在右半边
                    left = mid + 1
                else:  # 且目标值在左半边
                    right = mid - 1
        return -1
# leetcode submit region end(Prohibit modification and deletion)
