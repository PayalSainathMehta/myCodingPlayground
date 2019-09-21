def removeOuterParenthesis(S):
    stack = []
    res = ''
    for i,char in enumerate(S):
        if char == ')':
            top = stack.pop()
            if not stack:
                res = res + S[pre + 1:i]

        else:
            if not stack:
                pre = i
            stack.append(char)

    return res
