---
title: offer-32-3
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-15 11:27:52
---

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。



例如:
给定二叉树: `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回其层次遍历结果：

```
[
  [3],
  [20,9],
  [15,7]
]
```



**提示：**

1. `节点总数 <= 1000`



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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }

        Stack<TreeNode> nodeStack1 = new Stack<>();
        Stack<TreeNode> nodeStack2 = new Stack<>();
        List<List<Integer>> resultList = new ArrayList<>();

        nodeStack1.push(root);

        while (!nodeStack1.isEmpty() || !nodeStack2.isEmpty()) {
            List<Integer> layer = new ArrayList<>();
            boolean traceStack1 = !nodeStack1.isEmpty();
            Stack<TreeNode> nodeStack = traceStack1 ? nodeStack1 : nodeStack2;

            while (!nodeStack.isEmpty()) {
                TreeNode node = nodeStack.pop();
                layer.add(node.val);

                if (traceStack1) {
                    if (node.left != null) {
                        nodeStack2.push(node.left);
                    }
                    if (node.right != null) {
                        nodeStack2.push(node.right);
                    }
                } else {
                    if (node.right != null) {
                        nodeStack1.push(node.right);
                    }
                    if (node.left != null) {
                        nodeStack1.push(node.left);
                    }
                }

            }
            resultList.add(layer);
        }

        return resultList;

    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
