---
title: offer-27
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-05 14:50:09
---

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

`     4    /   \   2     7  / \   / \ 1   3 6   9`
镜像输出：

```
     4    /   \   7     2  / \   / \ 9   6 3   1
```



**示例 1：**

```
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
```



**限制：**

```
0 <= 节点个数 <= 1000
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
    public TreeNode mirrorTree(TreeNode root) {
        doFlip(root);
        return root;
    }

    private void doFlip(TreeNode node) {
        if (node == null) {
            return;
        }

        TreeNode left = node.left;
        node.left = node.right;
        node.right = left;
        doFlip(node.left);
        doFlip(node.right);
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
