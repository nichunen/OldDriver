---
title: offer-49
author: 倪春恩
top: false
hide: false
cover: true
toc: false
categories: leetcode
tags:
  - leetcode
date: 2023-02-07 11:06:08
---

我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。



**示例:**

```
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
```

**说明:**

1. `1` 是丑数。
2. `n` **不超过**1690。

```java

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int nthUglyNumber(int n) {
        int[] elems = {2, 3, 5};

        Queue<Long> pq = new PriorityQueue<>(new Comparator<Long>(){
            @Override
            public int compare(Long o1, Long o2) {
                return o1.compareTo(o2);
            }
        });

        Set<Long> nSet = new HashSet<>();

        pq.add(1L);
        nSet.add(1L);
        int ugly = 0;

        for (int i = 0; i < n; i++) {
            ugly = (pq.poll()).intValue();

            for (int elem : elems) {
                long v = (long)(ugly) * elem;

                if (!nSet.contains(v)) {
                    pq.add(v);
                    nSet.add(v);
                }
            }
        }

        return ugly;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
```
