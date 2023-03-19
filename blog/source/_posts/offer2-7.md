---
title: offer2-7
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-03-13 11:16:49
---

给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请

你返回所有和为 `0` 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。





**示例 1：**

```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
```

**示例 2：**

```
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
```

**示例 3：**

```
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
```



**提示：**

- `3 <= nums.length <= 3000`
- `-105 <= nums[i] <= 105`

```java
import java.util.HashSet;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        Set<String> resutSet = new HashSet<>();

        if (nums == null || nums.length == 0) {
            return result;
        }

        for (int i = 0; i < nums.length; i++) {
            findByOne(result, resutSet, nums, i, -nums[i]);
        }

        return result;
    }

    void findByOne(List<List<Integer>> result, Set<String> resutSet, int[] nums, int index, int target) {
        int start = 0;
        int end = index - 1;

        while (start < end) {
            if (nums[start] + nums[end] == target) {
                String resultKey = "" + nums[start] + "_" + nums[end] + "_" + -target;
                if (resutSet.contains(resultKey)) {
                    start++;
                    continue;
                }
                resutSet.add(resultKey);
                List<Integer> oneList = new ArrayList<>();
                oneList.add(nums[start]);
                oneList.add(nums[end]);
                oneList.add(-target);
                result.add(oneList);
                start++;
            } else if (nums[start] + nums[end] < target) {
                start++;
            } else {
                end--;
            }
        }
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
