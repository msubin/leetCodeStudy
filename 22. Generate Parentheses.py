"""
LeetCode 22) Generate Parentheses
Date: Jul 28, 21
"""


def generateParenthesis(n: int) -> list:
    ans = []
    def backtrack(S = [], left = 0, right = 0):
        if len(S) == 2 * n:
            ans.append("".join(S))
            return
        if left < n:
            S.append("(")
            backtrack(S, left+1, right)
            S.pop()
        if right < left:
            S.append(")")
            backtrack(S, left, right+1)
            S.pop()
    backtrack()
    return ans


print(generateParenthesis(2))

"(" "("