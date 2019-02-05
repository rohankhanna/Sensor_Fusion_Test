import json
from random import randint, randrange, uniform
import csv
from tqdm import tqdm
import math


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


def visibleTo(listOfDicts, config):
    index = 0
    for item in listOfDicts:
        if not (
            item["x"] <= config["range"]["x"]["end"] and
            item["x"] >= config["range"]["x"]["start"] and
            item["y"] <= config["range"]["y"]["end"] and
            item["y"] >= config["range"]["y"]["start"]
        ):
            del listOfDicts[index]
        else:
            index = index+1
    return listOfDicts


def writeDictArraytoCSVFile(dictArray=[], filename="../dist/expectedOutputData.csv"):
    keys = dictArray[0].keys()
    with open(filename, "w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictArray)


def writeCameraData(cameraData):
    writeDictArraytoCSVFile(dictArray=cameraData,
                            filename="../dist/cameraDataExpectedInput.csv")


def writeShortRangeRadarData(shortRangeRadarData):
    writeDictArraytoCSVFile(dictArray=shortRangeRadarData,
                            filename="../dist/shortRangeRadarDataExpectedInput.csv")


def writeLongRangeRadarData(longRangeRadarData):
    writeDictArraytoCSVFile(dictArray=longRangeRadarData,
                            filename="../dist/longRangeRadarDataExpectedInput.csv")


def readGroundTruthDataCSV(fileName="../dist/expectedOutputData.csv"):
    with open(fileName) as file:
        listOfDicts = [{k: float(v) for k, v in row.items()}
                       for row in csv.DictReader(file, skipinitialspace=True)]
        return listOfDicts
    pass


def getGroundTruthDataAtTimestamp(groundTruthData, timestamp):
    returnable = []
    for item in groundTruthData:
        if item.timestamp == timestamp:
            returnable.append(item)
    return returnable


def inRangeOfSensor(sensorConfig, x, y):
    if x <= sensorConfig["range"]["x"]["end"] and \
            x >= sensorConfig["range"]["x"]["start"] and \
            y <= sensorConfig["range"]["y"]["end"] and \
            y >= sensorConfig["range"]["y"]["start"]:
        return True
    return False


def noised(point, threshold, sensorConfig):
    dx = 0
    dy = 0
    while True:
        dx = uniform(-threshold/2, threshold/2)
        dy = uniform(-threshold/2, threshold/2)
        if (((dx*dx) + (dy*dy)) <= ((threshold/2)*(threshold/2)) and
                inRangeOfSensor(
                x=point["x"] + dx,
                y=point["y"] + dy,
                sensorConfig=sensorConfig)):
            break
    point["x"] = point["x"] + dx
    point["y"] = point["y"] + dy
    return point


def individualPointsNoised(groundTruthData, threshold, sensorConfig):
    returnable = []
    for point in groundTruthData:
        returnable.append(
            noised(
                point=point,
                threshold=threshold,
                sensorConfig=sensorConfig))
    return returnable


def main():
    cameraConfig = readCameraConfig()
    shortRangeRadarConfig = readShortRangeRadarConfig()
    longRangeRadarConfig = readLongRangeRadarConfig()
    threshold = 0.1
    groundTruthData = readGroundTruthDataCSV(
        fileName="../dist/expectedOutputData.csv")
    expectedInputDataCamera = []

    expectedInputDataShortRangeRadar = []
    expectedInputDataLongRangeRadar = []
    for timestamp in range(0, 4, 2):
        tempGroundTruthStore = getGroundTruthDataAtTimestamp(
            groundTruthData=groundTruthData, timestamp=timestamp)
        # add noise to individual Point readings
        expectedInputDataCamera.extend(
            individualPointsNoised(sensorConfig=cameraConfig,
                                   groundTruthData=visibleTo(
                                       listOfDicts=tempGroundTruthStore,
                                       config=cameraConfig),
                                   threshold=threshold))
        expectedInputDataShortRangeRadar.extend(
            individualPointsNoised(sensorConfig=shortRangeRadarConfig,
                                   groundTruthData=visibleTo(
                                       listOfDicts=tempGroundTruthStore,
                                       config=shortRangeRadarConfig),
                                   threshold=threshold))
        expectedInputDataLongRangeRadar.extend(
            individualPointsNoised(sensorConfig=longRangeRadarConfig,
                                   groundTruthData=visibleTo(
                                       listOfDicts=tempGroundTruthStore,
                                       config=longRangeRadarConfig),
                                   threshold=threshold))
        # add noise to sensor ranges that have no areas in common
        expectedInputDataCamera.extend()
        expectedInputDataShortRangeRadar.extend()
        expectedInputDataLongRangeRadar.extend()

        # tempNoiseStore=generateRandomNoiseData(
        #     sensorConfigs=[cameraConfig,
        #                    shortRangeRadarConfig,
        #                    longRangeRadarConfig]
        #     minMaxRangeValues=minMaxRangeValues)
        # expectedInputDataCamera=mergeData(timestamp=timestamp,
        #                                     sensorData=noised(
        #                                         JSONdata=visibleTo(JSONdata=expectedInputDataCamera, config=cameraConfig), config=cameraConfig),
        #                                     toMergeWith=tempNoiseStore)
        # expectedInputDataShortRangeRadar=mergeData(timestamp=timestamp,
        #                                              sensorData=noised(
        #                                                  JSONdata=visibleTo(JSONdata=expectedInputDataShortRangeRadar, config=shortRangeRadarConfig), config=shortRangeRadarConfig),
        #                                              toMergeWith=tempNoiseStore)
        # expectedInputDataLongRangeRadar=mergeData(timestamp=timestamp,
        #                                             sensorData=noised(
        #                                                 JSONdata=visibleTo(JSONdata=expectedInputDataLongRangeRadar, config=longRangeRadarConfig), config=cameraConfig),
        #                                             toMergeWith=tempNoiseStore)
        # writeExpectedOutputData(expectedOutputData=groundTruthData)
        # writeCameraData(
        #     cameraData=expectedInputDataCamera)
        # writeShortRangeRadarData(
        #     shortRangeRadarData=expectedInputDataShortRangeRadar)
        # writeLongRangeRadarData(
        #     longRangeRadarData=expectedInputDataLongRangeRadar)
    writeCameraData(expectedInputDataCamera)
    writeShortRangeRadarData(expectedInputDataShortRangeRadar)
    writeLongRangeRadarData(expectedInputDataLongRangeRadar)


main()
