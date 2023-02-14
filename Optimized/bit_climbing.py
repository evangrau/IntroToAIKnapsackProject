import time

start_time = time.time()

# function to get the information from the .kp file
def read_file(filename):
   data = []
   with open(filename) as f:
      for line in f:
         data.append(list(map(str, line.strip().split(',')))) # implementation to accept strings for the label
   return data

filename = "Datasets/test8.kp"
org_data = read_file(filename)

max_weight = int(org_data[0][1]) # gets max weight from the file
del org_data[0] # gets rid of first index in array containing number of lines and max weight

data = [[int(sublist[1]), int(sublist[2])] for sublist in org_data]

def bit_climbing_knapsack(items, max_weight):
   n = len(items)
   dp = [0 for _ in range(max_weight + 1)]
    
   for i in range(n):
      for w in range(max_weight, 0, -1):
         if items[i][0] <= w:
            dp[w] = max(dp[w], dp[w - items[i][0]] + items[i][1])
    
   return dp[max_weight]

print("Max value:", bit_climbing_knapsack(data, max_weight))

end_time = time.time()
time_elapsed = (end_time - start_time) * 1000
print("Time elapsed: {:.4f} milliseconds".format(time_elapsed))
