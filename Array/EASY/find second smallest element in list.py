def second_smallest(arr):
    s=float('inf')
    ss=float('inf')
    for i in arr:
        if s>i:
            ss=s
            s=i
        elif ss>i and ss!=i:
            ss=i
    return ss

arr=[1,2,3,4,5]
print(second_smallest(arr))