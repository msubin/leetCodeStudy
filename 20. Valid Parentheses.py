"""
LeetCode 20) Valid Parentheses
Date: Aug 3, 21
"""
import timer


@timer.timer
def isValid(s: str) -> bool:
    stack = []
    table = {"}": "{", ")": "(", "]": "[" }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


def main():
    isValid("{[}]")


if __name__ == "__main__":
    main()