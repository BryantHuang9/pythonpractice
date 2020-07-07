from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv

import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open("C:\\Users\\Bryant\\Documents\\Python learning\\timexy.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    # reader = csv.DictReader(csv_file) # read rows into a dictionary format
    columns['time'] = []
    columns['x'] = []
    columns['y'] = []
    line_count = 0
    for row in csv_reader: # read a row as {column1: value1, column2: value2,...}
        if line_count == 0:
            line_count += 1
        else:
            columns['time'].append(float(row[0])) # append the value into the appropriate list
            columns['x'].append(float(row[1]))
            columns['y'].append(float(row[2]))
            line_count += 1


print(columns['time'])
print(columns['x'])
print(columns['y'])

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = columns['x']
y = columns['y']
z = columns['time']

ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Time")

plt.show()

