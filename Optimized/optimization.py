import time

start_time = time.time()

# function to get the information from the .kp file
def read_file(filename):
   data = []
   with open(filename) as f:
      for line in f:
         data.append(list(map(str, line.strip().split(',')))) # implementation to accept strings for the label
   return data

filename = "Datasets/n06.kp"
org_data = read_file(filename)

max_weight = int(org_data[0][1]) # gets max weight from the file
num_items = int(org_data[0][0]) # gets number of items from the file
del org_data[0] # gets rid of first index in array containing number of lines and max weight

end_time = time.time()
time_elapsed = (end_time - start_time) * 1000
print("Time elapsed: {:.4f} milliseconds".format(time_elapsed))
