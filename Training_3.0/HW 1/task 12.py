def push(bracket):
    stack.append(bracket)


def pop():
    if len(stack) > 0:
        stack.pop()


def back():
    if len(stack) > 0:
        return stack[len(stack) - 1]


stack = []
sequence = input()
open_brackets = {'(', '[', '{'}
flag = True
if len(sequence) % 2 == 0:
    for item in sequence:
        if item in open_brackets:
            push(item)
        else:
            if item == ')':
                if back() == '(':
                    pop()
                else:
                    flag = False
                    break
            elif item == ']':
                if back() == '[':
                    pop()
                else:
                    flag = False
                    break
            elif item == '}':
                if back() == '{':
                    pop()
                else:
                    flag = False
                    break
else:
    flag = False

if flag:
    print('yes')
else:
    print('no')
