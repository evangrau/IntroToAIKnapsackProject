# function to get the information from the .kp file
def read_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(list(map(int, line.strip().split(','))))
    return data

filename = "Datasets/test5.kp"
org_data = read_file(filename)
maxWeight = org_data[0][1] # gets max weight from the file
num_items = org_data[0][0] # gets number of items from the file
del org_data[0] # gets rid of first index in array containing number of lines and max weight
# data = [[sublist[1], sublist[2]] for sublist in org_data] # creates new array containing weight and value
weights = [sublist[1] for sublist in org_data]
values = [sublist[2] for sublist in org_data]

def knapSack(W, wt, val, n):
    # initial conditions
    if n == 0 or W == 0 :
       return 0
    # if weight is higher than capacity then it is not included
    if (wt[n-1] > W):
       return knapSack(W, wt, val, n-1)
    # return either nth item being included or not
    else:
       return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
          knapSack(W, wt, val, n-1))

print("Max value: " + str(knapSack(maxWeight,weights,values,num_items)))