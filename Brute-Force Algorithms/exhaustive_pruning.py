# function to get the information from the .kp file
def read_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(list(map(int, line.strip().split(','))))
    return data

filename = "Datasets/test1.kp"
org_data = read_file(filename)
maxWeight = org_data[0][1] # gets max weight from the file
del org_data[0] # gets rid of first index in array containing number of lines and max weight
data = [[sublist[1], sublist[2]] for sublist in org_data] # creates new array containing weight and value
print(org_data)
print(data)