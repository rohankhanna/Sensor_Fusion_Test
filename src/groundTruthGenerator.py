import json
from random import randint, randrange, uniform
import csv
from tqdm import tqdm


def readCameraConfig():
    with open('../config/cameraConfig.json') as json_data:
        cameraConfig = json.load(json_data)
        return cameraConfig


def readShortRangeRadarConfig():
    with open('../config/shortRangeRadarConfig.json') as json_data:
        shortRangeRadarConfig = json.load(json_data)
        return shortRangeRadarConfig


def readLongRangeRadarConfig():
    with open('../config/longRangeRadarConfig.json') as json_data:
        longRangeRadarConfig = json.load(json_data)
        return longRangeRadarConfig


def findMinMaxRanges(sensorConfigs):
    maxXvalue = -99999999
    minXvalue = 99999999
    maxYvalue = -99999999
    minYvalue = 99999999
    for config in sensorConfigs:
        if config["range"]["x"]["start"] > maxXvalue:
            maxXvalue = config["range"]["x"]["start"]
        if config["range"]["x"]["end"] > maxXvalue:
            maxXvalue = config["range"]["x"]["end"]
        if config["range"]["y"]["start"] > maxYvalue:
            maxYvalue = config["range"]["y"]["start"]
        if config["range"]["y"]["end"] > maxYvalue:
            maxYvalue = config["range"]["y"]["start"]

        if config["range"]["x"]["start"] < minXvalue:
            minXvalue = config["range"]["x"]["start"]
        if config["range"]["x"]["end"] < minXvalue:
            minXvalue = config["range"]["x"]["end"]
        if config["range"]["y"]["start"] < minYvalue:
            minYvalue = config["range"]["y"]["start"]
        if config["range"]["y"]["end"] < minYvalue:
            minYvalue = config["range"]["y"]["start"]

    return [maxXvalue, minXvalue, maxYvalue, minYvalue]


def inRangeOfSensor(config, x, y):
    if x <= config["range"]["x"]["end"] and \
            x >= config["range"]["x"]["start"] and \
            y <= config["range"]["y"]["end"] and \
            y >= config["range"]["y"]["start"]:
        return True
    return False


def pointVisibleToCameraAndAnotherSensor(sensorConfigs, xy):
    [cameraConfig, shortRangeRadarConfig, longRangeRadarConfig] = sensorConfigs
    [x, y] = xy

    if inRangeOfSensor(config=cameraConfig, x=x, y=y):
        if inRangeOfSensor(config=shortRangeRadarConfig, x=x, y=y) or inRangeOfSensor(config=longRangeRadarConfig, x=x, y=y):
            return True
    return False


def generateValidGroundTruthDataPoint(objId, sensorConfigs, minMaxRangeValues):
    [maxXvalue, minXvalue, maxYvalue, minYvalue] = minMaxRangeValues
    sensorDataSpec = {
        "objId": 0,
        "x": None,
        "y": None
    }

    while True:
        x = uniform(minXvalue, maxXvalue)
        y = uniform(minYvalue, maxYvalue)
        if pointVisibleToCameraAndAnotherSensor(sensorConfigs=sensorConfigs, xy=[x, y]):
            sensorDataSpec["objId"] = objId
            sensorDataSpec["x"] = x
            sensorDataSpec["y"] = y
            return sensorDataSpec


def generateGroundTruthData(sensorConfigs, minMaxRangeValues):
    tempStore = []
    randomRange = randint(0, 100)
    for objId in tqdm(range(randomRange)):
        tempStore.append(
            generateValidGroundTruthDataPoint(
                objId=objId,
                sensorConfigs=sensorConfigs,
                minMaxRangeValues=minMaxRangeValues
            )
        )
    return tempStore


def writeCSVtoFile(dictArray=[], filename="../dist/expectedOutputData.csv"):
    keys = dictArray[0].keys()
    with open(filename, "w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictArray)


def writeExpectedOutputData(expectedOutputData):
    writeCSVtoFile(dictArray=expectedOutputData,
                   filename="../dist/expectedOutputData.csv")


def timestamped(dataArray, timestamp):
    for item in dataArray:
        item["timestamp"] = timestamp
    return dataArray


def main():
    cameraConfig = readCameraConfig()
    shortRangeRadarConfig = readShortRangeRadarConfig()
    longRangeRadarConfig = readLongRangeRadarConfig()

    sensorConfigs = [cameraConfig, shortRangeRadarConfig, longRangeRadarConfig]

    minMaxRangeValues = findMinMaxRanges(
        sensorConfigs=sensorConfigs)

    groundTruthData = []
    step = 2
    number = 100
    for timestamp in range(0, number*step, step):

        tempGroundTruthStore = generateGroundTruthData(
            sensorConfigs=sensorConfigs,
            minMaxRangeValues=minMaxRangeValues)

        groundTruthData.extend(timestamped(
            dataArray=tempGroundTruthStore,
            timestamp=timestamp)
        )

        writeExpectedOutputData(expectedOutputData=groundTruthData)


main()
