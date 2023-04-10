# searching for "9"
pos = -1

def search(list,n): # function that searches list
    i = 0
    while i < len(list): # go through list from first to last
        if list[i] == n:
            globals()["pos"] = i # using globals because "pos" is local/ found out of function
            return True
        i += 1
    return False

list = [5,8,4,6,9,2]
n = 9

if search(list,n):
    print("Found at index", pos)
else:
    print("Not Found")

# 9 = Found
# 10 = Not Found

# Found at index 4





