---
title: offer-07
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2022-12-05 11:21:06
---

```java
/**
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。



 示例 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]


 示例 2:


Input: preorder = [-1], inorder = [-1]
Output: [-1]




 限制：

 0 <= 节点个数 <= 5000



 注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
preorder-and-inorder-traversal/
 Related Topics树 | 数组 | 哈希表 | 分治 | 二叉树

 👍 943, 👎 0

*/
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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return build(preorder, inorder, 0, preorder.length - 1, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int[] inorder, int preStart, int preEnd, int inStart, int inEnd) {
        if (preEnd < preStart || inEnd < inStart || preStart < 0 || inStart < 0 || preEnd >= preorder.length || inEnd >= inorder.length) {
            return null;
        }

        TreeNode node = new TreeNode();
        node.val = preorder[preStart];
        if (preEnd == preStart || inEnd == inStart) {
            return node;
        }
        int leftNum = 0;
        for (leftNum = inStart; leftNum <= inEnd; leftNum++) {
            if (preorder[preStart] == inorder[leftNum]) {
                break;
            }
        }
        leftNum = (leftNum - inStart);


        node.left = build(preorder, inorder, preStart + 1, preStart + leftNum, inStart, inStart + leftNum - 1);
        node.right = build(preorder, inorder, preStart + leftNum + 1, preEnd, inStart + leftNum + 1, inEnd);
        return node;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
