def read_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(list(map(int, line.strip().split(','))))
    return data

def knapsack(items, maxWeight):
    items.sort(key=lambda x: x[0])
    n = len(items)
    totalValue = 0

    for i in range(n):
        if maxWeight == 0:
            return totalValue
        a = min(items[i][0], maxWeight)
        totalValue += a * (items[i][1] / items[i][0])
        maxWeight -= a

    return totalValue

filename = "Datasets/evan_hunter5.kp"
data = read_file(filename)
print("Largest value: " + str(knapsack(data, maxWeight)))