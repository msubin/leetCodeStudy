"""
LeetCode 125) Valid Palindrome
Date: Jul 14, 21
"""
import timer


@timer.timer
def isPalindrome(s: str) -> bool:
    s_list = []

    for char in s:
        if char.isalnum():
            s_list.append(char.lower())

    while len(s_list) > 1:
        if s_list.pop(0) != s_list.pop():
            print(s_list)
            return False

    return True


def main():
    isPalindrome("A man, a plan, a canal: Panama")


if __name__ == "__main__":
    main()
