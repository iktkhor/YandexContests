def push(number):
    stack.append(number)
    print('ok')


def pop():
    if len(stack) > 0:
        print(stack[len(stack) - 1])
        stack.pop()
    else:
        print('error')


def size():
    print(len(stack))


def back():
    if len(stack) > 0:
        print(stack[len(stack) - 1])
    else:
        print('error')


def clear():
    stack.clear()
    print('ok')


stack = []

while True:
    line = input().split()
    if line[0] == 'push':
        push(int(line[1]))
    elif line[0] == 'pop':
        pop()
    elif line[0] == 'back':
        back()
    elif line[0] == 'size':
        size()
    elif line[0] == 'clear':
        clear()
    elif line[0] == 'exit':
        print('bye')
        break
