# Week2学习笔记

---

## 1. 方法及模板
### 1.1 面试Coding四部曲
1. clarification
2. possible solutions ->optimal time and space
3. code
4. test

### 1.2 二叉树的遍历模板
#### 1.2.1 二叉树递归
```Python
class Solution:
    def traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 前序
        return [root.val] + self.traversal(root.left) + self.traversal(root.right)
        # # 中序
        # return self.traversal(root.left) + [root.val] + self.traversal(root.right)
        # # 后序
        # return self.traversal(root.left) + self.traversal(root.right) + [root.val]
```
#### 1.2.2 二叉树迭代（手动维护栈以模拟递归）
```Python
class Solution:
    """
    Pythonic, 其他语言手动加上visited标记即可。
    """
    def traversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            curr = stack.pop()
            if isinstance(curr, TreeNode):
                # 前序
                stack.extend([curr.right, curr.left, curr.val])
                # # 中序
                # stack.extend([curr.right, curr.val, curr.left])
                # # 后序
                # stack.extend([curr.val, curr.right, curr.left])
            elif isinstance(curr, int):
                res.append(curr)
        return res
```

## 2. 知识点

### 2.1 哈希表、映射、集合
* 通过哈希函数将key转换成下标，并存入值
* 核心问题：哈希函数设计、哈希碰撞解决
* 哈希碰撞解决方法：开放寻址法、链表法
* 时间复杂度：查找、插入、删除O(1)
* Worst时间复杂度：哈希碰撞，退化为链表，查找、插入、删除O(n)

### 2.2 树、二叉树、二叉搜索树
* 思想：链表是特殊的树，树是特殊的图

* 树的题型总结:
https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/solution/yi-tao-quan-fa-shua-diao-nge-bian-li-shu-de-wen--3/

#### 2.2.1 二叉树
* 完全二叉树可用一维数组实现
* 二叉树的遍历
  * 前序遍历（Pre-order）：根-左-右
  * 中序遍历（In-order）：左-根-右
  * 后序遍历（Post-order）：左-右-根

#### 2.2.2 二叉搜索树(BST, Binary Search Tree)：
* 左子树上的所有值均小于其根节点的值
* 右子树上的所有值均大于其根节点的值
* 每个子树也均为二叉搜索树
* 中序遍历递增；
* 复杂度：查询、插入、删除的复杂度O(logn)；

### 2.3 堆和二叉堆
* 最大/小值置顶的数据结构,O(1)
* 二叉堆：
    * 完全二叉树 
    * 插入：末尾上浮,O(logN)
    * 删除：堆首下沉,O(logN)
    * 可用一维数组实现：2*i+1、2*i+2
* Python手写堆：https://leetcode-cn.com/problems/top-k-frequent-elements/solution/quan-shou-xie-jian-li-kge-yuan-su-de-zui-xiao-dui-/

### 2.4 图(Graph)
* 图的类型：无/有向图、无/有权图
* 图的表示：邻接矩阵、邻接表
* 点
    * 入/出度
    * 是否连通
* 边（edge）
    * 有向和无向
    * 权重
* 图可能有环，BFS需要加上visited；树无环不需要



