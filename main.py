arr = [1,2,5,5,9,8,4,88,55,6,6,5,3,]
arr1 = []


for el in arr:
    if arr.count(el) > 2:
        arr1.append(el)


print(arr)
print(arr1)
