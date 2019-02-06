import json
import matplotlib.pyplot as plt

x = []
y = []

x_ = []
y_ = []

x__ = []
y__ = []

with open("../../dist/shortRangeRadarData.csv", "r") as stream:
    sRR = json.load(stream)

with open("../../dist/longRangeRadarData.csv", "r") as stream:
    lRR = json.load(stream)

with open("../../dist/cameraData.csv", "r") as stream:
    camera = json.load(stream)

print(sRR["timestamp"]["0"][0])
print(lRR["timestamp"]["0"][0])
print(camera["timestamp"]["0"][0])

for i in range(len(sRR["timestamp"]["0"])):
    x.append(sRR["timestamp"]["0"][i]["x"])
    y.append(sRR["timestamp"]["0"][i]["y"])

plt.scatter(x, y, color='red')

for i in range(len(lRR["timestamp"]["0"])):
    x_.append(lRR["timestamp"]["0"][i]["x"])
    y_.append(lRR["timestamp"]["0"][i]["y"])

plt.scatter(x_, y_, color='blue')

for i in range(len(camera["timestamp"]["0"])):
    x__.append(camera["timestamp"]["0"][i]["x"])
    y__.append(camera["timestamp"]["0"][i]["y"])

plt.scatter(x__, y__, color='green')

plt.show()
