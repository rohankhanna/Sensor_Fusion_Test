import json
import matplotlib.pyplot as plt
import csv

objId = []
x = []
y = []
timestamp = []

with open("../../dist/expectedOutputData.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if row[0] == "objId":
            continue
        objId.append(row[0])
        x.append(float(row[1]))
        y.append(float(row[2]))
        timestamp.append(row[3])


plt.scatter(x=x, y=y, color='gray')


plt.show()
