def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")

            # not stack : 스텍이 비어있지 않을떄
            # 스텍이 비어있지 않고 마지막 스텍이 똑같지 않으면 False 리턴
        elif not stack or stack.pop() != p:
            return 'NO'
    return "YES"

s = int(input())
print(isValid(s))
