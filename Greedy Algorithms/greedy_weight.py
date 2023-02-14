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
        while j >= 0 and items[j][0] > key[0]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
    return items

def knapsack(items, maxWeight):
    n = len(items)
    totalValue = 0

    for i in range(n):
        if maxWeight == 0:
            return int(totalValue)
        a = min(items[i][0], maxWeight)
        totalValue += a * (items[i][1] / items[i][0])
        maxWeight -= a

    return int(totalValue)

filename = "Datasets/test1.kp"
org_data = read_file(filename)
maxWeight = int(org_data[0][1])
del org_data[0]
data = [[int(sublist[1]), int(sublist[2])] for sublist in org_data]
data = insertion_sort(data)
print("Max value: " + str(knapsack(data, maxWeight)))

end_time = time.time()
time_elapsed = (end_time - start_time) * 1000
print("Time elapsed: {:.4f} milliseconds".format(time_elapsed))
