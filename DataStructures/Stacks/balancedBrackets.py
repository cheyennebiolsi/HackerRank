def is_matched(expression):
    matches = {"{":"}", "(":")", "[":"]", "}":"{", ")":"(", "]":"["}
    stack = []
    for character in expression:
        if len(stack) != 0:
            if stack[-1] == matches[character]:
                stack.pop()
                continue
        stack.append(character)
    return len(stack) == 0

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
