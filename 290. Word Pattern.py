"""
LeetCode 290) Word Pattern
Date: Oct 2, 21
"""
import timer


@timer.timer
def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    words = s.split(" ")

    word_dict = {}
    pattern_dict = {}

    if len(pattern) != len(words):
        return False

    for i in range(len(pattern)):
        try:
            temp = word_dict[words[i]]
            if temp != pattern[i]:
                return False

        except KeyError:
            word_dict[words[i]] = pattern[i]

            try:
                temp_2 = pattern_dict[pattern[i]]
                if temp_2 != word_dict[words[i]]:
                    return False
            except KeyError:
                pattern_dict[pattern[i]] = words[i]
    return True


def main():
    print(wordPattern("aaba", "dog dog cat dog"))


if __name__ == "__main__":
    main()
