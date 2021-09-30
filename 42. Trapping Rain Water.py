"""
LeetCode 42) Trapping Rain Water
Date: Jul 20, 21
"""
import timer


@timer.timer
def trap_brute(height: list) -> int:
    water = 0

    # iterate the array from left to right
    for i in range(1, len(height) - 1):
        left = height[i]
        for j in range(i):
            left = max(left, height[j])

        right = height[i]
        for j in range(i + 1, len(height)):
            right = max(right, height[j])

        water += (min(left, right) - height[i])

    return water


@timer.timer
def trap_dynamic(height: list) -> int:
    left = [0] * len(height)
    right = [0] * len(height)

    water = 0

    # Fill left array
    left[0] = height[0]
    for i in range(1, len(height)):
        left[i] = max(left[i - 1], height[i])

    # Fill right array
    right[len(height) - 1] = height[-1]
    for i in range(len(height) - 2, -1, -1):
        right[i] = max(right[i + 1], height[i])

    for i in range(len(height)):
        water += min(left[i], right[i]) - height[i]

    return water


@timer.timer
def trap_twoPointer(height: list) -> int:
    if not height:
        return 0

    water = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            water += left_max - height[left]
            left += 1
        else:
            water += right_max - height[right]
            right -= 1

    return water


@timer.timer
def trap_stack(height: list) -> int:
    stack = []
    water = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            water += distance * waters

        stack.append(i)

    return water


def main():
    ex = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    trap_brute(ex)
    trap_dynamic(ex)
    trap_twoPointer(ex)
    trap_stack(ex)


if __name__ == "__main__":
    main()