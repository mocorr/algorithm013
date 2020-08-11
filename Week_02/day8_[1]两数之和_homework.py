# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 8755 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSumBad(self, nums: List[int], target: int) -> List[int]:
        """
        暴力法 时间复杂度O(n^2) 空间复杂度O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSumSort(self, nums: List[int], target: int) -> List[int]:
        """
        排序+双指针 两元素相等时不能取同一index
        时间复杂度O(nlogn): max(排序sort:O(nlogn),while:O(n)*index:O(1))
        空间复杂度O(n)
        """
        tmp = sorted(nums)
        i, j = 0, len(nums) - 1
        while i < j:
            if tmp[i] + tmp[j] < target:
                i += 1
            elif tmp[i] + tmp[j] > target:
                j -= 1
            else:
                if tmp[i] != tmp[j]:
                    return [nums.index(tmp[i]), nums.index(tmp[j])]
                else:
                    left = nums.index(tmp[i])
                    del nums[left]
                    right = nums.index(tmp[j]) + 1
                    return [left, right]

    def twoSumHashTwice(self, nums: List[int], target: int) -> List[int]:
        """
        两遍哈希 时间复杂度O(n) 空间复杂度O(n)
        第一遍建立倒排索引 第二遍判断
        """
        dic = dict()
        for i in range(len(nums)):  # 遍历方向一致 步长相等 必可合并
            dic[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in dic and dic[nums[i]] != i:
                return [i, dic[nums[i]]]

    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        """
        一遍哈希 时间复杂度O(n) 空间复杂度O(n)
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [i, dic[nums[i]]]
            dic[target - nums[i]] = i

# leetcode submit region end(Prohibit modification and deletion)
