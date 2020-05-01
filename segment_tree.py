import numpy as np
import math
"""
Rudimentary implementation of rangequery!
"""
class segment_tree:
    def __init__(self, arr):
        self.arr = arr
        layers = math.ceil(math.log2(len(arr)))
        self.tree = np.full(shape=((2**layers) * 2 - 1, ), fill_value=np.PINF)
        self.constructTree(arr, low=0, high=len(arr)-1, pos=0)

    def constructTree(self, arr, low, high, pos):
        if low==high:
            self.tree[pos] = arr[low]
        else:
            mid = (low + high)//2
            # left child
            self.constructTree(arr, low, mid, 2*pos+1)
            # right child
            self.constructTree(arr, mid + 1, high, 2*pos+2)
            self.tree[pos] = min(self.tree[2*pos+1], self.tree[2*pos+2])

    def rangeMinQuery(self, qlow, qhigh, low, high, pos):
        # print(qlow, qhigh, low, high, pos)
        if qlow <= low and qhigh >= high:
            return self.tree[pos] # total overlap
        elif qlow > high or qhigh < low:
            return np.PINF # no overlap
        mid = (low + high)//2
        return min(self.rangeMinQuery(qlow, qhigh, low, mid, 2*pos+1),
                   self.rangeMinQuery(qlow, qhigh, mid+1, high, 2*pos+2))

    def search(self, q_low, q_high):
        assert q_low <= q_high, "range is set wrong!"
        return self.rangeMinQuery(qlow=q_low, qhigh=q_high,
                                  low=0, high=len(self.arr)-1,
                                  pos=0)


class max_segment_tree:
    def __init__(self, arr):
        self.arr = arr
        layers = math.ceil(math.log2(len(arr)))
        self.tree = np.full(shape=((2**layers) * 2 - 1, ), fill_value=np.NINF)
        self.constructTree(arr, low=0, high=len(arr)-1, pos=0)

    def constructTree(self, arr, low, high, pos):
        if low==high:
            self.tree[pos] = arr[low]
        else:
            mid = (low + high)//2
            # left child
            self.constructTree(arr, low, mid, 2*pos+1)
            # right child
            self.constructTree(arr, mid + 1, high, 2*pos+2)
            self.tree[pos] = max(self.tree[2*pos+1], self.tree[2*pos+2])

    def rangeMinQuery(self, qlow, qhigh, low, high, pos):
        # print(qlow, qhigh, low, high, pos)
        if qlow <= low and qhigh >= high:
            return self.tree[pos] # total overlap
        elif qlow > high or qhigh < low:
            return np.NINF # no overlap
        mid = (low + high)//2
        return max(self.rangeMinQuery(qlow, qhigh, low, mid, 2*pos+1),
                   self.rangeMinQuery(qlow, qhigh, mid+1, high, 2*pos+2))

    def search(self, q_low, q_high):
        assert q_low <= q_high, "range is set wrong!"
        return self.rangeMinQuery(qlow=q_low, qhigh=q_high,
                                  low=0, high=len(self.arr)-1,
                                  pos=0)



if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    segtree = max_segment_tree(nums)
    for i in range(len(nums)-3 + 1):
        print(segtree.search(i, i+2))


