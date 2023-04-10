# all values must be sorted for binary search

 # searching for "9"
pos = -1

def search(list,n): # function that searches list
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l+u)//2 # integer division //

        if list[mid] == n:
            globals()["pos"] = mid
            return True
        else:
            if list[mid] < n:
                l = mid # if not found do mid + 1
            else:
                u = mid # if not found mid -1
    return False


list = [4,7,8,12,45,99]
n = 45

if search(list,n):
    print("Found at index", pos)
else:
    print("Not Found")

# Found at index 4





