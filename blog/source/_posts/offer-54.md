---
title: offer-54
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-12 11:28:15
---

给定一棵二叉搜索树，请找出其中第 `k` 大的节点的值。



**示例 1:**

```
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
```

**示例 2:**

```
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
```



**限制：**

- 1 ≤ k ≤ 二叉搜索树元素个数

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
    public int kthLargest(TreeNode root, int k) {
        Map<TreeNode, Integer> numMap = new HashMap<>();
        int allNum = createNumMap(numMap, root);
        

        return getKth(numMap, root, allNum + 1 - k);
    }

    private int getKth(Map<TreeNode, Integer> numMap, TreeNode node, int k) {
        if (k < 1) {
            return -1;
        }

        int leftNum = node.left == null ? 0 : numMap.get(node.left);

        if (leftNum >= k) {
            return getKth(numMap, node.left, k);
        } else if (leftNum + 1 == k) {
            return node.val;
        } else {
            return getKth(numMap, node.right, k - leftNum - 1);
        }

    }

    private int createNumMap(Map<TreeNode, Integer> numMap, TreeNode node) {
        if (node == null) {
            return 0;
        }

        if (numMap.containsKey(node)) {
            return numMap.get(node);
        }

        int leftNum = createNumMap(numMap, node.left);
        int rightNum = createNumMap(numMap, node.right);
        numMap.put(node, leftNum + rightNum + 1);

        return leftNum + rightNum + 1;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
