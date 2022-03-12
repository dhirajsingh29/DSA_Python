def BinarySearch(arr, target: int, start: int, end: int) -> int:

    if start > end:
        return -1

    m = start + (end - start) // 2

    if arr[m] == target:
        return m

    if (target < arr[m]):
        return BinarySearch(arr, target, start, end=m-1)
    
    return BinarySearch(arr, target, start=m+1, end=end)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    print(BinarySearch(arr, target, 0, len(arr) - 1))