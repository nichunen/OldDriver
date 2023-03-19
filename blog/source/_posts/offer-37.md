---
title: offer-37
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-20 11:25:33
---

请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

**提示：**输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 [LeetCode 序列化二叉树的格式](https://support.leetcode-cn.com/hc/kb/article/1567641/)。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。



**示例：**

![img](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)

```
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
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
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sBuilder = new StringBuilder();
        sBuilder.append("[");

        if (root == null) {
            sBuilder.append("]");
            return sBuilder.toString();
        }
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);
        sBuilder.append(root.val);

        while (!nodeQueue.isEmpty()) {
            for (int i = 0; i < nodeQueue.size(); i++) {
                TreeNode node = nodeQueue.poll();
                sBuilder.append(",");
                if (node.left == null) {
                    sBuilder.append("null");
                } else {
                    nodeQueue.add(node.left);
                    sBuilder.append(node.left.val);
                }
                sBuilder.append(",");
                if (node.right == null) {
                    sBuilder.append("null");
                } else {
                    nodeQueue.add(node.right);
                    sBuilder.append(node.right.val);
                }
            }
        }
        sBuilder.append("]");
        return sBuilder.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String realStr = data.substring(1);
        realStr = realStr.substring(0, realStr.length() - 1);

        if ("".equals(realStr)) {
            return null;
        }

        String[] nodeValues = realStr.split(",");

        TreeNode root = new TreeNode();
        int index = 0;
        root.val = Integer.valueOf(nodeValues[index++]);
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);
        while (index < nodeValues.length) {
            int layerSize = nodeQueue.size();

            for (int i = 0; i < layerSize; i++) {
                TreeNode node = nodeQueue.poll();
                String leftV = nodeValues[index++];
                String rightV = nodeValues[index++];
                if ("null".equals(leftV)) {
                    node.left = null;
                } else {
                    TreeNode leftN = new TreeNode(Integer.valueOf(leftV));
                    node.left = leftN;
                    nodeQueue.add(leftN);
                }
                if ("null".equals(rightV)) {
                    node.right = null;
                } else {
                    TreeNode rightN = new TreeNode(Integer.valueOf(rightV));
                    node.right = rightN;
                    nodeQueue.add(rightN);
                }

            }
        }

        return root;
    }
}


// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
//leetcode submit region end(Prohibit modification and deletion)
```
