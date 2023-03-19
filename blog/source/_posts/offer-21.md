---
title: offer-21
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2022-12-28 14:16:44
---

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。



**示例：**

```
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
```



**提示：**

1. `0 <= nums.length <= 50000`
2. `0 <= nums[i] <= 10000`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int[] exchange(int[] nums) {
        if (nums == null || nums.length == 0) {
            return nums;
        }

        int start = 0, end = nums.length - 1;

        while (start < end) {
            boolean doSwap = nums[start] % 2 == 0 && nums[end] % 2 == 1;
            if (doSwap) {
                int temp = nums[start];
                nums[start] = nums[end];
                nums[end] = temp;
                start++;
                end--;
            } else {
                if (nums[start] % 2 == 1) {
                    start++;
                }
                if (nums[end] % 2 == 0) {
                    end--;
                }
            }
        }

        return nums;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
