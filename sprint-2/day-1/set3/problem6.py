# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"


# queue 

from collections import deque;

queue = deque([1,2,3,4])

queue.append(5);


print(queue);

front = queue.popleft();
print(front)


#Stack

from queue import LifoQueue;

stack = LifoQueue()

stack.put(1);

stack.put(2);

print(stack);

top = stack.get();

print(top);

