from sys import argv

script_name, productivity, hourly_rate, bonus = argv

print('Ваша заработная плата -', int(productivity) * int(hourly_rate) + int(bonus))
