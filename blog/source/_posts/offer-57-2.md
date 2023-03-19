---
title: offer-57-2
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-19 22:12:27
---

输入一个正整数 `target` ，输出所有和为 `target` 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。



**示例 1：**

```
输入：target = 9
输出：[[2,3,4],[4,5]]
```

**示例 2：**

```
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
```



**限制：**

- `1 <= target <= 10^5`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int[][] findContinuousSequence(int target) {
        if (target == 1 || target == 2) {
            return new int[0][];
        }
        List<List<Integer>> resultList = new ArrayList<>();
        int curSum = 1;

        int start = 1, end = 1;

        while (start <= target / 2) {
            if (curSum == target) {
                List<Integer> oneSe = new ArrayList<>();
                oneSe.add(start);
                oneSe.add(end);
                resultList.add(oneSe);
                curSum -= start;
                start++;
            } else if (curSum < target) {
                end++;
                curSum += end;
            } else {
                curSum -= start;
                start++;
            }
        }

        if (resultList.size() == 0) {
            return new int[0][];
        }

        int[][] result = new int[resultList.size()][];
        int index = 0;

        for (List<Integer> oneSe : resultList) {
            int[] oneArr = new int[oneSe.get(1) - oneSe.get(0) + 1];
            for (int i = oneSe.get(0); i <= oneSe.get(1); i++) {
                oneArr[i - oneSe.get(0)] = i;
            }
            result[index++] = oneArr;
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
