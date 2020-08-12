# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：head = [1,3,2]
# 输出：[2,3,1] 
# 
#  
# 
#  限制： 
# 
#  0 <= 链表长度 <= 10000 
#  Related Topics 链表 
#  👍 45 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reversePrint1(self, head: ListNode) -> List[int]:
        """
        存进数组 反转数组 时间复杂度O(n) 空间复杂度O(n)
        数组切片/反转：时间复杂度O(n)
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

    def reversePrint2(self, head: ListNode) -> List[int]:
        """
        节点入栈 出栈时记录 时间复杂度O(n) 空间复杂度O(n)
        """
        stack = []
        res = []
        while head:
            stack.append(head)
            head = head.next
        for i in range(len(stack)-1, -1, -1):
            res.append(stack[i].val)
        return res

    def reversePrint3(self, head: ListNode) -> List[int]:
        """
        原地反转链表(递归) 时间复杂度O(n) 空间复杂度O(n)
        """
        def helper(node):
            if not node or not node.next:
                return node
            new_head = helper(node.next)
            node.next.next, node.next = node, None
            return new_head
        res = []
        head = helper(head)
        while head:
            res.append(head.val)
            head = head.next
        return res

    def reversePrint(self, head: ListNode) -> List[int]:
        """
        原地反转链表(迭代) 时间复杂度O(n) 空间复杂度O(n)
        """
        pre, curr = None, head
        while curr:
            curr.next, curr, pre = pre, curr.next, curr
        res = []
        while pre:
            res.append(pre.val)
            pre = pre.next
        return res
# leetcode submit region end(Prohibit modification and deletion)
