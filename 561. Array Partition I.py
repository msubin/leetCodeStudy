"""
LeetCode 561) Array Partition I
Date: Jul 29th, 21
"""
import timer


@timer.timer
def arrayPairSum_subin(nums: list) -> int:
    num_list = sorted(nums)
    sum_list = []

    for n in range(0, len(nums) - 1, 2):
        sum_list.append(min(num_list[n], num_list[n + 1]))

    return sum(sum_list)


@timer.timer
def arrayPairSum_ascending(nums: list) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


@timer.timer
def arrayPairSum_even(nums: list) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


@timer.timer
def arrayPairSum_pythonic(nums: list) -> int:
    return sum(sorted(nums)[::2])


def main():
    nums = [6, 2, 6, 5, 1, 2]
    arrayPairSum_subin(nums)
    arrayPairSum_ascending(nums)
    arrayPairSum_even(nums)
    arrayPairSum_pythonic(nums)


if __name__ == "__main__":
    main()
