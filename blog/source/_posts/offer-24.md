---
title: offer-24
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2022-12-30 11:35:37
---

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。



**示例:**

```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```



**限制：**

```
0 <= 节点个数 <= 5000
```



```java

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
    public ListNode reverseList(ListNode head) {
        return reverseFunc(head);
    }

    private ListNode reverseFunc(ListNode node) {
        if (node == null || node.next == null) {
            return node;
        }

        ListNode nextNode = node.next;
        node.next = null;
        ListNode newHead = reverseFunc(nextNode);
        nextNode.next = node;
        return newHead;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
