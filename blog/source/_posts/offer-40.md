---
title: offer-40
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-01-29 11:14:32
---

输入整数数组 `arr` ，找出其中最小的 `k` 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。



**示例 1：**

```
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
```

**示例 2：**

```
输入：arr = [0,1,2,1], k = 1
输出：[0]
```



**限制：**

- `0 <= k <= arr.length <= 10000`
- `0 <= arr[i] <= 10000`



```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int[] getLeastNumbers(int[] arr, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return -o1.compareTo(o2);
            }
        });

        for (int val : arr) {
            pq.add(val);

            if (pq.size() > k) {
                pq.poll();
            }
        }

        if (pq.size() > 0) {
            int[] result = new int[pq.size()];
            int pqSize = pq.size();
            for (int i = 0; i < pqSize; i++) {
                result[i] = pq.poll();
            }
            return result;
        } else {
            return new int[0];
        }
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
