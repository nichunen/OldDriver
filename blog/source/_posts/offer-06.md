---
title: offer-06
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2022-12-02 11:33:54
---

```java
/**
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。 

 

 示例 1： 

 输入：head = [1,3,2]
输出：[2,3,1] 

 

 限制： 

 0 <= 链表长度 <= 10000 
 Related Topics栈 | 递归 | 链表 | 双指针 

 👍 354, 👎 0 

*/
//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] reversePrint(ListNode head) {
        int len = 0;
        ListNode node = head;
        while (node != null) {
            len++;
            node = node.next;
        }

        int[] result = new int[len];
        doReverse(head, result, len - 1);
        return result;
    }

    private void doReverse(ListNode node, int[] result, int curIndex) {
        if (node == null) {
            return;
        }

        doReverse(node.next, result, curIndex - 1);
        result[curIndex] = node.val;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
