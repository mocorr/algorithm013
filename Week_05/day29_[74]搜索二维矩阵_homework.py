# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  示例 1: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false 
#  Related Topics 数组 二分查找 
#  👍 226 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        """
        转为1维 二分法
        """
        vect = []
        for row in matrix:
            vect.extend(row)
        left = 0
        right = len(vect) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > vect[mid]:
                left = mid + 1
            elif target < vect[mid]:
                right = mid - 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        直接二分法
        """
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // n][mid % n] > target:
                right = mid - 1
            elif matrix[mid // n][mid % n] < target:
                left = mid + 1
            else:
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
