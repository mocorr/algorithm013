from typing import List


# 输入整数数组arr ，找出其中最小的k个数。例如，输入4、5、1、6、2、7、3、8
# 这8个数字，则最小的4个数字是1、2、3、4。


# 解法一：排序法：直接排序返回长度为K的数组
def getLeastNumbers1(arr: List[int], k: int) -> List[int]:
    arr.sort()
    return arr[:k]


# 解法二：用一个大根堆实时维护数组的前 kk 小值。
# 首先将前 kk 个数插入大根堆中，随后从第 k+1k+1 个数开始遍历，
# 如果当前遍历到的数比大根堆的堆顶的数要小，就把堆顶的数弹出，再插入当前遍历到的数。
# 最后将大根堆里的数存入数组返回
def getLeastNumbers2(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return list()
    hp = [-x for x in arr[:k]]
    heapq.heapify(hp)
    for i in range(k, len(arr)):
        if -hp[0] > arr[i]:
            heapq.heappop(hp)
            heapq.heappush(hp, -arr[i])
    ans = [-x for x in hp]
    return ans
