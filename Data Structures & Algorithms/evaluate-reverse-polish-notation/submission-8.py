class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        math_tokens = ['+', '-', '*', '/']
        for token in tokens:
            if token in math_tokens: 
                b = stack.pop()
                a = stack.pop()
                
                print(a)
                print(token)
                print(b)
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                else:
                    x = a/b
                    if x<0:
                        stack.append(math.ceil(x))
                    else:
                        stack.append(math.floor(x))
            else:
                stack.append(int(token))
        print(stack)
        return stack[-1]