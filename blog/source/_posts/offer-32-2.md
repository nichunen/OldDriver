---
title: offer-32-2
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-13 11:23:46
---

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。



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
  [9,20],
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

        Queue<TreeNode> nodeQueue = new LinkedList<>();
        List<List<Integer>> resultList = new ArrayList<>();

        nodeQueue.add(root);

        while (!nodeQueue.isEmpty()) {
            int qSize = nodeQueue.size();
            List<Integer> layer = new ArrayList<>();
            for (int i = 0; i < qSize; i++) {
                TreeNode node = nodeQueue.poll();
                layer.add(node.val);

                if (node.left != null) {
                    nodeQueue.add(node.left);
                }

                if (node.right != null) {
                    nodeQueue.add(node.right);
                }
            }
            resultList.add(layer);
        }

        return resultList;

    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
