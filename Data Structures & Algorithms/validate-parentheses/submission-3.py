class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        pars = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in pars.keys():
                stack.append(c)
            elif c in pars.values():
                if len(stack) ==0:
                    return False
                correct = pars.get(stack[-1]) == c
                if not correct:
                    return False
                stack = stack[:-1]
            else:
                return False 
        if len(stack) >0:
            return False
        return True 