triplets to make sum

my answer: make a map of numbers to indices. do a quadratic loop over pairs, look for inverse of pair in map, making sure to not duplicate indices

they're only considering negative numbers for i. I guess that makes sense. they're coming at either end

I feel like my solution would have also worked, but

```
def threeSum(self, nums: List[int]) -> List[List[int]]:
  nums.sort()
  res = []
  for i in range(len(nums)):
    if nums[i] > 0 or i > 0 and nums[i] == nums[i-1]: continue
    l, r = i+1, len(nums)-1
    while l < r:
      total = nums[i] + nums[l] + nums[r]
      if total == 0:
        res.append([nums[i], nums[l], nums[r]])
        l, r = l+1, r-1
        while l < len(nums) -1 and nums[l] == nums[l-1]:
          l += 1
      elif total > 0:
        r -= 1
      else:
        l += 1
  return res
```

---

akuna oa

Given an array a of length n, find the maximum possible sum from a subarray of length at most k.

use two pointers.

make a prefix sum array
make left pointer, "scrunch it along", keeping track of running "window" sum as you go

I think that would work, but they're using a monotonic queue? don't know what that is

---

0-1 Knapsack

bottom up dynamic programming, one dimension is weight, other is possible items

---


# interview prep

logarithms "find the power". put in a number, find out what power the *implicit* base (almost always 2 in computer science because of binary) was raised to
or we can say it tells us how many times we can divide a number by the base before we get to 1
how many "exponential layers" away is it from 1

permutations (order matters, no replacement), is `n!`

number of subsets is a decision tree of binary choices (is this element in the set or not)
so it's `2 ^ n` subsets

sum of *any* arithmetic sequence is

```
(first_element + last_element) * number_of_element / 2
```

an arithmetic sequence is any sequence where the difference between items is *a constant* (1, 2, etc)

a geometric sequence is any sequence where the *ratio* between differences is a constant
basically, arithmetic *adds* by a constant whereas geometric *multiplies* by a constant

sum of a geometric series is

```
first_element * (1 - ratio^number_of_elements) / (1 - ratio)
```

the modulo operation is distributive???


```
(a + b) MOD c = ((a MOD c) + (b MOD c)) MOD c
```

stacks are lifo
queues are fifo
deques (pronounced deck) are double ended queues, supporting back/front versions of push/pop/peek
`from collections import deque`

```
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.children = []

class LinkedListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next


import math
positive_inf = math.inf
negative_inf = -math.inf
```


insertion sort is the dumbest/simplest one. for each element, you just swap that element downward with its previous neighbor while it's smaller than its previous neighbor

selection sort is also simple, we iterate through the indexes, and for each find the min in the *unsorted* portion





# two pointers methods

fixed size window, obvious since just basically doing some sort of a convolution or close

changing window, any structure you can commutatively add/remove things from as you slide can be used to figure out which section of an iterable fits some condition
when finding maximum sized window, slow pointer is main, fast goes out as far as possible while condition continues to hold, max check done there?
when finding minimum sized window, fast pointer is main, slow is pulled in while condition continues to hold, min check is done on each iteration







Common bit manipulation operations
Typically, these problems use a recursive function as well in order to do dp. Below is some pseudocode to outline this idea. Here are some useful operations to keep in mind:

(1 << i) -> simply 2 to the power of i, or an integer where the only bit that is 1 is the ith bit.

(bitmask & (1 << i)) -> this operation checks if the ith bit in the bitmask is set to 1 or not

(bitmask ^ (1 << i)) -> this operation toggles the ith bit in the bitmask to 1 if it was 0 or to 0 if it was 1.

(bitmask | (1 << i)) -> this operation unconditionally turns on the ith bit in the bitmask.




a trie is a tree where each *item* in a "prefix"-able sequence is the node. so if the words "hi" and "hit" were both in the trie, then "h", "i", and "t" would be in, and "h" and "i" would have a frequency of 2 and "t" only of 1


in this world LRU (least recently used) caches are implemented with a doubly-linked list, where the "highest priority" items are the ones closer to the head of the list. so removing old items just means deleting from the end



priority heaps store values with the smallest (or largest if that's how it's implemented) value at the front, with simple swaps promoting things
they can insert new things in `log(n)` time, and get the min in constant time





a monotonic stack only allows you to push things if the items on the stack change monotonically. this can be useful when doing things related to finding the "next larger" or things like that

