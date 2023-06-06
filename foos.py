import functools as fnt
import operator as op
from statistics import median


def evaluateAverages(temperatureFromSensor,humidityFromSensor,temperatureFromApi,humidityFromApi):
 
    avgTempSensor = (fnt.reduce(op.add, temperatureFromSensor))/len(temperatureFromSensor)

    avgTempApi = (fnt.reduce(op.add, temperatureFromApi))/len(temperatureFromApi)

    avgHumiditySensor = (fnt.reduce(op.add, humidityFromSensor))/len(humidityFromSensor)

    avgHumidityApi = (fnt.reduce(op.add, humidityFromApi))/len(humidityFromApi)

    averageTemperatureFromSensor = str(avgTempSensor) + " *C"
    averageHumidityFromSensor = str(avgHumiditySensor) + " %"
    averageTemperatureFromApi = str(avgTempApi) + " *C"
    averageHumidityFromApi = str(avgHumidityApi) + " %"
    
    return ({
            "averageTemperatureFromSensor" : averageTemperatureFromSensor,
            "averageHumidityFromSensor" : averageHumidityFromSensor,
            "averageTemperatureFromApi" : averageTemperatureFromApi,
            "averageHumidityFromApi" : averageHumidityFromApi
        })

def evaluateMinsAndMaxs(temperatureFromSensor,humidityFromSensor,temperatureFromApi ,humidityFromApi,axisX):
    
    maxTempSensor = max(temperatureFromSensor)
    maxTempSensorTime = axisX[temperatureFromSensor.index(maxTempSensor)]

    minTempSensor = min(temperatureFromSensor)
    minTempSensorTime = axisX[temperatureFromSensor.index(minTempSensor)]

    maxHumiditySensor = max(humidityFromSensor)
    maxHumiditySensorTime = axisX[humidityFromSensor.index(maxHumiditySensor)]

    minHumiditySensor = min(humidityFromSensor)
    minHumiditySensorTime = axisX[humidityFromSensor.index(minHumiditySensor)]

    maxTempApi = max(temperatureFromApi)
    maxTempApiTime = axisX[temperatureFromApi.index(maxTempApi)]

    minTempApi = min(temperatureFromApi)
    minTempApiTime = axisX[temperatureFromApi.index(minTempApi)]

    maxHumidityApi = max(humidityFromApi)
    maxHumidityApiTime = axisX[humidityFromApi.index(maxHumidityApi)]

    minHumidityApi = min(humidityFromApi)
    minHumidityApiTime = axisX[humidityFromApi.index(minHumidityApi)]

    return ({
        'maxTempSensor' : {
            'value' : maxTempSensor,
            'time' : maxTempSensorTime
        },
        'minTempSensor' : {
            'value' : minTempSensor,
            'time' : minTempSensorTime
        },
        'maxHumiditySensor' : {
            'value' : maxHumiditySensor,
            'time' : maxHumiditySensorTime
        },
        'minHumiditySensor' : {
            'value' : minHumiditySensor,
            'time' : minHumiditySensorTime
        },
        'maxTempApi' : {
            'value' : maxTempApi,
            'time' : maxTempApiTime
        },
        'minTempApi' : {
            'value' : minTempApi,
            'time' : minTempApiTime
        },
        'maxHumidityApi' : {
            'value' : maxHumidityApi,
            'time' : maxHumidityApiTime
        },
        'minHumidityApi' : {
            'value' : minHumidityApi,
            'time' : minHumidityApiTime
        }
    })

def medians(tempSensor, humidSensor, tempApi ,humidApi): 

    medianFromTempSensor = median(tempSensor)
    medianFromHumidSensor = median(humidSensor)
    medianFromTempApi = median(tempApi)
    medianFromHumidApi = median(humidApi)

    return ({
        'medianTempSensor' : medianFromTempSensor,
        'medianHumidSensor' : medianFromHumidSensor,
        'medianTempApi' : medianFromTempApi,
        'medianHumidApi' : medianFromHumidApi
    })

def changeToNum(arr):
    return [int(i) for i in arr]


def evaluateStatistics (arrTemp, arrHumid, arrApiTemp, arrApiHumid, axisX):

    averages = evaluateAverages(arrTemp, arrHumid, arrApiTemp, arrApiHumid)

    minAndMax = evaluateMinsAndMaxs(arrTemp, arrHumid, arrApiTemp, arrApiHumid, axisX)

    allMedians = medians(arrTemp, arrHumid, arrApiTemp, arrApiHumid)

    return [
        averages,
        minAndMax,
        allMedians
    ]

