---
title: offer-56-1
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-15 11:15:52
---

一个整型数组 `nums` 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。



**示例 1：**

```
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
```

**示例 2：**

```
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
```



**限制：**

- `2 <= nums.length <= 10000`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int[] singleNumbers(int[] nums) {
        int twoXor = 0;

        for (int num : nums) {
            twoXor ^= num;
        }

        int key = 1;

        while ((key & twoXor) == 0) {
            key = key << 1;
        }

        int numOne = 0, numTwo = 0;

        for (int num : nums) {
            if ((num & key) == 0) {
                numOne ^= num;
            } else {
                numTwo ^= num;
            }
        }

        int[] result = new int[2];
        result[0] = numOne;
        result[1] = numTwo;

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
