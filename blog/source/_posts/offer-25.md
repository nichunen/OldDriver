---
title: offer-25
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-03 21:35:15
---

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

**示例1：**

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

**限制：**

```
0 <= 链表长度 <= 1000
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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head, curNode;

        if (l1 == null && l2 == null) {
            return null;
        }

        if (l1 == null) {
            head = l2;
            curNode = l2;
            l2 = l2.next;
        } else if (l2 == null) {
            head = l1;
            curNode = l1;
            l1 = l1.next;
        } else {
            if (l1.val < l2.val) {
                head = l1;
                curNode = l1;
                l1 = l1.next;
            } else {
                head = l2;
                curNode = l2;
                l2 = l2.next;
            }
        }

        while (l1 != null || l2 != null) {
            if (l1 == null || (l2 != null && l1.val > l2.val)) {
                curNode.next = l2;
                curNode = l2;
                l2 = l2.next;
            } else {
                curNode.next = l1;
                curNode = l1;
                l1 = l1.next;
            }
        }

        return head;

    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
