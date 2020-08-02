# 学习笔记



## 高效学习数据结构与算法的真确打开方式

**看视频：**

> 1.5-2.0倍数播放，难点（暂停+反复）

**刷题：**

> 切题四件套：
>
> Clarification：理解题意（目标、限制）
>
> Possible solutions:想多种解法，寻求最优解
>
> ​	Compare：（Time/Space）
>
> ​	optimal：（加强）
>
> Coding：（多写）
>
> Test cases：测试
>
> 五毒神掌：
>
> 过遍数、敢于放手、敢于死记硬背、善于看高手的代码，不要死磕！！！**五分钟想不出来直接看题解**
>
> 第一遍：
>
> 读题+思考（5min）
>
> ​	如果不知道怎么做的话：直接看解法（多解法、比较优劣）
>
> 背诵、默写好解法（理解）
>
> 
>
> 第二遍：（第一遍完成后）
>
> 马上自己写 -> LeetCode提交
>
> 多种解法比较、体会 -> 优化
>
> 
>
> 第三遍： （一天后）
>
> 不同解法熟练程度- > 专项训练
>
> 
>
> 第四遍：（一周以后）
>
> 反复练习相同、相类似的题目
>
> 
>
> 第五遍：
>
> 面试前一周恢复性训练

**学习三步骤：**

> 预习:基础知识点预习与查看
>
> 课堂互动：思考问题、解决问题
>
> 课后作业：
>
> LeetCode 300+的积累
>
> ```
> Chunk it up：切碎知识点
> 庖丁解牛+脉络连接
> 
> Deliberate Practicaing 刻意练习
> 过遍数：五遍刷题
> 练习弱项、专项练习
> 
> 
> Feedback 反馈：
> 即时反馈：
> 主动寻求反馈：自己去找——看高手怎么写、操作的
> 被动反馈：高手点评
> ```

## 数据结构与算法总览

**数据结构：**

```
一维：
基础：数组arry（string）、链表Link list
高级：栈（stack）、队列（Queue）、双端队列（deque）、集合（Set）、映射Map（hash or map）、
二维：
基础：树（Tree）、图（Graph）
高级：
二叉搜索树（binary search tree）：根节点大于左子树，小于右子树
特殊的二叉搜索树：红黑树（Red-Black Tree）、AVL、堆（Heap）、并查集（disjoin set）、字典树（Trie）
特殊：
位运算：Bitwise,布隆过滤器BloomFilter
缓存：LUR cache
```

**算法：**

```
逻辑切换：if-else,switch -> branch
循环：for, while loop -> lteration
递归：Recursion（Divide & Conquer， Back trace）
搜索（Search）：深度优先搜索Depth first Search，广度优先搜索Breadth first seach
动态规划：Dynamic Programing
二分查找：Binary Search
贪心： Greedy
数学：Math、几何Geometry
```



## 课堂内容笔记：

**数组：**有序的元素序列。若将有限个类型相同的变量的集合命名，那么这个名称为<u>数组</u>名

查：O（1）：由于其特性内存地址有序，能够任意的访问到数组中任何一个元素

增删：由于是连续的，所以若想修改须将新增的元素与原数组重新排序（一般为新建一个数组将）

元素末尾插入删除：O（1）

元素中任意位置插入删除：O（n）

**链表：**存储单元非连续、非顺序的存储结构，元素更具链表中的指针衔接实现

查O（n）：由于其特性内存地址由指针衔接，能够任意修改的到中任何一个元素。内存地址无序

增删：O（1）：由指针衔接

**跳表：**特殊的链表，只能使用于元素有序的情况；维护成本较高

对标（可取代）：平衡树、二分查找  插入/删除/搜索 都是O(log n) 的结构

简单优化：添加头尾指针

查：O（log n）

增删：O（1），由于必须是有序