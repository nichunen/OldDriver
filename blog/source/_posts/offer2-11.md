---
title: offer2-11
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-03-17 11:01:58
---

给定一个二进制数组 `nums` , 找到含有相同数量的 `0` 和 `1` 的最长连续子数组，并返回该子数组的长度。



**示例 1：**

```
输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
```

**示例 2：**

```
输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。
```



**提示：**

- `1 <= nums.length <= 105`
- `nums[i]` 不是 `0` 就是 `1`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int findMaxLength(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int[] ones = new int[nums.length + 1];
        int result = 0;

        for (int i = 1; i <= nums.length; i++) {
            if (nums[i - 1] == 1) {
                ones[i] = ones[i - 1] + 1;
            } else {
                ones[i] = ones[i - 1];
            }
        }
        for (int i = nums.length; i > 0; i--) {
            if (i <= result) {
                break;
            }
            for (int j = i % 2 == 1 ? 1 : 0; j < i; j+=2) {
                if ((i - j) <= result) {
                    break;
                }
                if ((i - j) / 2 == ones[i] - ones[j] && (i - j) > result) {
                    result = i - j;
                    break;
                }
            }
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
