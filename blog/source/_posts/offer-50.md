---
title: offer-50
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-08 10:57:48
---

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

**示例 1:**

```
输入：s = "abaccdeff"
输出：'b'
```

**示例 2:**

```
输入：s = "" 
输出：' '
```



**限制：**

```
0 <= s 的长度 <= 50000
```



```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public char firstUniqChar(String s) {
        Set<Character> chSet = new HashSet<>();
        Set<Character> duplicateChSet = new HashSet<>();

        Queue<Character> chQ = new LinkedList<>();

        for (char ch : s.toCharArray()) {
            if (!chSet.contains(ch)) {
                chQ.add(ch);
                chSet.add(ch);
            } else {
                duplicateChSet.add(ch);
            }
        }

        while (!chQ.isEmpty()) {
            char ch = chQ.poll();

            if (!duplicateChSet.contains(ch)) {
                return ch;
            }
        }

        return ' ';
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
