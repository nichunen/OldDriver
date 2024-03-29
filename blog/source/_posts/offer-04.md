---
title: offer-04
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2022-11-29 10:52:52
---

```java
/**
在一个 n * m 的二维数组中，每一行都按照从左到右 非递减 的顺序排序，每一列都按照从上到下 非递减 的顺序排序。请完成一个高效的函数，输入这样的一个二维数
组和一个整数，判断数组中是否含有该整数。 

 

 示例: 

 现有矩阵 matrix 如下： 

 
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
 

 给定 target = 5，返回 true。 

 给定 target = 20，返回 false。 

 

 限制： 

 0 <= n <= 1000 

 0 <= m <= 1000 

 

 注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/ 
 Related Topics数组 | 二分查找 | 分治 | 矩阵 

 👍 826, 👎 0 

*/
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0) {
            return false;
        }

        int i = matrix.length - 1, j = 0;

        while (i >= 0 && j < matrix[0].length) {
            if (matrix[i][j] == target) {
                return true;
            } else if (matrix[i][j] < target) {
                j++;
            } else {
                i--;
            }
        }

        return false;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
