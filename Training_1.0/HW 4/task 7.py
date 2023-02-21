operations = {}


def check_client_in_data(client):
    if client not in operations:
        operations[client] = 0


with open('input.txt') as text:
    for line in text:
        data = line.split()
        operation = data[0]

        if operation == 'DEPOSIT':
            client_name = data[1]
            amount = int(data[2])
            check_client_in_data(client_name)
            operations[client_name] += amount
        elif operation == 'WITHDRAW':
            client_name = data[1]
            amount = int(data[2])
            check_client_in_data(client_name)
            operations[client_name] -= amount
        elif operation == 'BALANCE':
            client_name = data[1]
            if client_name not in operations:
                print('ERROR')
            else:
                print(operations[client_name])
        elif operation == 'INCOME':
            percent = int(data[1])
            for key, value in operations.items():
                if value > 0:
                    income = value * percent // 100
                    operations[key] += income
        elif operation == 'TRANSFER':
            client_name_1 = data[1]
            client_name_2 = data[2]
            amount = int(data[3])
            check_client_in_data(client_name_1)
            check_client_in_data(client_name_2)
            operations[client_name_1] -= amount
            operations[client_name_2] += amount
