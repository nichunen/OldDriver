---
title: offer-41
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-30 19:50:18
---

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

- void addNum(int num) - 从数据流中添加一个整数到数据结构中。
- double findMedian() - 返回目前所有元素的中位数。

**示例 1：**

```
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
```

**示例 2：**

```
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
```



**限制：**

- 最多会对 `addNum、findMedian` 进行 `50000` 次调用。



```java
//leetcode submit region begin(Prohibit modification and deletion)
class MedianFinder {
    private PriorityQueue<Integer> smallQ;
    private PriorityQueue<Integer> bigQ;

    /** initialize your data structure here. */
    public MedianFinder() {
        smallQ = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer v1, Integer v2) {
                return -v1.compareTo(v2);
            }
        });

        bigQ = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer v1, Integer v2) {
                return v1.compareTo(v2);
            }
        });
    }

    public void addNum(int num) {
        if (smallQ.isEmpty() || num < smallQ.peek()) {
            smallQ.add(num);
        } else {
            bigQ.add(num);
        }

        if (smallQ.size() - bigQ.size() > 1) {
            bigQ.add(smallQ.poll());
        } else if (bigQ.size() > smallQ.size()) {
            smallQ.add(bigQ.poll());
        }
    }

    public double findMedian() {
        if (smallQ.size() - bigQ.size() == 1) {
            return (double)(smallQ.peek());
        } else if (smallQ.size() > 0 && smallQ.size() == bigQ.size()) {
            return (double)(smallQ.peek() + bigQ.peek()) / 2;
        } else {
            return (double)0;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
//leetcode submit region end(Prohibit modification and deletion)
```
