#!/usr/bin/env python3

import json
from random import randrange, uniform
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


def generateCameraData():
    global cameraConfig
    cameraDataSpec = {
        "objId": 0,
        "x": None,
        "y": None
    }
    cameraData = []
    for index in range(100):
        cameraData.append(cameraDataSpec.copy())
        objId = index
        x = uniform(cameraConfig["range"]["x"]["start"], cameraConfig["range"]["x"]["end"]) + \
            uniform(-cameraConfig["tolerance"], cameraConfig["tolerance"])
        y = uniform(cameraConfig["range"]["y"]["start"], cameraConfig["range"]["y"]["end"]) + \
            uniform(-cameraConfig["tolerance"], cameraConfig["tolerance"])

        cameraData[index]["objId"] = objId
        cameraData[index]["x"] = x
        cameraData[index]["y"] = y
    return cameraData


def generateShortRangeRadarData():
    global shortRangeRadarConfig
    shortRangeRadarDataSpec = {
        "objId": 0,
        "x": None,
        "y": None
    }
    shortRangeRadarData = []
    for index in range(100):
        shortRangeRadarData.append(shortRangeRadarDataSpec.copy())
        objId = index
        x = uniform(shortRangeRadarConfig["range"]["x"]["start"], shortRangeRadarConfig["range"]["x"]["end"]) + \
            uniform(-shortRangeRadarConfig["tolerance"],
                    shortRangeRadarConfig["tolerance"])
        y = uniform(shortRangeRadarConfig["range"]["y"]["start"], shortRangeRadarConfig["range"]["y"]["end"]) + \
            uniform(-shortRangeRadarConfig["tolerance"],
                    shortRangeRadarConfig["tolerance"])

        shortRangeRadarData[index]["objId"] = objId
        shortRangeRadarData[index]["x"] = x
        shortRangeRadarData[index]["y"] = y
    return shortRangeRadarData


def generateLongRangeRadarData():
    global longRangeRadarConfig
    longRangeRadarDataSpec = {
        "objId": 0,
        "x": None,
        "y": None
    }
    longRangeRadarData = []
    for index in range(100):
        longRangeRadarData.append(longRangeRadarDataSpec.copy())
        objId = index
        x = uniform(longRangeRadarConfig["range"]["x"]["start"], longRangeRadarConfig["range"]["x"]["end"]) + \
            uniform(-longRangeRadarConfig["tolerance"],
                    longRangeRadarConfig["tolerance"])
        y = uniform(longRangeRadarConfig["range"]["y"]["start"], longRangeRadarConfig["range"]["y"]["end"]) + \
            uniform(-longRangeRadarConfig["tolerance"],
                    longRangeRadarConfig["tolerance"])

        longRangeRadarData[index]["objId"] = objId
        longRangeRadarData[index]["x"] = x
        longRangeRadarData[index]["y"] = y
    return longRangeRadarData


def writeDictArrayToCSV(dictArray=[], filename="data.csv"):
    keys = dictArray[0].keys()
    with open(filename, "w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictArray)


def writeCameraData():
    cameraData = generateCameraData()
    writeDictArrayToCSV(dictArray=cameraData, filename="cameraData.csv")


def writeShortRangeRadarData():
    shortRangeRadarData = generateShortRangeRadarData()
    writeDictArrayToCSV(dictArray=shortRangeRadarData,
                        filename="shortRangeRadarData.csv")


def writeLongRangeRadarData():
    longRangeRadarData = generateLongRangeRadarData()
    writeDictArrayToCSV(dictArray=longRangeRadarData,
                        filename="longRangeRadarData.csv")


writeCameraData()
writeShortRangeRadarData()
writeLongRangeRadarData()
