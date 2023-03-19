---
title: offer-42
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-31 11:31:36
---

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。



**示例1:**

```
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```



**提示：**

- `1 <= arr.length <= 10^5`
- `-100 <= arr[i] <= 100`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int maxSubArray(int[] nums) {
        int maxV = Integer.MIN_VALUE;

        int curSum = 0;

        for (int num : nums) {
            curSum += num;

            if (curSum > maxV) {
                maxV = curSum;
            }

            if (curSum < 0) {
                if (num > 0) {
                    curSum = num;
                } else {
                    curSum = 0;
                }
            }
        }

        return maxV;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
