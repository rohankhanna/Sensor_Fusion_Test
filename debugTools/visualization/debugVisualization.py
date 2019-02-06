import json
import matplotlib.pyplot as plt
import csv

# x = []
# y = []

# x_ = []
# y_ = []

# x__ = []
# y__ = []

# with open("../../dist/expectedOutputData.csv", "r") as stream:
#     expOutput = csv.load(stream)
objId = []
x = []
y = []
timestamp = []

_objId = []
_x = []
_y = []
_timestamp = []

__objId = []
__x = []
__y = []
__timestamp = []
# with open("../../dist/expectedOutputData.csv") as csvDataFile:
#     csvReader = csv.reader(csvDataFile)
#     for row in csvReader:
#         if row[0] == "objId":
#             continue
#         objId.append(row[0])
#         x.append(float(row[1]))
#         y.append(float(row[2]))
#         timestamp.append(row[3])

with open("../../dist/cameraDataExpectedInput.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if row[0] == "objId":
            continue
        objId.append(row[0])
        x.append(float(row[1]))
        y.append(float(row[2]))
        timestamp.append(row[3])

with open("../../dist/shortRangeRadarDataExpectedInput.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if row[0] == "objId":
            continue
        _objId.append(row[0])
        _x.append(float(row[1]))
        _y.append(float(row[2]))
        _timestamp.append(row[3])


with open("../../dist/longRangeRadarDataExpectedInput.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if row[0] == "objId":
            continue
        __objId.append(row[0])
        __x.append(float(row[1]))
        __y.append(float(row[2]))
        __timestamp.append(row[3])

plt.scatter(x=x, y=y, color='red')
plt.scatter(x=_x, y=_y, color='blue')
plt.scatter(x=__x, y=__y, color='green')

plt.show()
