---
title: offer-47
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-05 11:25:35
---

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？



**示例 1:**

```
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
```



提示：

- `0 < grid.length <= 200`
- `0 < grid[0].length <= 200`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int maxValue(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) {
            return 0;
        }

        int[][] f = new int[grid.length][grid[0].length];

        for (int i = 0; i < grid.length; i++){
            Arrays.fill(f[i], -1);
        }

        f[0][0] = grid[0][0];

        if (grid.length == 1 && grid[0].length == 1) {
            return f[0][0];
        }

        return getValue(grid, f, grid.length - 1, grid[0].length - 1);
    }

    private int getValue(int[][] grid, int[][] f, int row, int column) {
        if (f[row][column] > -1) {
            return f[row][column];
        }

        if (row == 0) {
            f[row][column] = getValue(grid, f, row, column - 1) + grid[row][column];
        } else if (column == 0) {
            f[row][column] = getValue(grid, f, row - 1, column) + grid[row][column];
        } else {
            f[row][column] = Math.max(getValue(grid, f, row - 1, column), getValue(grid, f, row, column - 1)) + grid[row][column];
        }

        return f[row][column];
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
