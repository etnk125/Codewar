def dirReduc(arr):
    dict = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    ans = []
    for i in arr:
        if len(ans) > 0:
            if dict[i] == ans[-1]:
                ans.pop()
                continue
        ans.append(i)
    return ans
"""
def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3

    apply with recursive replace
"""