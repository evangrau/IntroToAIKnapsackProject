import time

start_time = time.time()

# function to get the information from the .kp file
def read_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(list(map(str, line.strip().split(','))))
    return data

# insertion sort function to sort items by value
def insertion_sort(items):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j][1] > key[1]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
    return items

def knapsack(items, max_weight):
    n = len(items)
    totalValue = 0
    totalWeight = 0
    numItems = 0

    for i in range(n-1, -1, -1):
        if totalWeight + items[i][0] <= max_weight:
            totalValue += items[i][1]
            totalWeight += items[i][0]
            numItems += 1
        else:
            break

    return totalValue, totalWeight, numItems

filename = "Datasets/knapsack_testcases-final/test400.kp"
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
