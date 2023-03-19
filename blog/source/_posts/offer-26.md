---
title: offer-26
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-04 14:05:57
---

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

`     3     / \    4   5   / \  1   2`
给定的树 B：

`   4    /  1`
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

**示例 1：**

```
输入：A = [1,2,3], B = [3,1]
输出：false
```

**示例 2：**

```
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
```

**限制：**

```
0 <= 节点个数 <= 10000
```

```java

//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSubStructure(TreeNode A, TreeNode B) {
        if (A == null || B == null) {
            return false;
        }

        if (A.val == B.val && isSame(A, B)) {
            return true;
        }

        return isSubStructure(A.left, B) || isSubStructure(A.right, B);
    }


    private boolean isSame(TreeNode nodeA, TreeNode nodeB) {
        if (nodeB == null) {
            return true;
        }

        if (nodeA == null) {
            return false;
        }

        if (nodeA.val != nodeB.val) {
            return false;
        } else {
            return isSame(nodeA.left, nodeB.left) && isSame(nodeA.right, nodeB.right);
        }
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
