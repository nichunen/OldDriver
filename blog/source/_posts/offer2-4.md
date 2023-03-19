---
title: offer2-4
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-03-08 11:22:54
---

给你一个整数数组 `nums` ，除某个元素仅出现 **一次** 外，其余每个元素都恰出现 **三次 。**请你找出并返回那个只出现了一次的元素。



**示例 1：**

```
输入：nums = [2,2,3,2]
输出：3
```

**示例 2：**

```
输入：nums = [0,1,0,1,0,1,100]
输出：100
```



**提示：**

- `1 <= nums.length <= 3 * 104`
- `-231 <= nums[i] <= 231 - 1`
- `nums` 中，除某个元素仅出现 **一次** 外，其余每个元素都恰出现 **三次**



**进阶：**你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？



```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int singleNumber(int[] nums) {
        int[] bitNum = new int[32];
        for (int num : nums) {
            for (int i = 0; i < 32; i++) {
                bitNum[i] += (num & 1);
                num = num >> 1;
            }
        }
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result = (result << 1) + (bitNum[31 - i] % 3);
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
