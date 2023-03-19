---
title: offer-56-2
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-16 11:09:31
---

在一个数组 `nums` 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。



**示例 1：**

```
输入：nums = [3,4,3,3]
输出：4
```

**示例 2：**

```
输入：nums = [9,1,7,9,7,9,7]
输出：1
```



**限制：**

- `1 <= nums.length <= 10000`
- `1 <= nums[i] < 2^31`

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int singleNumber(int[] nums) {
        int[] bitNum = new int[63];


        for (int num : nums) {
            int i = 0;

            while (num > 0) {
                bitNum[i] += num % 2;
                i++;
                num = num >> 1;
            }
        }

        int result = 0;

        for (int i = 62; i >= 0; i--) {
            result = result << 1;
            if (bitNum[i] % 3 == 1) {
                result += 1;
            }
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
