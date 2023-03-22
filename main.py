import numpy as np

# create an empty list to store the sums
sums = []

# read the input file and split the arrays
with open('input.txt') as f:
    values = []
    for line in f:
        # check if the line is empty
        if line.strip() == '':
            # convert the values list to a NumPy ndarray and calculate the sum
            array = np.array(values, dtype=int)
            array_sum = np.sum(array)
            # add the sum to the list of sums
            sums.append(array_sum)
            # reset the values list
            values = []
        else:
            # add the value to the values list
            values.append(int(line.strip()))

    # calculate the sum of the last array and add it to the list of sums
    array = np.array(values, dtype=int)
    array_sum = np.sum(array)
    sums.append(array_sum)
max = 0
# print the list of sums
for i in sums:
    if max < i:
        max = i
print(max)


###### End of part one
sums.sort()
print(sums[-1]+sums[-2]+sums[-3])
##### end of part 2
