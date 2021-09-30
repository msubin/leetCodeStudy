"""
LeetCode 1) Two Sum
Date: Jul 13, 21
"""
import timer


@timer.timer
def twoSum_brute(nums: list, target: int) -> list:
    for m in range(len(nums)):
        for n in range(m + 1, len(nums)):
            if nums[m] + nums[n] == target:
                return [m, n]


@timer.timer
def twoSum_in(nums: list, target: int) -> list:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


@timer.timer
def twoSum_hash_1(nums: list, target: int) -> list:
    nums_map = {}
    # Value = Key / Index = value
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


@timer.timer
def twoSum_hash_2(nums: list, target: int) -> list:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


def main():
    nums = [2, 7, 11, 15]
    target = 9
    twoSum_brute(nums, target)
    twoSum_in(nums, target)
    twoSum_hash_1(nums, target)
    twoSum_hash_2(nums, target)


if __name__ == "__main__":
    main()