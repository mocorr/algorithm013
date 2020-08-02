# Week1学习笔记

---
## 1 学习方法

### 1.1 五毒神掌

过遍数 刻意练习

 - 第一遍：5分钟内没有思路直接看题解； 
 - 第二遍：自己做； 
 - 第三遍：一天后再次刷；
 - 第四遍：一周后刷； 
 - 第五遍：面试前一周恢复性训练。

考虑多种解题思路，分析时间/空间复杂度，看高票题解

### 1.2 费曼学习法

以教促学

### 1.3 TIPS

 - 善用脑图
 - 分清优先级
 - 碎片时间学习
 - 不必看算法导论
 - 加固语言基础
 - 熟练IDE的快捷键操作

## 2 数据结构

 1. 数组、链表、跳表
 跳表基于链表，元素必须有序，对标(取代)平衡树和二分查找。
 2. 栈、队列、优先队列、双端队列

需掌握如下知识点：

 - 原理和实现
 - 时间复杂度和空间复杂度
 - 在工程中的应用

**加速常用思想：
升维——空间换时间**

## 3 算法

### 递归模板

    def recursion(level, param1, param2, ...):
        # recursion terminator
        if level > MAX_LEVEL:
    	   process_result
    	   return
        # process logic in current level
        process(level, data...)
        # drill down
        self.recursion(level + 1, p1, ...)
        # reverse the current level status if needed




