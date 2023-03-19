---
title: offer-60
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-23 11:09:11
---

把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。



你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。



**示例 1:**

```
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
```

**示例 2:**

```
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
```



**限制：**

```
1 <= n <= 11
```



```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public double[] dicesProbability(int n) {
        if (n <= 0) {
            return new double[0];
        }

        double[][] f = new double[n + 1][6 * n + 1];
        double magic = (double) 1 / 6;

        for (int i = 1; i <= 6; i++) {
            f[1][i] = magic;
        }

        int start = 1, end = 6;

        for (int i = 2; i <= n; i++) {
            for (int j = start; j <= end; j++) {
                for (int k = 1; k <= 6; k++) {
                    f[i][j + k] += f[i - 1][j] * magic;
                }
            }

            start++;
            end+=6;
        }

        double[] result = new double[end - start + 1];

        for (int i = start; i <= end; i++) {
            result[i - start] = ((double)Math.round(f[n][i] * 100000)) / 100000.0;
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
