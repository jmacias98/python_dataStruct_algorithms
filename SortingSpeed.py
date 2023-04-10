'''
This program creates lists of random integer numbers and uses 3 sorting
algorithms to determine which performs the fastest. Results are also
displayed using a graph.
'''
import numpy as np
import matplotlib.pyplot as plt
import time
import random
from collections import deque

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.

    # Last i elements are already in place
        for j in range(0, n-i-1):

    # traverse the array from 0 to n-i-1
    # Swap if the element found is greater
    # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def shellSort(arr):
    n = len(arr)
    gap = n // 2 
    while gap > 0: 
        for i in range(gap,n): 
            temp = arr[i] 
            j = i 
            while  j >= gap and arr[j-gap] > temp: 
                arr[j] = arr[j-gap] 
                j = j - gap 
            arr[j] = temp 
        gap = gap // 2

def swap (A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
def partition(a, start, end):
 
    # Pick the rightmost element as a pivot from the list
    pivot = a[end]
 
    # elements less than the pivot will go to the left of `pIndex`
    # elements more than the pivot will go to the right of `pIndex`
    # equal elements can go either way
    pIndex = start
 
    # each time we find an element less than or equal to the pivot,
    # `pIndex` is incremented, and that element would be placed
    # before the pivot.
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex = pIndex + 1
 
    # swap `pIndex` with pivot
    swap(a, pIndex, end)
 
    # return `pIndex` (index of the pivot element)
    return pIndex
 
# Iterative Quicksort routine
def quickSort(a):
 
    # create a stack for storing sublist start and end index
    stack = deque()
 
    # get the starting and ending index of a given list
    start = 0
    end = len(a) - 1
 
    # push the start and end index of the array into the stack
    stack.append((start, end))
 
    # loop till stack is empty
    while stack:
 
        # remove top pair from the list and get sublist starting
        # and ending indices
        start, end = stack.pop()
 
        # rearrange elements across pivot
        pivot = partition(a, start, end)
 
        # push sublist indices containing elements that are
        # less than the current pivot to stack
        if pivot - 1 > start:
            stack.append((start, pivot - 1))
 
        # push sublist indices containing elements that are
        # more than the current pivot to stack
        if pivot + 1 < end:
            stack.append((pivot + 1, end))

array10 = []
array20 = []
array30 = []
array40 = []
array60 = []

for i in range(0,10000): # create 10000 random numbers
    x = random.randint(1,10000) # ranges 1 to 10000
    array10.append(x)
start_time = time.time() # start the clock
bubbleSort(array10) #  put your sorting method
stop_time = time.time() - start_time
print("Bubble Sort 10000: %s seconds" % stop_time)
for i in range(0,10000): # create 10000 random numbers
    x = random.randint(1,10000) # ranges 1 to 10000
    array10.append(x)
start_time2 = time.time() # start the clock
shellSort(array10)
stop_time2 = time.time() - start_time2
print("Shell Sort 10000: %s seconds" % stop_time2)
for i in range(0,10000): # create 10000 random numbers
    x = random.randint(1,10000) # ranges 1 to 10000
    array10.append(x)
start_time3 = time.time() # start the clock
quickSort(array10)
stop_time3 = time.time() - start_time3
print("Quick Sort 10000: %s seconds" % stop_time3)

for i in range(0,20000): # create 10000 random numbers
    x = random.randint(1,20000) # ranges 1 to 10000
    array20.append(x)
start_time4 = time.time() # start the clock
bubbleSort(array20) #  put your sorting method
stop_time4 = time.time() - start_time4
print("Bubble Sort 20000: %s seconds" % stop_time4)
for i in range(0,20000): # create 10000 random numbers
    x = random.randint(1,20000) # ranges 1 to 10000
    array20.append(x)
start_time5 = time.time() # start the clock
shellSort(array20)
stop_time5 = time.time() - start_time5
print("Shell Sort 20000: %s seconds" % stop_time5)
for i in range(0,20000): # create 10000 random numbers
    x = random.randint(1,20000) # ranges 1 to 10000
    array20.append(x)
start_time6 = time.time() # start the clock
quickSort(array20)
stop_time6 = time.time() - start_time6
print("Quick Sort 20000: %s seconds" % stop_time6)

for i in range(0,30000): # create 10000 random numbers
    x = random.randint(1,30000) # ranges 1 to 10000
    array30.append(x)
start_time7 = time.time() # start the clock
bubbleSort(array30) #  put your sorting method
stop_time7 = time.time() - start_time7
print("Bubble Sort 30000: %s seconds" % stop_time7)
for i in range(0,30000): # create 10000 random numbers
    x = random.randint(1,30000) # ranges 1 to 10000
    array30.append(x)
start_time8 = time.time() # start the clock
shellSort(array30)
stop_time8 = time.time() - start_time8
print("Shell Sort 30000: %s seconds" % stop_time8)
for i in range(0,30000): # create 10000 random numbers
    x = random.randint(1,30000) # ranges 1 to 10000
    array30.append(x)
start_time9 = time.time() # start the clock
quickSort(array30)
stop_time9 = time.time() - start_time9
print("Quick Sort 30000: %s seconds" % stop_time9)

for i in range(0,40000): # create 10000 random numbers
    x = random.randint(1,40000) # ranges 1 to 10000
    array40.append(x)
start_time10 = time.time() # start the clock
bubbleSort(array40) #  put your sorting method
stop_time10 = time.time() - start_time10
print("Bubble Sort 40000: %s seconds" % stop_time10)
for i in range(0,40000): # create 10000 random numbers
    x = random.randint(1,40000) # ranges 1 to 10000
    array40.append(x)
start_time11 = time.time() # start the clock
shellSort(array40)
stop_time11 = time.time() - start_time11
print("Shell Sort 40000: %s seconds" % stop_time11)
for i in range(0,40000): # create 10000 random numbers
    x = random.randint(1,40000) # ranges 1 to 10000
    array40.append(x)
start_time12 = time.time() # start the clock
quickSort(array40)
stop_time12 = time.time() - start_time12
print("Quick Sort 40000: %s seconds" % stop_time12)

for i in range(0,60000): # create 10000 random numbers
    x = random.randint(1,60000) # ranges 1 to 10000
    array60.append(x)
start_time13 = time.time() # start the clock
bubbleSort(array60) #  put your sorting method
stop_time13 = time.time() - start_time13
print("Bubble Sort 60000: %s seconds" % stop_time13)
for i in range(0,60000): # create 10000 random numbers
    x = random.randint(1,60000) # ranges 1 to 10000
    array60.append(x)
start_time14 = time.time() # start the clock
shellSort(array60)
stop_time14 = time.time() - start_time14
print("Shell Sort 60000: %s seconds" % stop_time14)
for i in range(0,60000): # create 10000 random numbers
    x = random.randint(1,60000) # ranges 1 to 10000
    array60.append(x)
start_time15 = time.time() # start the clock
quickSort(array60)
stop_time15 = time.time() - start_time15
print("Quick Sort 60000: %s seconds" % stop_time15)

barWidth = 0.25

# set heights of bars
bars1 = [stop_time, stop_time4, stop_time7, stop_time10, stop_time13]
bars2 = [stop_time2, stop_time5, stop_time8, stop_time11, stop_time14]
bars3 = [stop_time3, stop_time6, stop_time9, stop_time12, stop_time15]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='Bubble Sort')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='Shell Sort')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='Quick Sort')
 
# Add xticks on the middle of the group bars
plt.xlabel('Number of Elements in Array', fontweight='bold')
plt.ylabel("Seconds", fontweight = "bold")
plt.title("Sorting Algorithm Performance in Seconds")
plt.xticks([r + barWidth for r in range(len(bars1))], ['10000', '20000', '30000', '40000', '60000'])
 
# Create legend & Show graphic
plt.legend()
plt.show()
'''
CONCLUSION: On average, as elements in the array increase, seconds to sort
increases as well. However, bubble sort is the slowest performing by a long shot
while shell sort is slightly faster than quick sort. You have to
zoom in very close to see shell and quick sort results on graph.

RESULTS:
Bubble Sort 10000: 6.3130316734313965 seconds
Shell Sort 10000: 0.08549714088439941 seconds
Quick Sort 10000: 0.10882949829101562 seconds

Bubble Sort 20000: 26.038379669189453 seconds
Shell Sort 20000: 0.19202899932861328 seconds
Quick Sort 20000: 0.24004530906677246 seconds

Bubble Sort 30000: 130.31631731987 seconds
Shell Sort 30000: 0.7143654823303223 seconds
Quick Sort 30000: 1.0855679512023926 seconds

Bubble Sort 40000: 162.77058792114258 seconds
Shell Sort 40000: 0.9311318397521973 seconds
Quick Sort 40000: 1.4306325912475586 seconds

Bubble Sort 60000: 326.2737946510315 seconds
Shell Sort 60000: 0.7127058506011963 seconds
Quick Sort 60000: 0.792011022567749 seconds
'''