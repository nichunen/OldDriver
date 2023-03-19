---
title: offer-33
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-16 11:33:05
---

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 `true`，否则返回 `false`。假设输入的数组的任意两个数字都互不相同。



参考以下这颗二叉搜索树：

```
     5
    / \
   2   6
  / \
 1   3
```

**示例 1：**

```
输入: [1,6,3,2,5]
输出: false
```

**示例 2：**

```
输入: [1,3,2,6,5]
输出: true
```



**提示：**

1. `数组长度 <= 1000`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean verifyPostorder(int[] postorder) {
        if (postorder == null) {
            return false;
        }

        if (postorder.length <= 2) {
            return true;
        }

        return isPost(postorder, 0, postorder.length - 1);
    }

    private boolean isPost(int[] postorder, int from, int to) {
        if (to - from <= 1) {
            return true;
        }

        int firstBiggerIndex = to;

        int toValue = postorder[to];

        for (int i = from; i < to; i++) {
            if (postorder[i] > toValue) {
                firstBiggerIndex = i;
                break;
            }
        }

        for (int i = firstBiggerIndex; i < to; i++) {
            if (postorder[i] < toValue) {
                return false;
            }
        }

        return isPost(postorder, from, firstBiggerIndex - 1) && isPost(postorder, firstBiggerIndex, to - 1);
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
