---
title: offer-31
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-11 15:28:15
---

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。



**示例 1：**

```
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

**示例 2：**

```
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
```



**提示：**

1. `0 <= pushed.length == popped.length <= 1000`
2. `0 <= pushed[i], popped[i] < 1000`
3. `pushed` 是 `popped` 的排列。



```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        if ((pushed == null  || pushed.length == 0) && (popped == null || popped.length == 0)) {
            return true;
        }

        if (pushed == null || pushed.length == 0 || popped == null || popped.length == 0 || pushed.length != popped.length) {
            return false;
        }
        Stack<Integer> mockStack = new Stack<>();

        int pushIndex = 0, popIndex = 0;

        while (pushIndex < pushed.length || popIndex < popped.length) {
            while (!mockStack.isEmpty() && mockStack.peek() == popped[popIndex]) {
                mockStack.pop();
                popIndex++;
            }


            if (pushIndex == pushed.length) {
                return mockStack.isEmpty();
            } else {
                mockStack.push(pushed[pushIndex]);
                pushIndex++;
            }

        }

        return false;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
