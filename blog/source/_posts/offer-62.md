---
title: offer-62
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-24 11:29:56
---

0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。



**示例 1：**

```
输入: n = 5, m = 3
输出: 3
```

**示例 2：**

```
输入: n = 10, m = 17
输出: 2
```



**限制：**

- `1 <= n <= 10^5`
- `1 <= m <= 10^6`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int lastRemaining(int n, int m) {
        if (n <= 0 || m <= 0) {
            return -1;
        }
        List<Integer> myList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            myList.add(i);
        }

        int index = -1;
        while (myList.size() > 1) {
            index += m;
            index = index % myList.size();
            myList.remove(index);
            index--;
        }

        return myList.get(0);
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
