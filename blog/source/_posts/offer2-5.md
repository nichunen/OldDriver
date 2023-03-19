---
title: offer2-5
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-03-09 11:50:56
---

给定一个字符串数组 `words`，请计算当两个字符串 `words[i]` 和 `words[j]` 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。



**示例 1:**

```
输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。
```

**示例 2:**

```
输入: words = ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。
```

**示例 3:**

```
输入: words = ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。
```



**提示：**

- `2 <= words.length <= 1000`
- `1 <= words[i].length <= 1000`
- `words[i]` 仅包含小写字母

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int maxProduct(String[] words) {
        if (words == null || words.length == 0) {
            return 0;
        }
        Map<String, Integer> wordMap = new HashMap<>();

        for (String word : words) {
            int bitNum = 0;

            for (char ch : word.toCharArray()) {
                bitNum = (bitNum | (1 << (ch - 'a')));
            }

            wordMap.put(word, bitNum);
        }

        int result = 0;

        for (int i = 0; i < words.length - 1; i++) {
            for (int j = i + 1; j < words.length; j++) {
                String one = words[i];
                String two = words[j];

                if ((wordMap.get(one) & wordMap.get(two)) == 0 && one.length() * two.length() > result) {
                    result = one.length() * two.length();
                }
            }
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
