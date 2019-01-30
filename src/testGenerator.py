#!/usr/bin/env python3

import json
from random import randint, randrange, uniform
import csv


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


def appendRandomNoiseCameraData(cameraData, timestamp):
    global cameraConfig
    cameraDataSpec = {
        "objId": 0,
        "x": None,
        "y": None,
        "timestamp": 0
    }
    objId = len(cameraData) - 1
    randomRange = randint(0, 100)
    print(randomRange)
    for index in range(randomRange):
        cameraData.append(cameraDataSpec.copy())
        objId = objId+1
        x = uniform(cameraConfig["range"]["x"]["start"], cameraConfig["range"]["x"]["end"]) + \
            uniform(-cameraConfig["tolerance"],
                    cameraConfig["tolerance"])
        y = uniform(cameraConfig["range"]["y"]["start"], cameraConfig["range"]["y"]["end"]) + \
            uniform(-cameraConfig["tolerance"],
                    cameraConfig["tolerance"])

        cameraData[-1]["objId"] = objId
        cameraData[-1]["x"] = x
        cameraData[-1]["y"] = y
        cameraData[-1]["timestamp"] = timestamp
    return cameraData


def appendRandomNoiseShortRangeRadarData(shortRangeRadarData, timestamp):
    global shortRangeRadarConfig
    shortRangeRadarDataSpec = {
        "objId": 0,
        "x": None,
        "y": None,
        "timestamp": 0
    }
    objId = len(shortRangeRadarData) - 1
    randomRange = randint(0, 100)
    for index in range(randomRange):
        shortRangeRadarData.append(shortRangeRadarDataSpec.copy())
        objId = objId+1
        x = uniform(shortRangeRadarConfig["range"]["x"]["start"], shortRangeRadarConfig["range"]["x"]["end"]) + \
            uniform(-shortRangeRadarConfig["tolerance"],
                    shortRangeRadarConfig["tolerance"])
        y = uniform(shortRangeRadarConfig["range"]["y"]["start"], shortRangeRadarConfig["range"]["y"]["end"]) + \
            uniform(-shortRangeRadarConfig["tolerance"],
                    shortRangeRadarConfig["tolerance"])

        shortRangeRadarData[-1]["objId"] = objId
        shortRangeRadarData[-1]["x"] = x
        shortRangeRadarData[-1]["y"] = y
        shortRangeRadarData[-1]["timestamp"] = timestamp
    return shortRangeRadarData


def appendRandomNoiseLongRangeRadarData(longRangeRadarData, timestamp):
    global longRangeRadarConfig
    longRangeRadarDataSpec = {
        "objId": 0,
        "x": None,
        "y": None,
        "timestamp": 0
    }
    objId = len(longRangeRadarData) - 1
    randomRange = randint(0, 100)
    for index in range(randomRange):
        longRangeRadarData.append(longRangeRadarDataSpec.copy())
        objId = objId+1
        x = uniform(longRangeRadarConfig["range"]["x"]["start"], longRangeRadarConfig["range"]["x"]["end"]) + \
            uniform(-longRangeRadarConfig["tolerance"],
                    longRangeRadarConfig["tolerance"])
        y = uniform(longRangeRadarConfig["range"]["y"]["start"], longRangeRadarConfig["range"]["y"]["end"]) + \
            uniform(-longRangeRadarConfig["tolerance"],
                    longRangeRadarConfig["tolerance"])

        longRangeRadarData[-1]["objId"] = objId
        longRangeRadarData[-1]["x"] = x
        longRangeRadarData[-1]["y"] = y
        longRangeRadarData[-1]["timestamp"] = timestamp
    return longRangeRadarData


def writeDictArrayToCSV(dictArray=[], filename="../dist/data.csv"):
    keys = dictArray[0].keys()
    with open(filename, "w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictArray)


def writeCameraData(cameraData):
    writeDictArrayToCSV(dictArray=cameraData,
                        filename="../dist/cameraData.csv")


def writeShortRangeRadarData(shortRangeRadarData):
    writeDictArrayToCSV(dictArray=shortRangeRadarData,
                        filename="../dist/shortRangeRadarData.csv")


def writeLongRangeRadarData(longRangeRadarData):
    writeDictArrayToCSV(dictArray=longRangeRadarData,
                        filename="../dist/longRangeRadarData.csv")


def generateRandomGroundTruthData(epochs=200):
    pass


def addGlobalNoise(epochs=200):
    timestamp = 0
    cameraData = []
    shortRangeRadarData = []
    longRangeRadarData = []

    for _ in range(200):
        timestamp = timestamp+2
        cameraData = appendRandomNoiseCameraData(
            cameraData=cameraData, timestamp=timestamp)
        shortRangeRadarData = appendRandomNoiseShortRangeRadarData(
            shortRangeRadarData=shortRangeRadarData, timestamp=timestamp)
        longRangeRadarData = appendRandomNoiseLongRangeRadarData(
            longRangeRadarData=longRangeRadarData, timestamp=timestamp)

    writeCameraData(cameraData=cameraData)
    writeShortRangeRadarData(shortRangeRadarData=shortRangeRadarData)
    writeLongRangeRadarData(longRangeRadarData=longRangeRadarData)


cameraConfig = []
shortRangeRadarConfig = []
longRangeRadarConfig = []


def main():
    global cameraConfig
    global shortRangeRadarConfig
    global longRangeRadarConfig

    cameraConfig = readCameraConfig()
    shortRangeRadarConfig = readShortRangeRadarConfig()
    longRangeRadarConfig = readLongRangeRadarConfig()
    addGlobalNoise(epochs=200)


main()
