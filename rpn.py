
stack = []

def add():
    b = stack.pop()
    a = stack.pop()
    stack.append(a + b)

def subtract():
    b = stack.pop()
    a = stack.pop()
    stack.append(a - b)

def multiply():
    b = stack.pop()
    a = stack.pop()
    stack.append(a * b)

def divide():
    b = stack.pop()
    a = stack.pop()
    stack.append(a / b)

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

while True:
    inpt = input()
    
    try:
        inpt = float(inpt)
        stack.append(inpt)
    except:
        try:
            inpt = operations[inpt]()
            print(stack[-1])
        except:
            raise ValueError

    print(stack)