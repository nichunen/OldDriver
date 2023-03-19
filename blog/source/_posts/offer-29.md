---
title: offer-29
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-09 17:09:07
---

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。



**示例 1：**

```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
```

**示例 2：**

```
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
```



**限制：**

- `0 <= matrix.length <= 100`
- `0 <= matrix[i].length <= 100`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int[] spiralOrder(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0) {
            return new int[0];
        }

        int[][] next = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        int curIndex = 0;
        Set<String> visitedLocSet = new HashSet<>();
        int[] result = new int[matrix.length * matrix[0].length];
        int curR = 0, curC = -1;

        while (visitedLocSet.size() < result.length) {
            curR = curR + next[curIndex][0];
            curC = curC + next[curIndex][1];
            String locStr = "" + curR + "-" + curC;

            if (curR < 0 || curC < 0 || curR >= matrix.length || curC >= matrix[0].length || visitedLocSet.contains(locStr)) {
                curR = curR - next[curIndex][0];
                curC = curC - next[curIndex][1];
                curIndex++;

                if (curIndex == 4) {
                    curIndex = 0;
                }

                continue;
            }


            result[visitedLocSet.size()] = matrix[curR][curC];
            visitedLocSet.add(locStr);
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
