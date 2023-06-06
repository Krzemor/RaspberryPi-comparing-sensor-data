import matplotlib.pyplot as plt

#plots
def plotChartsFromResults(axisX,
                          arrTemp,
                          arrApiTemp,
                          arrHumid,
                          arrApiHumid,
                          arrOfHeatFlow,
                          timeTempSensorMax,
                          sensorTempMax,
                          timeSensorTempMin,
                          sensorTempMin,
                          timeApiTempMax,
                          apiTempMax,
                          timeApiTempMin,
                          apiTempMin,
                          timeHumidSensorMax,
                          sensorHumidMax,
                          timeHumidSensorMin,
                          sensorHumidMin,
                          timeApiHumidMax,
                          apiHumidMax,
                          timeApiHumidMin,
                          apiHumidMin):
    
    fig, axs = plt.subplots(3)
    
    axs[0].plot(axisX, arrTemp)
    axs[0].plot(axisX, arrApiTemp)
    axs[0].plot(timeTempSensorMax, sensorTempMax, marker = '.', markersize = 10)
    axs[0].plot(timeSensorTempMin, sensorTempMin, marker = '*', markersize = 7)
    axs[0].plot(timeApiTempMax, apiTempMax, marker = '.', markersize = 10)
    axs[0].plot(timeApiTempMin, apiTempMin, marker = '*', markersize = 7)
    axs[0].set_ylabel('T[°C]')
    axs[0].legend(['sensor', 'api'])
    
    axs[1].plot(axisX, arrHumid)
    axs[1].plot(axisX, arrApiHumid)
    axs[1].plot(timeHumidSensorMax, sensorHumidMax, marker = '.', markersize = 10)
    axs[1].plot(timeHumidSensorMin, sensorHumidMin, marker = '*', markersize = 7)
    axs[1].plot(timeApiHumidMax, apiHumidMax, marker = '.', markersize = 10)
    axs[1].plot(timeApiHumidMin, apiHumidMin, marker = '*', markersize = 7)
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Humidity[%]')
    axs[1].legend(['sensor', 'api'])
    
    axs[2].plot(axisX, arrOfHeatFlow)
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('Heat flow[W]')
    plt.show() 
