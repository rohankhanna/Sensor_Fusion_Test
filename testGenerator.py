#!/usr/bin/env python3

import json
from random import randint, randrange, uniform
import csv


def readCameraConfig():
    cameraConfig = []
    with open('cameraConfig.json') as json_data:
        cameraConfig = json.load(json_data)
        return cameraConfig


def readShortRangeRadarConfig():
    shortRangeRadarConfig = []
    with open('shortRangeRadarConfig.json') as json_data:
        shortRangeRadarConfig = json.load(json_data)
        return shortRangeRadarConfig


def readLongRangeRadarConfig():
    longRangeRadarConfig = []
    with open('longRangeRadarConfig.json') as json_data:
        longRangeRadarConfig = json.load(json_data)
        return longRangeRadarConfig


cameraConfig = readCameraConfig()
shortRangeRadarConfig = readShortRangeRadarConfig()
longRangeRadarConfig = readLongRangeRadarConfig()


def appendRandomNoiseCameraData(cameraData, timestamp):
    global cameraConfig
    cameraDataSpec = {
        "objId": 0,
        "x": None,
        "y": None,
        "timestamp": 0
    }
    objId = len(cameraData)-1
    for index in range(100):
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
    objId = len(shortRangeRadarData)
    for index in range(100):
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
    # print(shortRangeRadarData[-1])
    # print(shortRangeRadarConfig)
    return shortRangeRadarData


def appendRandomNoiseLongRangeRadarData(longRangeRadarData, timestamp):
    global longRangeRadarConfig
    longRangeRadarDataSpec = {
        "objId": 0,
        "x": None,
        "y": None,
        "timestamp": 0
    }
    objId = len(longRangeRadarData)
    for index in range(100):
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
    # print(longRangeRadarData[-1])
    # print(longRangeRadarConfig)
    return longRangeRadarData


def writeDictArrayToCSV(dictArray=[], filename="data.csv"):
    keys = dictArray[0].keys()
    with open(filename, "w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictArray)


def writeCameraData(cameraData):
    writeDictArrayToCSV(dictArray=cameraData,
                        filename="cameraData.csv")


def writeShortRangeRadarData(shortRangeRadarData):
    writeDictArrayToCSV(dictArray=shortRangeRadarData,
                        filename="shortRangeRadarData.csv")


def writeLongRangeRadarData(longRangeRadarData):
    writeDictArrayToCSV(dictArray=longRangeRadarData,
                        filename="longRangeRadarData.csv")


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
