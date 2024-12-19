def two_pointers(arr: list[int]):
    """
    Two Pointers is a technique to solve problems by iterating over the array with two pointers.
    The two pointers can be at the same end or at different ends of the array.
    This technique is useful when you need to find a pair of elements in an array that satisfies a certain condition
    or when you need to find a subarray that satisfies a certain condition.
    """
    left = 0
    right = len(arr) - 1
    while left < right:
        left += 1
        right -= 1
    return
