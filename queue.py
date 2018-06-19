""" We do not want to implement queues using list in Python,
    since popping elements from the left of the list (necessary
    for the queue to work) requires moving all other elements
    over to the left, which is an O(n) operation
"""
from collections import deque

q = deque(["a", "b", "c"])
q.append("d")
q.popleft()
assert q.popleft() == "b"

# We can also create a deque with some max length. If we add more
# elements than the max length of the deque, the deque will automatically
# pop older elements, allowing us to work with only the most recent
# elements added to the deque

max_q = deque(["a", "b", "c"], 3)
max_q.append("d")
assert max_q.popleft() == "b"
