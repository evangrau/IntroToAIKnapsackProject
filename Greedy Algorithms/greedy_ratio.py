def read_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(list(map(int, line.strip().split(','))))
    return data

def knapsack(items, maxWeight):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    n = len(items)
    totalValue = 0

    for i in range(n):
        if maxWeight == 0:
            return totalValue
        if items[i][0] <= maxWeight:
            totalValue += items[i][1]
            maxWeight -= items[i][0]
        else:
            fraction = maxWeight / items[i][0]
            totalValue += items[i][1] * fraction
            maxWeight = 0

    return totalValue

items = [(2,3),(3,4),(4,5),(5,8),(9,10)]
maxWeight = 20
print(knapsack(items, maxWeight))
