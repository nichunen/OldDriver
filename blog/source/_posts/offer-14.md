---
title: offer-14
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2022-12-19 14:13:34
---

给你一根长度为 `n` 的绳子，请把绳子剪成整数长度的 `m` 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 `k[0],k[1]...k[m-1]` 。请问 `k[0]*k[1]*...*k[m-1]` 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

**示例 1：**

```
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
```

**示例 2:**

```
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
```

**提示：**

- `2 <= n <= 58`

```java
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int cuttingRope(int n) {
        if (n == 2 || n == 3) {
            return n - 1;
        }
        Map<Integer, Integer> resultMap = new HashMap<>();
        return cutting(resultMap, n);
    }

    private int cutting(Map<Integer, Integer> resultMap, int n) {
        if (resultMap.containsKey(n)) {
            return resultMap.get(n);
        }

        int result = 0;

        if (n <= 4) {
            result = n;
        } else {
            for (int i = 1; i <= n / 2; i++) {
                result = Math.max(result, cutting(resultMap, i) * cutting(resultMap, n - i));
            }
        }

        resultMap.put(n, result);
        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
