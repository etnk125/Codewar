def find_uniq(arr):
    count = {}
    for i in arr:
        if i in count.keys():
            continue
        count[i] = 1
        if arr.count(i) == 1:
            return i
