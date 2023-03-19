---
title: offer-55-2
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-14 11:38:29
---

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。



**示例 1:**

给定二叉树 `[3,9,20,null,null,15,7]`

```
    3
   / \
  9  20
    /  \
   15   7
```

返回 `true` 。

**示例 2:**

给定二叉树 `[1,2,2,3,3,null,null,4,4]`

```
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```

返回 `false` 。



**限制：**

- `0 <= 树的结点个数 <= 10000`

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
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        return getBalancedDepth(root) != -1;
    }


    private int getBalancedDepth(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int left = getBalancedDepth(node.left);
        if (left == -1) {
            return -1;
        }
        int right = getBalancedDepth(node.right);
        if (right == -1) {
            return -1;
        }

        int gap = left - right;

        if (gap < -1 || gap > 1) {
            return -1;
        }
        return left > right ? left + 1 : right + 1;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
