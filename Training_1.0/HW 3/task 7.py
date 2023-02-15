def is_real(positions, turtles):
    if abs(positions[0]) + abs(positions[1]) != turtles - 1:
        return False
    return True


def true_turtles():
    turtles = int(input())
    positions = set()
    ans = 0
    for i in range(turtles):
        position = input()
        if position not in positions:
            if is_real(list(map(int, position.split())), turtles):
                positions.add(position)
                ans += 1
    return ans


print(true_turtles())
