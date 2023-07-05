def push(num):
    stack.append(num)


def pop():
    if len(stack) > 0:
        stack.pop()


def back():
    if len(stack) > 0:
        return stack[len(stack) - 1]


stack = []
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
operators = {'+', '-', '*'}
sequence = input()

for item in sequence:
    if item in numbers:
        push(int(item))
    elif item in operators:
        operand_2 = back()
        pop()
        operand_1 = back()
        pop()
        new_number = 0
        if item == '+':
            new_number = operand_1 + operand_2
        elif item == '-':
            new_number = operand_1 - operand_2
        elif item == '*':
            new_number = operand_1 * operand_2
        push(new_number)

print(back())
