# Approach: Add a current value var to keep curr values and self.iter to store iterator
# TC: O(1)
# SC: O(1)
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator  # Store iterator in instance var
        self.curr = self.iter.next() # init current with first value

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.curr # peek means just returns the val at current
        

    def next(self):
        """
        :rtype: int
        """
        tmp = self.curr # before sending next value, store it in tmp
        self.curr = self.iter.next() # update curr with next value
        return tmp # send tmp as next value

    def hasNext(self):
        """
        :rtype: bool
        """
        # when there is no next item default is -100000, if that is the value, then
        # we no longer have next value remaining
        return self.curr is not -100000
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].