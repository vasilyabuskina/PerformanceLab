import math
import sys

print(sys.argv)

file = open(sys.argv[1], "r")
file1 = [line.strip() for line in file]

file = open(sys.argv[2], "r")
file2 = [line.strip() for line in file]

#print(file1)
#print(file2)

# ================================

center = file1[0]
center = center.split()
rad = float(file1[1])
#print(center)
for line in file2:
    #print(line.split())
    point = line.split()
    dist = math.sqrt((float(center[0]) - float(point[0])) ** 2 + (float(center[1]) - float(point[1])) ** 2)
    #print(dist)
    if dist < rad:
        print(1)
    elif dist > rad:
        print(2)
    else:
        print(0)
