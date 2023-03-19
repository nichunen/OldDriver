---
title: offer-53
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-10 11:01:09
---

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。



**示例 1:**

```
输入: [0,1,3]
输出: 2
```

**示例 2:**

```
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
```



**限制：**

```
1 <= 数组长度 <= 10000
```



```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int missingNumber(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        if (nums.length == 1) {
            return nums[0] == 0 ? 1 : 0;
        }

        int start = 0, end = nums.length - 1;

        while (start < end) {
            if (start == end) {
                return nums[start] - 1;
            }

            if (start + 1 == end) {
                if (nums[start] == start) {
                    return nums[end] == end ?  end + 1 : nums[end] - 1;
                } else {
                    return nums[start] - 1;
                }
            }

            int mid = start + (end - start) / 2;

            if (nums[mid] == mid) {
                start = mid;
            } else {
                end = mid;
            }
        }

        return 0;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
