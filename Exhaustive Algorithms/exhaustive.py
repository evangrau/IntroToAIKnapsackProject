# function to get the information from the .kp file
def read_file(filename):
   data = []
   with open(filename) as f:
      for line in f:
         data.append(list(map(str, line.strip().split(',')))) # implementation to accept strings for the label
   return data

filename = "Datasets/test1.kp"
org_data = read_file(filename)

max_weight = int(org_data[0][1]) # gets max weight from the file
num_items = int(org_data[0][0]) # gets number of items from the file
del org_data[0] # gets rid of first index in array containing number of lines and max weight

# gets all of the weights and puts them into an array and does the same with complementing values
weights = [sublist[1] for sublist in org_data]
values = [sublist[2] for sublist in org_data]
# converts the arrays into int arrays
weights = [int(i) for i in weights]
values = [int(i) for i in values]

# basic exhaustive knapsack algorithm
def knapsack(max_w, w, val, n):
   # initial conditions
   # if num of items is 0 or max weight is 0 then the max has to be 0
   if n == 0 or max_w == 0:
      return 0
   # if weight is higher than capacity then it is not included
   if (w[n-1] > max_w):
      return knapsack(max_w, w, val, n-1)
   # return either nth item being included or not
   else:
      return max(val[n-1] + knapsack(max_w-w[n-1], w, val, n-1),
         knapsack(max_w, w, val, n-1))

print("Max value: " + str(knapsack(max_weight, weights, values, num_items)))
