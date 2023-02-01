def read_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(list(map(int, line.strip().split(','))))
    return data

def knapsack(items, maxWeight):
    items.sort(key=lambda x: x[1], reverse=True)
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

input = input("Enter the filename: ")
filename = "Datasets/" + input
org_data = read_file(filename)
maxWeight = org_data[0][1]
del org_data[0]
data = [[sublist[1], sublist[2]] for sublist in org_data]
print("Largest value: " + str(knapsack(data, maxWeight)))
