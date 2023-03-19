---
title: offer-64
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-27 14:54:43
---

求 `1+2+...+n` ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。



**示例 1：**

```
输入: n = 3
输出: 6
```

**示例 2：**

```
输入: n = 9
输出: 45
```



**限制：**

- `1 <= n <= 10000`

```java
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    class InnerC {
        public static int num = 0;
        InnerC(int n) {
            num += n;
        }
    }

    private boolean innerFunc(int n) {
        InnerC s = new InnerC(n);
        return n > 0 && innerFunc(n - 1);
    }
    public int sumNums(int n) {
        InnerC.num = 0;
        innerFunc(n);
        return InnerC.num;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
