class Item:
    num = 0
    weight = 0
    value = 0

input = input("Enter the filename: ")               #prompt user
filename = "Datasets/" + input                      #create filename
count = -1
data = []
with open(filename) as f:                           #read file
    for line in f:
        if(count == -1):                         #first line
            firstLine = line.split(",")
            numItems = int(firstLine[0])
            maxWeight = int(firstLine[1])
            for i in range(0,numItems):
                data.append(Item())
        else:                                      #read into data array
            currLine = line.split(",")
            data[count].num = int(currLine[0])
            data[count].weight = int(currLine[1])
            data[count].value = int(currLine[2])
        count+=1

# greedy algorithm that sorts the items by weight
# insertion sort data by weight

for i in range(1, len(data)):    #set item to be fixed
    fix = data[i].weight
    fixNum = data[i].num
    fixVal = data[i].value
    fixInd = i

    j = i-1
    while j >= 0 and data[j].weight > fix:   #finding correct position for fix
        data[j+1].weight = data[j].weight
        data[j+1].num = data[j].num
        data[j+1].value = data[j].value

        j-=1
    data[j+1].weight = fix     #swapping values
    data[j+1].num = fixNum
    data[j+1].value = fixVal

#select values
maxWeightTemp = maxWeight
currValue = 0
for i in range(0, len(data)):
    if(maxWeightTemp - data[i].weight >= 0):
        currValue += data[i].value
        maxWeightTemp -= data[i].weight
    else:
        exit

# Greedy Algorithm by weight results
print("Greedy algorithm by weight max value: ", currValue, "\n")

# greedy algorithm that sorts the items by value
# insertion sort data by value

for i in range(1, len(data)):    #set item to be fixed
    fix = data[i].value
    fixNum = data[i].num
    fixWeight = data[i].weight
    fixInd = i

    j = i-1
    while j >= 0 and data[j].value > fix:   #finding correct position for fix
        data[j+1].weight = data[j].weight
        data[j+1].num = data[j].num
        data[j+1].value = data[j].value

        j-=1
    data[j+1].weight = fixWeight     #swapping values
    data[j+1].num = fixNum
    data[j+1].value = fix

#select values
maxWeightTemp = maxWeight
currValue = 0
for i in range(0, len(data)):
    if(maxWeightTemp - data[i].weight >= 0):
        currValue += data[i].value
        maxWeightTemp -= data[i].weight

# Greedy Algorithm by value results
print("Greedy algorithm by value max value: ", currValue, "\n")

for i in range(1, len(data)):    #set item to be fixed
    fix = data[i].value / data[i].weight
    fixNum = data[i].num
    fixWeight = data[i].weight
    fixVal = data[i].value
    fixInd = i

    j = i-1
    while j >= 0 and data[j].value / data[j].weight < fix:   #finding correct position for fix
        data[j+1].weight = data[j].weight
        data[j+1].num = data[j].num
        data[j+1].value = data[j].value

        j-=1

    data[j+1].weight = fixWeight     #swapping values
    data[j+1].num = fixNum
    data[j+1].value = fixVal

#select values
maxWeightTemp = maxWeight
currValue = 0
for i in range(0, len(data)):
    if(maxWeightTemp - data[i].weight >= 0):
        currValue += data[i].value
        maxWeightTemp -= data[i].weight


# Greedy Algorithm by ratio results
print("Greedy algorithm by value:weight ratio max value: ", currValue, "\n")
