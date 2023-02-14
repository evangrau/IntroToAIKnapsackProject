import time

start_time = time.time()

# function to get the information from the .kp file
def read_file(filename):
   data = []
   with open(filename) as f:
      for line in f:
         data.append(list(map(str, line.strip().split(',')))) # implementation to accept strings for the label
   return data

filename = "Datasets/final_testcases-final/test1.kp"
org_data = read_file(filename)

max_weight = int(org_data[0][1]) # gets max weight from the file
del org_data[0] # gets rid of first index in array containing number of lines and max weight

data = [[int(sublist[1]), int(sublist[2])] for sublist in org_data]

def bit_climbing_knapsack(items, max_weight):
   n = len(items)
   dp = [[0 for _ in range(max_weight + 1)] for _ in range(n)]
    
   for i in range(n):
      for w in range(max_weight + 1):
         if items[i][0] <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i][0]] + items[i][1])
         else:
            dp[i][w] = dp[i-1][w]
    
   max_value = dp[n-1][max_weight]
   weight = max_weight
   num_items = 0
   item_weights = []
    
   for i in range(n-1, -1, -1):
      if max_value != dp[i-1][weight] and i > 0:
         num_items += 1
         item_weights.append(items[i][0])
         max_value -= items[i][1]
         weight -= items[i][0]
      elif max_value == dp[i-1][weight] and i > 0:
         continue
      elif max_value != 0:
         num_items += 1
         item_weights.append(items[i][0])
         max_value -= items[i][1]
         weight -= items[i][0]
      else:
         break
                
   return dp[n-1][max_weight], sum(item_weights), num_items


v, w, i = bit_climbing_knapsack(data, max_weight)

print("Max value:", v)
print("Weight:", w)
print("Number of items:", i)

end_time = time.time()
time_elapsed = (end_time - start_time) * 1000
print("Time elapsed: {:.4f} milliseconds".format(time_elapsed))
