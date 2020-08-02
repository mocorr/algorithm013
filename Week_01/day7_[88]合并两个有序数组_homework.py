# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。 
# 
#  
# 
#  说明: 
# 
#  
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。 
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。 
#  
# 
#  
# 
#  示例: 
# 
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6] 
#  Related Topics 数组 双指针 
#  👍 578 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mergeBad(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        合并+sort 时间复杂度O((n+m)log(n+m)) 空间复杂度O(1)
        """
        nums1[:] = sorted(nums1[:m] + nums2)  # 直接用nums1赋值会把nums1放到新的内存地址

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        双指针法 时间复杂度O(m+n) 空间复杂度O(m)
        """
        nums1_copy = nums1.copy()[:m]
        i = 0
        j = 0
        for k in range(len(nums1)):
            if i < m and j < n:
                if nums1_copy[i] < nums2[j]:
                    nums1[k] = nums1_copy[i]
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1
            elif i < m:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

# leetcode submit region end(Prohibit modification and deletion)
