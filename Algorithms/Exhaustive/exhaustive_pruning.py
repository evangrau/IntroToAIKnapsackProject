import time

start_time = time.time()

# function to get the information from the .kp file
def read_file(filename):
   data = []
   with open(filename) as f:
      for line in f:
         data.append(list(map(str, line.strip().split(',')))) # implementation to accept strings for the label
   return data

filename = "Datasets/knapsack_testcases-final/test5.kp"
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
# matrix to contain previous answers for memoization
memo = [[-1 for x in range(max_weight + 1)] for y in range(num_items + 1)]

# exhaustive knapsack algorithm using memoization for pruning
def knapsack(max_w, w, val, n, memo):
   # initial conditions
   # if num of items is 0 or max weight is 0 then the max has to be 0
   if n == 0 or max_w == 0:
      return 0, 0, 0
   # if the value in memo isnt a useless value (i.e. -1) then we can return that value
   if memo[n][max_w] != -1:
      return memo[n][max_w]
   # if weight is higher than capacity then it is not included 
   if w[n-1] > max_w:
      memo[n][max_w] = knapsack(max_w, w, val, n-1, memo)
   # set current value of memo to nth item being included or not
   else:
      # tries set with item
      with_item_val, with_item_weight, with_item_num_items = knapsack(max_w-w[n-1], w, val, n-1, memo)
      with_item_val += val[n-1]
      with_item_weight += w[n-1]
      with_item_num_items += 1

      # tries set without item  
      without_item_val, without_item_weight, without_item_num_items = knapsack(max_w, w, val, n-1, memo)

      # returns value based on which is higher  
      if with_item_val > without_item_val:
         memo[n][max_w] = (with_item_val, with_item_weight, with_item_num_items)
      else:
         memo[n][max_w] = (without_item_val, without_item_weight, without_item_num_items)
    
   return memo[n][max_w]

v, w, i = knapsack(max_weight, weights, values, num_items, memo)

print("Max value:", v)
print("Weight:", w)
print("Number of items:", i)

end_time = time.time()
time_elapsed = (end_time - start_time) * 1000
print("Time elapsed: {:.4f} milliseconds".format(time_elapsed))
