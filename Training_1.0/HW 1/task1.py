t_room, t_cond = map(int, input().split())
regime = input()

if regime == "heat":
    if t_room > t_cond:
        print(t_room)
    else:
        print(t_cond)
elif regime == "freeze":
    if t_room <= t_cond:
        print(t_room)
    else:
        print(t_cond)
elif regime == "auto":
    print(t_cond)
elif regime == "fan":
    print(t_room)
