---
title: offer-46
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-03 11:39:29
---

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。



**示例 1:**

```
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
```



**提示：**

- `0 <= num < 231`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int translateNum(int num) {
        String numStr = Integer.valueOf(num).toString();
        int[] f = new int[numStr.length()];
        int lastNum = -1;

        for (int i = 0; i < numStr.length(); i++) {
            int curNum = numStr.charAt(i) - '0';
            if (i == 0) {
                f[i] = 1;
            } else {
                if (lastNum * 10 + curNum >= 10 && lastNum * 10 + curNum <= 25) {
                    if (i == 1) {
                        f[i] = 2;
                    } else {
                        f[i] = f[i - 1] + f[i - 2];
                    }
                } else {
                    f[i] = f[i - 1];
                }
            }
            lastNum = curNum;
        }
        return f[numStr.length() - 1];
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
