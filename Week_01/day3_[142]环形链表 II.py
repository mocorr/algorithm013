# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。 
# 
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。 
# 
#  说明：不允许修改给定的链表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  
# 
#  示例 3： 
# 
#  输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
#  
# 
#  
# 
#  
# 
#  进阶： 
# 你是否可以不用额外空间解决此题？ 
#  Related Topics 链表 双指针 
#  👍 569 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycleHash(self, head: ListNode) -> ListNode:
        """
        哈希法 时间复杂度O(n) 空间复杂度O(n)
        """
        tmp = []
        while head:
            if head in tmp:
                return head
            tmp.append(head)
            head = head.next
        return

    def detectCycle(self, head: ListNode) -> ListNode:
        """
        快慢指针法 时间复杂度O(n) 空间复杂度O(1)
        思路: 先找出快慢指针相遇点，再找出环入口
        定义:
            head到链表入口有a个节点（不计head），链表环有b个节点
        阶段1:
            找出快慢指针相遇点 快2慢1
            以慢指针为坐标系：慢指针原地不动，快指针每次追1步，若有环必会相遇
            f = 2s, f = s + nb ==>  s = nb, f = 2nb
        阶段2:
            找出环入口
            a = 从head到达环入口步数 = 慢指针再走回到环入口步数
        """
        p1, p2 = self.getCross(head), head
        if not p1:
            return
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def getCross(self, head):
        faster, slower = head, head
        while faster and slower and faster.next:
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                return faster
        return

# leetcode submit region end(Prohibit modification and deletion)
