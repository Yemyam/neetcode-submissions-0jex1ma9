class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                op1 = int(stack.pop(-1))
                op2 = int(stack.pop(-1))
                match token:
                    case "+":
                        stack.append(op1+op2)
                    case "-":
                        stack.append(op2-op1)
                    case "*":
                        stack.append(op1*op2)
                    case "/":
                        stack.append(op2/op1)
            else:
                stack.append(token)

        if len(tokens) == 1:
            return int(tokens[0])

        return int(stack[0])