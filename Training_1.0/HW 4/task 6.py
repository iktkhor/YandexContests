buyers = {}
with open('input.txt') as text:
    for line in text:
        data = line.split()
        name = data[0]
        product = data[1]
        amount = data[2]
        if name not in buyers:
            buyers[name] = {product: 0}
        elif product not in buyers[name]:
            buyers[name][product] = 0
        buyers[name][product] += int(amount)

for buyer in sorted(buyers.keys()):
    print(buyer + ':')
    for item in sorted(buyers[buyer].keys()):
        print(item, buyers[buyer][item])



