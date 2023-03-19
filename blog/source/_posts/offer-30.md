---
title: offer-30
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-10 11:01:04
---

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。



**示例:**

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
```



**提示：**

1. 各函数的调用总次数不超过 20000 次



```java

//leetcode submit region begin(Prohibit modification and deletion)
class MinStack {

    /** initialize your data structure here. */
    private List<Integer> dataList;
    private int minIndex;

    public MinStack() {
        this.dataList = new ArrayList<>();
        this.minIndex = -1;
    }

    public void push(int x) {
        this.dataList.add(x);

        if (this.minIndex == -1) {
            this.minIndex = 0;
        } else if (x < this.dataList.get(minIndex)) {
            this.minIndex = this.dataList.size() - 1;
        }
    }

    public void pop() {
        if (this.dataList.size() > 0) {
            this.dataList.remove(this.dataList.size() - 1);

            if (this.dataList.size() == this.minIndex) {
                if (this.dataList.size() == 0) {
                    this.minIndex = -1;
                } else {
                    int minV = Integer.MAX_VALUE;

                    for (int i = 0; i < this.dataList.size(); i++) {
                        if (this.dataList.get(i) <= minV) {a
                            minV = this.dataList.get(i);
                            this.minIndex = i;
                        }
                    }
                }
            }
        }
    }

    public int top() {
        if (this.dataList.size() > 0) {
            return this.dataList.get(this.dataList.size() - 1);
        } else {
            return  Integer.MAX_VALUE;
        }
    }

    public int min() {
        if (this.minIndex != -1) {
            return this.dataList.get(this.minIndex);
        } else {
            return  Integer.MAX_VALUE;
        }
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.min();
 */
//leetcode submit region end(Prohibit modification and deletion)
```
