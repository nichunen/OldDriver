---
title: offer2-2
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-03-06 13:27:38
---

给定两个 01 字符串 `a` 和 `b` ，请计算它们的和，并以二进制字符串的形式输出。

输入为 **非空** 字符串且只包含数字 `1` 和 `0`。



**示例 1:**

```
输入: a = "11", b = "10"
输出: "101"
```

**示例 2:**

```
输入: a = "1010", b = "1011"
输出: "10101"
```



**提示：**

- 每个字符串仅由字符 `'0'` 或 `'1'` 组成。
- `1 <= a.length, b.length <= 10^4`
- 字符串如果不是 `"0"` ，就都不含前导零。

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String addBinary(String a, String b) {
        StringBuilder resultB = new StringBuilder();

        int indexA = a == null ? -1 : a.length() - 1;
        int indexB = b == null ? -1 : b.length() - 1;
        int carry = 0;

        while (indexA >= 0 || indexB >= 0) {
            int aBit = indexA >= 0 ? a.charAt(indexA) - '0' : 0;
            int bBit = indexB >= 0 ? b.charAt(indexB) - '0' : 0;

            resultB.append((aBit + bBit + carry) % 2);
            if (carry + aBit + bBit > 1) {
                carry = 1;
            } else {
                carry = 0;
            }
            indexA--;
            indexB--;
        }

        if (carry == 1) {
            resultB.append(1);
        }

        return resultB.reverse().toString();
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
