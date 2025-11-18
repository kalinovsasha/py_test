def stray(arr:list):
    if arr.__len__() > 2:
        for i in arr:
            if arr.count(i) == 1:
                return i
print(stray([1,2,2,2]))