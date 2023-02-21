keys = int(input())
keys_clicks = list(map(int, input().split()))
clicks = int(input())
keys_clicked = list(map(int, input().split()))
for clicked in keys_clicked:
    keys_clicks[clicked - 1] -= 1
for clicks in keys_clicks:
    if clicks < 0:
        print("YES")
    else:
        print("NO")
