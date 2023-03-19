---
title: offer-59-1
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-22 11:09:38
---

给定一个数组 `nums` 和滑动窗口的大小 `k`，请找出所有滑动窗口里的最大值。

**示例:**

```
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```



**提示：**

你可以假设 *k* 总是有效的，在输入数组 **不为空** 的情况下，`1 ≤ k ≤ nums.length`。

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0) {
            return nums;
        }

        if (k <= 0) {
            return null;
        }

        PriorityQueue<Pair<Integer, Integer>> pq = new PriorityQueue<>(new Comparator<Pair<Integer, Integer>>() {
            @Override
            public int compare(Pair<Integer, Integer> p1, Pair<Integer, Integer> p2) {
                return -p1.getKey().compareTo(p2.getKey());
            }
        });

        for (int i = 0; i < k && i < nums.length; i++) {
            Pair<Integer, Integer> p = new Pair<>(nums[i], i);
            pq.add(p);
        }

        if (nums.length <= k) {
            int[] result = new int[1];
            result[0] = pq.poll().getKey();
            return result;
        }

        int[] result = new int[nums.length - k + 1];
        result[0] = pq.peek().getKey();

        for (int i = k; i < nums.length; i++) {
            Pair<Integer, Integer> p = new Pair<>(nums[i], i);
            pq.add(p);

            while (pq.peek().getValue() <= (i - k)) {
                pq.poll();
            }
            result[i - k + 1] = pq.peek().getKey();
        }

        return result;

    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
