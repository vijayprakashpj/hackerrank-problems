def minimumAbsoluteDifference(arr):
    """
    Greedy algorithm: Minimum difference will be possible only between
    two adjacent numbers
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    arr.sort()
    
    result = -1
    for i in range(len(arr) - 1):
        difference = abs(arr[i] - arr[i+1])
        if result == -1 or result > difference:
            result = difference
    
    return result


if __name__ == "__main__":
    print("Enter number of items: ")
    n = int(input())

    print("Enter array items: ")
    arr = list(map(lambda x: int(x), input().split(" ")))

    print(minimumAbsoluteDifference(arr))

