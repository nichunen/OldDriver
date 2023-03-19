---
title: offer-03
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2022-11-24 23:38:00
---

```java
/**
找出数组中重复的数字。 

 
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出
数组中任意一个重复的数字。 

 示例 1： 

 输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
 

 

 限制： 

 2 <= n <= 100000 
 Related Topics数组 | 哈希表 | 排序 

 👍 1007, 👎 0 

*/
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int findRepeatNumber(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int targetIndex = nums[i] < 0 ? -(nums[i] + 1) : nums[i];

            if (nums[targetIndex] < 0) {
                return targetIndex;
            }

            nums[targetIndex] = -(nums[targetIndex] + 1);
        }

        return -1;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
