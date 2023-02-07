# function to get the information from the .kp file
def read_file(filename):
   data = []
   with open(filename) as f:
      for line in f:
         data.append(list(map(int, line.strip().split(','))))
   return data

filename = "Datasets/test1.kp"
org_data = read_file(filename)
max_weight = org_data[0][1] # gets max weight from the file
num_items = org_data[0][0] # gets number of items from the file
del org_data[0] # gets rid of first index in array containing number of lines and max weight
weights = [sublist[1] for sublist in org_data] # gets all of the weights and puts them into an array
values = [sublist[2] for sublist in org_data] # gets all of the values and puts them into an array to complement the weights

def knapSack(max_w, w, val, n):
   # initial conditions
   if n == 0 or max_w == 0:
      return 0
   # if weight is higher than capacity then it is not included
   if (w[n-1] > max_w):
      return knapSack(max_w, w, val, n-1)
   # return either nth item being included or not
   else:
      return max(val[n-1] + knapSack(max_w-w[n-1], w, val, n-1),
         knapSack(max_w, w, val, n-1))

print("Max value: " + str(knapSack(max_weight, weights, values, num_items)))