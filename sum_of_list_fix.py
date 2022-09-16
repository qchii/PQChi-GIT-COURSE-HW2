def sum_list(list):
    sum = 0
    for i in list:
        if i.isnumeric():
            sum += i
    return sum