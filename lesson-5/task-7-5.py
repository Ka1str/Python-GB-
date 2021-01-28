import json

profit_firm = dict()
loss_firm = dict()

with open('task-7.txt', encoding='utf-8') as my_file:
    temp_profit = []

    for line in my_file:
        name = line.split()[0]
        proceeds = int(line.split()[2])
        costs = int(line.split()[3])

        if proceeds > costs:
            profit = proceeds - costs
            temp_profit.append(profit)
            profit_firm.update({name: profit})
            print(f'Фирма {name} имеет прибыль {profit}')

        elif costs > proceeds:
            loss = proceeds - costs
            loss_firm.update({name: loss})
            print(f'Фирма {name} имеет убыток {loss}')

    average_profit = sum(temp_profit) / len(temp_profit)
    average_profit_dict = {'average_profit': average_profit}
    print(f'Средняя прибыль прибыльных фирм: {average_profit}')

report = [profit_firm, average_profit_dict, loss_firm]

with open('report.json', 'w') as file:
    json.dump(report, file)
