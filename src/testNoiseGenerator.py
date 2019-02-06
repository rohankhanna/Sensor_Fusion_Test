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
        "y": None
    }
    tempStore = []
    randomRange = randint(0, 100)
    for fakeObjId in range(randomRange):
        tempStore.append(cameraDataSpec.copy())
        x = uniform(cameraConfig["range"]["x"]["start"], cameraConfig["range"]["x"]["end"]) + \
            uniform(-cameraConfig["tolerance"],
                    cameraConfig["tolerance"])
        y = uniform(cameraConfig["range"]["y"]["start"], cameraConfig["range"]["y"]["end"]) + \
            uniform(-cameraConfig["tolerance"],
                    cameraConfig["tolerance"])

        tempStore[-1]["objId"] = fakeObjId
        tempStore[-1]["x"] = x
        tempStore[-1]["y"] = y
    cameraData["timestamp"][timestamp] = tempStore
    return cameraData


def appendRandomNoiseShortRangeRadarData(shortRangeRadarData, timestamp):
    global shortRangeRadarConfig
    shortRangeRadarDataSpec = {
        "objId": 0,
        "x": None,
        "y": None
    }
    tempStore = []
    randomRange = randint(0, 100)
    for fakeObjId in range(randomRange):
        tempStore.append(shortRangeRadarDataSpec.copy())
        x = uniform(shortRangeRadarConfig["range"]["x"]["start"], shortRangeRadarConfig["range"]["x"]["end"]) + \
            uniform(-shortRangeRadarConfig["tolerance"],
                    shortRangeRadarConfig["tolerance"])
        y = uniform(shortRangeRadarConfig["range"]["y"]["start"], shortRangeRadarConfig["range"]["y"]["end"]) + \
            uniform(-shortRangeRadarConfig["tolerance"],
                    shortRangeRadarConfig["tolerance"])

        tempStore[-1]["objId"] = fakeObjId
        tempStore[-1]["x"] = x
        tempStore[-1]["y"] = y
    shortRangeRadarData["timestamp"][timestamp] = tempStore
    return shortRangeRadarData


def appendRandomNoiseLongRangeRadarData(longRangeRadarData, timestamp):
    global longRangeRadarConfig
    longRangeRadarDataSpec = {
        "objId": 0,
        "x": None,
        "y": None
    }
    tempStore = []
    randomRange = randint(0, 100)
    for fakeObjId in range(randomRange):
        tempStore.append(longRangeRadarDataSpec.copy())
        x = uniform(longRangeRadarConfig["range"]["x"]["start"], longRangeRadarConfig["range"]["x"]["end"]) + \
            uniform(-longRangeRadarConfig["tolerance"],
                    longRangeRadarConfig["tolerance"])
        y = uniform(longRangeRadarConfig["range"]["y"]["start"], longRangeRadarConfig["range"]["y"]["end"]) + \
            uniform(-longRangeRadarConfig["tolerance"],
                    longRangeRadarConfig["tolerance"])

        tempStore[-1]["objId"] = fakeObjId
        tempStore[-1]["x"] = x
        tempStore[-1]["y"] = y

    longRangeRadarData["timestamp"][timestamp] = tempStore
    return longRangeRadarData


def writeJSONtoFile(JSONdata, filename="../dist/data.csv"):
    with open(filename, 'w') as outfile:
        json.dump(JSONdata, outfile)


def writeCameraData(cameraData):
    writeJSONtoFile(JSONdata=cameraData,
                    filename="../dist/cameraData.json")


def writeShortRangeRadarData(shortRangeRadarData):
    writeJSONtoFile(JSONdata=shortRangeRadarData,
                    filename="../dist/shortRangeRadarData.json")


def writeLongRangeRadarData(longRangeRadarData):
    writeJSONtoFile(JSONdata=longRangeRadarData,
                    filename="../dist/longRangeRadarData.json")





def addGlobalNoise(epochs=200):
    timestamp = 0
    cameraData = {"timestamp": {}}
    shortRangeRadarData = {"timestamp": {}}
    longRangeRadarData = {"timestamp": {}}

    for _ in range(4):
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
