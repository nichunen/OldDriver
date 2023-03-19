---
title: offer2-10
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-03-16 11:03:22
---

给定一个整数数组和一个整数 `k` **，**请找到该数组中和为 `k` 的连续子数组的个数。



**示例 1：**

```
输入:nums = [1,1,1], k = 2
输出: 2
解释: 此题 [1,1] 与 [1,1] 为两种不同的情况
```

**示例 2：**

```
输入:nums = [1,2,3], k = 3
输出: 2
```



**提示:**

- `1 <= nums.length <= 2 * 104`
- `-1000 <= nums[i] <= 1000`
- `-107 <= k <= 107`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int subarraySum(int[] nums, int k) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int[] sums = new int[nums.length];
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                sums[i] = nums[i];
            } else {
                sums[i] = sums[i - 1] + nums[i];
            }
        }

        int result = 0;

        for (int i = 0; i < nums.length; i++) {
            if (sums[i] == k) {
                result++;
            }

            for (int j = 0; j < i; j++) {
                if (sums[i] - sums[j] == k) {
                    result++;
                }
            }
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
