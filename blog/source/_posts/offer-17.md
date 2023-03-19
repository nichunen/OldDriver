---
title: offer-17
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2022-12-22 13:59:18
---

输入数字 `n`，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

**示例 1:**

```
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
```



说明：

- 用返回一个整数列表来代替打印
- n 为正整数



```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int[] printNumbers(int n) {
        int maxV = 0;

        for (int i = 0; i < n; i++) {
            maxV = maxV * 10 + 9;
        }

        int[] result = new int[maxV];

        for (int i = 1; i <= maxV; i++) {
            result[i - 1] = i;
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
