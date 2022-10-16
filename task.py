
def calc_digit_sum(x, numbers):
    sum = 0
    if x == 0:
        return 0
    while x > 0:
        sum += int(x % 10)
        x /= 10
        if x in numbers:
            return numbers[x] + sum
    return sum

def count_groups_size_from_zero(n_customers):
    groups = {}
    numbers = {}
    for i in range(n_customers + 1):
        group_num = calc_digit_sum(i, numbers)
        if group_num in groups:
            groups[group_num] += 1
        else:
            groups[group_num] = 1
    for key, value in groups.items():
        print("Группа", key, " Количество", value)

def count_groups_size(n_first_id, n_customers):
    groups = {}
    numbers = {}
    for i in range(n_first_id, n_customers + 1):
        group_num = calc_digit_sum(i, numbers)
        if group_num in groups:
            groups[group_num] += 1
        else:
            groups[group_num] = 1
    for key, value in groups.items():
        print("Группа", key, " Количество", value)

count_groups_size(10000, 453212)


