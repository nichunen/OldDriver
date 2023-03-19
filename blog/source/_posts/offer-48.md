---
title: offer-48
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-06 16:30:01
---

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。



**示例 1:**

```
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2:**

```
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3:**

```
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```



提示：

- `s.length <= 40000`

```java
import java.util.HashMap;
import java.util.Map;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        int result = 0;
        Map<Character, Integer> chIndexMap = new HashMap<>();
        int curStart = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (chIndexMap.containsKey(ch)) {
                int len = i - curStart;

                if (len > result) {
                    result = len;
                }

                int end = chIndexMap.get(ch);
                for (int j = curStart; j <= end; j++) {
                    chIndexMap.remove(s.charAt(j));
                }
                curStart = end + 1;
            }
            chIndexMap.put(ch, i);
        }

        int len = s.length() - curStart;

        if (len > result) {
            result = len;
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
