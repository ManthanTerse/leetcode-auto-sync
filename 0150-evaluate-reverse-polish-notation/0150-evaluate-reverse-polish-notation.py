class Solution(object):
    def evalRPN(self, tokens):
        s = []
        for token in tokens:
            if token not in "+-*/":
                s.append(int(token))
            else:
                b = s.pop()
                a = s.pop()
                if token == "+":
                    s.append(a + b)
                elif token == "-":
                    s.append(a - b)
                elif token == "*":
                    s.append(a * b)
                else:
                    s.append(int(float(a)/b))
        return s.pop()