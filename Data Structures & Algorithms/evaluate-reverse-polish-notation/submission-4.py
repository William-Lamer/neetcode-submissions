class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens: 
            
            if tok != "+" and tok != "*" and tok != "-" and tok != "/":
                stack.append(int(tok))
                continue

            second = stack.pop()
            first = stack.pop()

            if tok == "+":
                stack.append(first + second) 
            elif tok == "-":
                stack.append(first - second) 
            elif tok == "*":
                stack.append(first * second) 
            elif tok == "/":
                stack.append(int(first / second)) 
            


        return stack.pop()