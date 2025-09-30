

def eval_rpn(tokens):
    stack = []
    operators = {"+", "-", "*", "/"}
    
    for token in tokens:
        if token not in operators:
            # token is a number, push it as int
            stack.append(int(token))
        else:
            # token is an operator; pop two operands
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:  # token == "/"
                # integer division that truncates toward zero
                stack.append(int(a / b))
    
    return stack.pop()
