---
title: offer-58-2
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-21 13:08:08
---

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。



**示例 1：**

```
输入: s = "abcdefg", k = 2
输出: "cdefgab"
```

**示例 2：**

```
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
```



**限制：**

- `1 <= k < s.length <= 10000`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String reverseLeftWords(String s, int n) {
        if (n == 0 || s == null || s.length() == 0) {
            return s;
        }

        int k = n % s.length();

        return s.substring(k) + s.substring(0, k);
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```