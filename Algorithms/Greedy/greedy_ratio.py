import time

start_time = time.time()

def read_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(list(map(str, line.strip().split(','))))
    return data

def insertion_sort(items):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j][1]/items[j][0] < key[1]/key[0]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
    return items

def knapsack(items, max_weight):
    n = len(items)
    total_value = 0
    total_weight = 0
    num_items = 0

    for i in range(n):
        if max_weight == 0:
            break
        if items[i][0] <= max_weight:
            total_value += items[i][1]
            total_weight += items[i][0]
            max_weight -= items[i][0]
            num_items += 1

    return total_value, total_weight, num_items


filename = "Datasets/knapsack_testcases-final/test4.kp"
org_data = read_file(filename)
max_weight = int(org_data[0][1])
del org_data[0]
data = [[int(sublist[1]), int(sublist[2])] for sublist in org_data]
data = insertion_sort(data)

v, w, i = knapsack(data, max_weight)

print("Max value:", v)
print("Weight:", w)
print("Number of items:", i)

end_time = time.time()
time_elapsed = (end_time - start_time) * 1000
print("Time elapsed: {:.0f} milliseconds".format(time_elapsed))
