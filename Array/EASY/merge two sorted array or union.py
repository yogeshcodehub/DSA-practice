def merge_sorted_array(arr1,arr2):
    i=0
    j=0
    nums=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            if not nums or arr1[i]!=nums[-1]:
                nums.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j] :
            if not  nums or arr2[j]!=nums[-1]:
                nums.append(arr2[j])
            j+=1
        else:
            if not nums or arr1[i]!=nums[-1]:
                nums.append(arr1[i])
            i+=1
            j+=1
    while i<len(arr1):
        if arr1[i]!=nums[-1] or not nums:
            nums.append(arr1[i])
        i+=1
    while j<len(arr2):
        if not nums or arr2[j]!=nums[-1]:
            nums.append(arr2[j])
        j+=1
    return nums

arr1=[2,4,6,8,10]
arr2=[1,3,5,7,9]
print(merge_sorted_array(arr1,arr2))