---
title: offer2-9
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-03-15 10:53:51
---

给定一个正整数数组 `nums`和整数 `k` ，请找出该数组内乘积小于 `k` 的连续的子数组的个数。



**示例 1:**

```
输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8 个乘积小于 100 的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
```

**示例 2:**

```
输入: nums = [1,2,3], k = 0
输出: 0
```



**提示:**

- `1 <= nums.length <= 3 * 104`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 106`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int start = 0;
        int end = 0;
        int result = 0;
        int product = 1;

        while (end < nums.length) {
            product *= nums[end];

            while (start <= end && product >= k) {
                product /= nums[start];
                start++;
            }

            end++;
            result += (end - start);
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```