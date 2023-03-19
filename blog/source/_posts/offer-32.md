---
title: offer-32
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-12 10:58:17
---

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。



例如:
给定二叉树: `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回：

```
[3,9,20,15,7]
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
    public int[] levelOrder(TreeNode root) {
        if (root == null) {
            return new int[0];
        }

        Queue<TreeNode> nodeQueue = new LinkedList<>();
        List<Integer> resultList = new ArrayList<>();

        nodeQueue.add(root);

        while (!nodeQueue.isEmpty()) {
            int qSize = nodeQueue.size();
            for (int i = 0; i < qSize; i++) {
                TreeNode node = nodeQueue.poll();
                resultList.add(node.val);

                if (node.left != null) {
                    nodeQueue.add(node.left);
                }

                if (node.right != null) {
                    nodeQueue.add(node.right);
                }
            }
        }

        return resultList.stream().mapToInt(i->i).toArray();

    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
