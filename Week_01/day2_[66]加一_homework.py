# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。 
# 
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。 
# 
#  你可以假设除了整数 0 之外，这个整数不会以零开头。 
# 
#  示例 1: 
# 
#  输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#  
# 
#  示例 2: 
# 
#  输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#  
#  Related Topics 数组 
#  👍 514 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def plusOnePython(self, digits: List[int]) -> List[int]:
        """
        python特解 时间复杂度o(n)
        """
        num = ''
        for i in digits:
            num += str(i)
        num = int(num) + 1
        res = [int(j) for j in str(num)]
        return res

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        常规解法：从个位开始遍历 若等于9则进位 首位若为0改为1末尾补0
        时间复杂度o(n)
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        if digits[0] == 0:
            digits[0] = 1
            digits.append(0)
        return digits

# leetcode submit region end(Prohibit modification and deletion)
