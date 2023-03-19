---
title: offer-35
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-18 11:24:51
---

请实现 `copyRandomList` 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 `next` 指针指向下一个节点，还有一个 `random` 指针指向链表中的任意节点或者 `null`。



**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e1.png)

```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**示例 2：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e2.png)

```
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```

**示例 3：**

**![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e3.png)**

```
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
```

**示例 4：**

```
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
```



**提示：**

- `-10000 <= Node.val <= 10000`
- `Node.random` 为空（null）或指向链表中的节点。
- 节点数目不超过 1000 。

```java

//leetcode submit region begin(Prohibit modification and deletion)
/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/
class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return head;
        }
        Node newHead = new Node(head.val);


        Map<Node, Node> nodeMap = new HashMap<>();
        nodeMap.put(head, newHead);
        Node temp = head.next;
        Node last = newHead;
        while (temp != null) {
            Node tempCopy = new Node(temp.val);
            nodeMap.put(temp, tempCopy);
            last.next = tempCopy;
            last = tempCopy;
            temp = temp.next;
        }
        last.next = null;

        temp = head;
        while (temp != null) {
            Node tempCopy = nodeMap.get(temp);
            if (temp.random == null) {
                tempCopy.random = null;
            } else {
                Node target = nodeMap.get(temp.random);
                tempCopy.random = target;
            }
            temp = temp.next;
        }

        return newHead;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
