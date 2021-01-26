num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([num_list[i] for i in range(1, len(num_list)) if num_list[i] > num_list[i - 1]])
