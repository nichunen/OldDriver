---
title: offer-16
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2022-12-21 11:15:12
---

实现 [pow(*x*, *n*)](https://www.cplusplus.com/reference/valarray/pow/) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。



**示例 1：**

```
输入：x = 2.00000, n = 10
输出：1024.00000
```

**示例 2：**

```
输入：x = 2.10000, n = 3
输出：9.26100
```

**示例 3：**

```
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
```



**提示：**

- `-100.0 < x < 100.0`
- `-231 <= n <= 231-1`
- `-104 <= xn <= 104`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public double myPow(double x, int n) {
        int absN = n > 0 ? n : -n;
        
        if (n == Integer.MIN_VALUE) {
            if ((int)x == 1 || (int)x == -1) {
                return 1.0;
            } else {
                return 0.0;
            }
        }

        double result = 1.0;
        double curP = x;

        while (absN > 0) {
            if (absN % 2 == 1) {
                result *= curP;
            }

            absN = absN >> 1;
            curP = curP * curP;
        }

        if (n > 0) {
            return result;
        } else {
            return 1.0 / result;
        }
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
