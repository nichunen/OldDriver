---
title: offer-09
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2022-12-06 10:56:44
---

```java
/**
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能
。(若队列中没有元素，deleteHead 操作返回 -1 ) 

 

 示例 1： 

 
输入：
["CQueue","appendTail","deleteHead","deleteHead","deleteHead"]
[[],[3],[],[],[]]
输出：[null,null,3,-1,-1]
 

 示例 2： 

 
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
 

 提示： 

 
 1 <= values <= 10000 
 最多会对 appendTail、deleteHead 进行 10000 次调用 
 
 Related Topics栈 | 设计 | 队列 

 👍 633, 👎 0 

*/
//leetcode submit region begin(Prohibit modification and deletion)
class CQueue {

    private Stack<Integer> stackAppend;
    private Stack<Integer> stackDelete;

    public CQueue() {
        this.stackAppend = new Stack<>();
        this.stackDelete = new Stack<>();
    }

    public void appendTail(int value) {
        this.stackAppend.push(value);
    }

    public int deleteHead() {
        if (this.stackAppend.isEmpty() && this.stackDelete.isEmpty()) {
            return -1;
        }

        if (!stackDelete.isEmpty()) {
            return stackDelete.pop();
        }

        while (!stackAppend.isEmpty()) {
            stackDelete.push(stackAppend.pop());
        }
        return stackDelete.pop();
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue obj = new CQueue();
 * obj.appendTail(value);
 * int param_2 = obj.deleteHead();
 */
//leetcode submit region end(Prohibit modification and deletion)
```