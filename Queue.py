'''
This program demonstrates queue implementation using Python list
'''
# initialize the queue
queue = []

# adding values to the queue
queue.append("Python")
queue.append("Hello")
queue.append("World!")

# display initial queue
print("Initial Queue")
print(queue)

# remove values from the queue
print("\nElements Dequeued from Queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

# display queue after removing values
print("\nQueue After Removing Elements")
print(queue)

# OUTPUT:
# Initial Queue
# ['Python', 'Hello', 'World!']

# Elements Dequeued from Queue 
# Python
# Hello
# World!

# Queue After Removing Elements
# []
