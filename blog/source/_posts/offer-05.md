---
title: offer-05
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2022-12-01 11:21:27
---

```java
/**
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 

 

 示例 1： 

 输入：s = "We are happy."
输出："We%20are%20happy." 

 

 限制： 

 0 <= s 的长度 <= 10000 
 Related Topics字符串 

 👍 375, 👎 0 

*/
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String replaceSpace(String s) {
        StringBuilder sBuilder = new StringBuilder();

        for (char ch : s.toCharArray()) {
            if (ch == ' ') {
                sBuilder.append("%20");
            } else {
                sBuilder.append(ch);
            }
        }

        return sBuilder.toString();
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
