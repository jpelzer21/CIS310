# Juancamilo Castaneda, Joshua Pelzer, Ryan Stallings, Brian Hannah

import csv
from operator import itemgetter

lines = []
col_names = []

with open('input.csv', 'r') as in_fd:
    csv_reader = csv.reader(in_fd)
    col_names = next(csv_reader)

    for indx, i in enumerate(csv_reader):
        # make a tuple, first item is a float, second is a string
        float_and_string = (float(i[0]), i[1])

        # append lines array with new tuple
        lines.append(float_and_string)
        

# sort the data
lines = sorted(lines, key=itemgetter(0))


# find the 5th
fifth_val = lines[4][1]
# print(fifth_val)

# find the 10th
tenth_val = lines[9][1]
# print(tenth_val)


# output to output.txt
f = open("output.txt", "w")
f.write(fifth_val)
f.write('\n')
f.write(tenth_val)
f.close()
