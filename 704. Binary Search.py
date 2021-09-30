"""
LeetCode 704) Binary Search
Date: Jul 15, 21
"""
import timer, bisect


@timer.timer
def search_recursion(nums: list, target: int) -> int:
    def binary_search(left, right):
        if left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return mid
        else:
            return -1

    return binary_search(0, len(nums) - 1)


@timer.timer
def search_iterative(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


@timer.timer
def search_bisect(nums: list, target: int) -> int:
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index

    else:
        return -1


@timer.timer
def search_index(nums: list, target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1

@timer.timer
def search(nums: list, target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        return -1


def main():
    nums = [i for i in range(1, 100000, 3)]
    target = 89723

    search_recursion(nums, target)
    search_iterative(nums, target)
    search_bisect(nums, target)
    search_index(nums, target)
    search(nums, target)


if __name__ == "__main__":
    main()
