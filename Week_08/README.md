# Week8学习笔记

---

## 1. 知识点
### 1.1 位运算

#### 1.1.1 二进制基础概念：
[参考链接][1]
- 原码
- 补码
- 反码
- 正数的二进制值，原码、补码、反码都一样
- 负数的二进制值是其补码，即反码加1

#### 1.1.2 位运算基本操作：
- 左移 : << 
- 右移 : >> 
- 按位或 : |
- 按位与 : &
- 按位取反 : ~
- 按位异或 : ^

#### 1.1.3 异或技巧
相同为0，不同为1.也可用**“进位加法”**来理解
- x ^ 0 = X
- x ^ 1s = ~x  # 1s = ~ 0
- x ^ (~x) = 1s 
- x ^ x = 0
- c = a ^ b  => a ^ c = b, b ^c = a # 交换两数
- a ^ b ^ c = a ^(b ^ c) = (a ^ b) ^c # associative 

#### 1.1.4 位运算常用技巧：
- & 1 只取最后一位
- n & (-n) 获取n最右边的1
- n & (n - 1) 将n最右边的1设置为0
  - 解释:
  - 若n是奇数: n最末位必为1，n-1最末位必为0，其他位相同，n & (n - 1) 最末位必为0
  - 若n是偶数: n最末位必为0，n-1必向最后一个1借位，n & (n - 1) 同样消去最后一个1
- n & ~n = 0
- 判断奇偶：
  - x % 2 == 1 ---> (x & 1) == 1; // 奇数
  - x % 2 == 0 ---> (x & 1) == 0; // 偶数
- 除以2
  - x = x / 2 ---> x = x >> 1;
  - mid = (left + right) / 2 ---> mid = (left + right) >> 1;

#### 1.1.5 指定位置的位运算：
- 将 x 最右边的 n 位清零： x & (~0 << n)
- 获取 x 的第 n 位值(0 或者 1)：(x >> n) & 1
- 获取 x 的第 n 位的幂值：x & (1 << n)
- 仅将第 n 位 置为1：x | (1 << n)
- 仅将第 n 位 置为0：x & (~(1 << n))
- 将 x 最高位至第 n 位(含) 清零：x & ((1 << n) - 1)

### 1.2 布隆过滤器和LRU缓存

#### 1.2.1 布隆过滤器
将一个对象经过多次hash函数之后,将其映射到一个很长的二进制位上。

- 优点：空间效率和查询时间都远超一般算法
- 缺点：一定的误识别率、删除困难

可以挡在数据库外层作为缓存：

- 查询为不存在：一定不存在；
- 查询为存在: 可能存在。

#### 1.2.2 LRU缓存

 Least Recently Used=最近最少使用，使用HashMap和双向链表可以实现。
 
- 查询: O(1)
- 修改/更新: O(1)

### 1.3 排序算法

参考链接: [十大经典排序][2]

分为 比较类排序 和 非比较排序

- 比较类排序
通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此也成为非线形时间比较类排序
 - 交换排序：冒泡排序、快速排序
 - 插入排序：(简单)插入排序、希尔排序
 - 选择排序：(简单)选择排序、堆排序
 - 归并排序：二路归并排序、多路归并排序
- 非比较排序
不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线形时间运行，因此也成为线形时间非比较类排序
 - 计数排序
 - 桶排序
 - 基数排序


#### 1.3.1 初级排序

##### 1.3.1.1 冒泡排序

交换相邻两个元素，每次都有一个最大的数沉底
 
```python
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(1, len(nums)-i):
            if nums[j] <= nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return
```


##### 1.3.1.2 选择排序

每次挑选未排序元素中最小到值放到当前位置

```python
def choice_sort(nums):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return
```

##### 1.3.1.3 插入排序

将当前位置的元素插入到已排序数组中正确的位置

```python
def insertion_sort(nums):
    for i in range(1, len(nums)):
        cur_num = nums[i]
        j = i
        while j > 0 and nums[j-1] > cur_num:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = cur_num
    return

```

##### 1.3.1.4 希尔排序

插入排序是间隔为1的希尔排序，希尔排序是间隔为h的插入排序

```python
def shell_sort(nums):
    h = 1
    while h < len(nums):
        h = 3 * h + 1
    while h > 0:
        for i in range(h, len(nums)):
            cur_num = nums[i]
            j = i
            while j > 0 and nums[j-h] > cur_num:
                nums[j] = nums[j-h]
                j -= h
            nums[j] = cur_num
        h //= 3
    return
```

#### 1.3.2 高级排序

##### 1.3.2.1 归并排序

建立在归并操作上的一种有效，稳定的排序算法，该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。

- 第一步：申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
- 第二步：设定两个指针，最初位置分别为两个已经排序序列的起始位置
- 第三步：比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
- 重复步骤3直到某一指针超出序列尾

```python
def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i +=1
        else:
            temp.append(nums[j])
            j +=1
    while i<=mid:
        temp.append(nums[i])
        i +=1
    while j<=right:
        temp.append(nums[j])
        j +=1
    nums[left:right+1] = temp
```

##### 1.3.2.2 快速排序

通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

- 从数列中挑出一个元素，称为 “基准”（pivot）；
- 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
- 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

```python
# 版本1
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)
    
def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
    
# 版本2
def quick_sort(nums):    
    if len(nums) >= 2:  # 递归入口及出口        
        mid = nums[len(nums)//2]  # 选取基准值，也可以选取第一个或最后一个元素        
        left, right = [], []  # 定义基准值左右两侧的列表        
        nums.remove(mid)  # 从原始数组中移除基准值        
        for num in nums:            
            if num >= mid:                
                right.append(num)            
            else:                
                left.append(num)        
        return quick_sort(left) + [mid] + quick_sort(right)    
    else:        
        return nums

```

##### 1.3.2.3 堆排序

堆的插入：O(logN)，取最大/最小值 O(1)
- 数组元素依次建立小顶堆
- 依次取堆顶元素，并删除

```python
def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2*parent_index+1
    while child_index < length:
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index+1
        if temp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2*parent_index + 1
    nums[parent_index] = temp


def heapsort(nums):
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
```

#### 1.3.3 特殊排序(非比较类排序)

 O(n+k)
 

- 计数排序
要求输入的数据必须是有确定范围的整数。 思路：将输入的数据值转化为键存储在额外开辟的数组空间，然后依次把计数大于 1 的填充回原数组；

- 桶排序
思路：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或以递归方式继续使用桶排序进行排序）。

- 基数排序
 - 基数排序是按照低位先排序，然后收集；
 - 再按照高位先排序，然后再收集；以此类推，直到最高位。
 - 有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。


  [1]: http://www.361way.com/bitwise-operators/5778.html
  [2]: https://www.cnblogs.com/onepixel/p/7674659.html