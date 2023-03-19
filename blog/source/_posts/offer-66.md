---
title: offer-66
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-03-01 19:53:18
---

给定一个数组 `A[0,1,…,n-1]`，请构建一个数组 `B[0,1,…,n-1]`，其中 `B[i]` 的值是数组 `A` 中除了下标 `i` 以外的元素的积, 即 `B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]`。不能使用除法。



**示例:**

```
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
```



**提示：**

- 所有元素乘积之和不会溢出 32 位整数
- `a.length <= 100000`

```java
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int[] constructArr(int[] a) {
        if (a == null || a.length == 0) {
            return a;
        }

        int[] pre = new int[a.length];

        pre[0] = 1;

        for (int i = 1; i < a.length; i++) {
            pre[i] = pre[i - 1] * a[i - 1];
        }

        int[] suf = new int[a.length];

        suf[a.length - 1] = 1;

        for (int i = a.length - 2; i >= 0; i--) {
            suf[i] = suf[i + 1] * a[i + 1];
        }

        int[] result = new int[a.length];

        for (int i = 0; i < a.length; i++) {
            result[i] = pre[i] * suf[i];
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
