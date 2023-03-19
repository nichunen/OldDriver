---
title: offer-65
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-28 11:34:30
---

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。



**示例:**

```
输入: a = 1, b = 1
输出: 2
```



**提示：**

- `a`, `b` 均可能是负数或 0
- 结果不会溢出 32 位整数

**预备知识**

有符号整数通常用补码来表示和存储，补码具有如下特征：

- 正整数的补码与原码相同；负整数的补码为其原码除符号位外的所有位取反后加 1。
- 可以将减法运算转化为补码的加法运算来实现。
- 符号位与数值位可以一起参与运算。

**思路和算法**

虽然题目只要求了不能使用运算符 +、-、* 和 /，但是原则上来说也不宜使用类似的运算符 +=、-=、*= 和 /=，以及 sum 等方法。于是，我们使用位运算来处理这个问题。

首先，考虑两个二进制位相加的四种情况如下：

```java
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int add(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
