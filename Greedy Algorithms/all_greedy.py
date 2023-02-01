# function to get the information from the .kp file
def read_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(list(map(int, line.strip().split(','))))
    return data

# greedy algorithm that sorts the items by weight
def greedy_weight(items, maxWeight):
    items.sort(key=lambda x: x[0])
    n = len(items)
    totalValue = 0

    for i in range(n):
        if maxWeight == 0:
            return int(totalValue)
        a = min(items[i][0], maxWeight)
        totalValue += a * (items[i][1] / items[i][0])
        maxWeight -= a

    return int(totalValue)

# greedy algorithm that sorts the items by weight
def greedy_value(items, maxWeight):
    items.sort(key=lambda x: x[1], reverse=True)
    n = len(items)
    totalValue = 0

    for i in range(n):
        if maxWeight == 0:
            return int(totalValue)
        if items[i][0] <= maxWeight:
            totalValue += items[i][1]
            maxWeight -= items[i][0]
        else:
            fraction = maxWeight / items[i][0]
            totalValue += items[i][1] * fraction
            maxWeight = 0

    return int(totalValue)

# greedy algorithm that sorts the items by the value:weight ratio
def greedy_ratio(items, maxWeight):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    n = len(items)
    totalValue = 0

    for i in range(n):
        if maxWeight == 0:
            return int(totalValue)
        if items[i][0] <= maxWeight:
            totalValue += items[i][1]
            maxWeight -= items[i][0]
        else:
            fraction = maxWeight / items[i][0]
            totalValue += items[i][1] * fraction
            maxWeight = 0

    return int(totalValue)

input = input("Enter the filename: ") # gets the filename from the user
filename = "Datasets/" + input
org_data = read_file(filename)
maxWeight = org_data[0][1] # gets max weight from the file
del org_data[0] # gets rid of first index in array containing number of lines and max weight
data = [[sublist[1], sublist[2]] for sublist in org_data] # creates new array containing weight and value
print("Largest value for greedy algorithm sorting by weight: " + str(greedy_weight(data, maxWeight)))
print("Largest value for greedy algorithm sorting by value: " + str(greedy_value(data, maxWeight)))
print("Largest value for greedy algorithm sorting by value:weight ratio: " + str(greedy_ratio(data, maxWeight)))