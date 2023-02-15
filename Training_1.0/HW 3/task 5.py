def min_buttons(buttons_menu, number):
    buttons = set()
    buttons_used = set()
    min_buttons = 0

    for button in buttons_menu:
        buttons.add(button)
    for letter in number:
        if (letter not in buttons) and (letter not in buttons_used):
            buttons_used.add(letter)
            min_buttons += 1

    return min_buttons


buttons = list(input().split())
number = input()
print(min_buttons(buttons, number))
