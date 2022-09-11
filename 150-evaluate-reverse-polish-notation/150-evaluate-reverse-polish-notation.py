class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = { "+": 1, "-": 1, "*":1, "/":1 }
        for x in tokens:
            if x not in op.keys():
                stack.append(x)
            else:
                b=int(stack.pop())
                a = int(stack.pop())
                if x == "+":
                    y = a + b
                elif x == "*":
                    y = a*b
                elif x == "-":
                    y = a-b
                else:
                    y = int(a/b)
                stack.append(y)
        return stack[0]
        