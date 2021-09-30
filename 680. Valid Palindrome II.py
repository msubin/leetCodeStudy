"""
LeetCode 125) Valid Palindrome
Date: Sep 24, 21
"""

import timer


def validPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return isPalindrome(s[left + 1:right + 1]) or isPalindrome(s[left:right])
        else:
            left += 1
            right -= 1
    return True


def isPalindrome(s: str) -> bool:
    return s == s[::-1]


# @timer.timer
# def validPalindrome(s: str) -> bool:
    # Time: O(n)
    # Space: O(n)
    # left, right = 0, len(s) - 1
    # while left < right:
    #     if s[left] != s[right]:
    #         one, two = s[left:right], s[left+1: right+1]
    #         return one == one[::-1] or two == two[::-1]
    #     left, right = left + 1, right - 1
    # return True


# def validPalindrome(s: str) -> bool:
#     left = 0
#     right = len(s) - 1
#
#     while left < right:
#         if s[left] != s[right]:
#             return isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1)
#
#         left += 1
#         right -= 1
#
#     return True


# def isPalindrome(s: str, leftPointer: int, rightPointer: int) -> bool:
#     while leftPointer < rightPointer:
#         if s[leftPointer] != s[rightPointer]:
#             return False
#         leftPointer += 1
#         rightPointer -= 1
#     return True


def main():
    print(validPalindrome("amanaplanacanalpanama"))
    print(validPalindrome("abc"))
    print(validPalindrome(""))
    print(validPalindrome("effe"))
    print(validPalindrome("abca"))


if __name__ == "__main__":
    main()