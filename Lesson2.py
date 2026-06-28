# SEARCHING ALGORITHMS 


def search_indx(arr : list[int], target: int) -> int:
    n : int = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i 
    return -1

def delete_element(arr:list[int], target : int) -> list[int]:
    ans : list[int] = []

    n : int = len(arr)
    for i in range(n):
        if arr[i] != target:
            ans.append(arr[i])
    return ans




arr : list[int] = [22, 33, 12, 20, 100, 101]
target : int = 100

# ex - target = 12 , index = 2
# ex - target = 20, index = 3
target_index = search_indx(arr, target)

print(delete_element(arr, target))




