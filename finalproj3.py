import board
import adafruit_dht
import time
import psutil
from datetime import datetime 
import requests, json
import tkinter as tk
from foos import changeToNum, evaluateStatistics
from charts import plotChartsFromResults

#takes actual date for first mesure
actualTime = datetime.now().strftime("%H:%M:%S")
#keep data from sensor in arrays
arrTemp = []
arrHumid = []
#keep date in array
axisX = []
#keep data from weather api in arrays
arrApiTemp = []
arrApiHumid =[]
#initial condition - y(0) = 0
y = 0

#creating GUI to enter data to program
win = tk.Tk()
win.title('Temperature and humidity entry sheet')
tk.Label(win, text = 'Enter time of measurment[s]:').grid(row = 0)
tk.Label(win, text = 'Enter interval[s]:').grid(row = 1)
tk.Label(win, text = 'Enter city name:').grid(row = 2)
tk.Label(win, text = 'Enter thermal transmittance[W/m^2*K]:').grid(row = 3)
tk.Label(win, text = 'Enter the building area[m^2]:').grid(row = 4)

eTime = tk.Entry(win)
eInterval = tk.Entry(win)
eCity = tk.Entry(win)
eTransm = tk.Entry(win)
eArea = tk.Entry(win)

eTime.grid(row = 0, column = 1)
eInterval.grid(row = 1, column = 1)
eCity.grid(row = 2, column = 1)
eTransm.grid(row = 3, column = 1)
eArea.grid(row = 4, column = 1)


tk.Button(win, text='Save data', command=win.quit).grid(row=5, column=2, sticky=tk.W, pady=4)

win.mainloop()


city_name = eCity.get()

#chart of lose or receive warm
arrOfHeatFlow = []
surfaceArea = float(eArea.get()) # [m^2]
thermalTransmittanceCoefficient = float(eTransm.get()) # [W/m^2*K]

# if heatFlow is positive number the heat is taken from facility, when negative - facility takes a heat
def evaluateHeatFlow (tempIn,tempOut) :
    return surfaceArea * thermalTransmittanceCoefficient * (int(tempIn) - int(tempOut))


# userInputOfTimeInterval is variable that describes how long are intervals between measures (in seconds)
# userInputOfSecondsToMeasure is variable that describes how long will last whole measure, so if we divide userInputOfSecondsToMeasure,
# through userInputOfTimeInterval we recive numbers that sensor will take a measure
userInputOfSecondsToMeasure = int(eTime.get())
userInputOfTimeInterval = int(eInterval.get())
arraysLength = userInputOfSecondsToMeasure/userInputOfTimeInterval

#give information about correct measure
ctr = 0 

# function that takes data (humidity and temperature) from API server and return it as an array,
# or if there's a problem return none
def apiFunc():
    api_key = "44daa64a42d066212e1a93a720402e19"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #name of city where we are and where we take a measure by sensor
    #city_name = 'Kraków'
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = round(y["temp"]-273)
        current_humidity = y["humidity"]
        return [current_temperature, current_humidity]
    else:
        print(" City Not Found ")
        return None


#def evaluateData(arrTemperatureSensor,arrHumiditySensor,arrTemperatureApi,arrHumidityApi):

    #must have
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
            
# set sensor on GPIO11 pin
sensor = adafruit_dht.DHT11(board.D11)

# take a series of measures
while (len(arrTemp) < arraysLength ):
    isError = False

    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        arrayFromApi = apiFunc()
        apiTemp = arrayFromApi[0]
        apiHumidity = arrayFromApi[1]
        if (temp and humidity and apiTemp and apiHumidity):
            arrTemp.append(temp)
            arrHumid.append(humidity)
            arrApiTemp.append(apiTemp)
            arrApiHumid.append(apiHumidity)
            #TODO
            heatFlow = evaluateHeatFlow(temp,apiTemp)
            arrOfHeatFlow.append(heatFlow)

            axisX.append(datetime.now().strftime("%H:%M:%S"))
            y += 1
            ctr += 1
        else :
            isError = True
        #print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1)
        continue

    except Exception as error:
        sensor.exit()
        raise error

    if (isError == False and ctr != arraysLength):
        time.sleep(userInputOfTimeInterval)

arrTemp = changeToNum(arrTemp)
arrHumid = changeToNum(arrHumid)
arrApiTemp = changeToNum(arrApiTemp)
arrApiHumid = changeToNum(arrApiHumid)

statistics = evaluateStatistics (arrTemp, arrHumid, arrApiTemp, arrApiHumid, axisX)

print(statistics)

maxTempSensorTime = statistics[1]['maxTempSensor']['time']
maxTempSensor = statistics[1]['maxTempSensor']['value']
minTempSensorTime = statistics[1]['minTempSensor']['time']
minTempSensor = statistics[1]['minTempSensor']['value']
maxTempApiTime = statistics[1]['maxTempApi']['time']
maxTempApi = statistics[1]['maxTempApi']['value']
minTempApiTime = statistics[1]['minTempApi']['time']
minTempApi = statistics[1]['minTempApi']['value']

maxHumidSensorTime = statistics[1]['maxHumiditySensor']['time']
maxHumidSensor = statistics[1]['maxHumiditySensor']['value']
minHumidSensorTime = statistics[1]['minHumiditySensor']['time']
minHumidSensor = statistics[1]['minHumiditySensor']['value']
maxHumidApiTime = statistics[1]['maxHumidityApi']['time']
maxHumidApi = statistics[1]['maxHumidityApi']['value']
minHumidApiTime = statistics[1]['minHumidityApi']['time']
minHumidApi = statistics[1]['minHumidityApi']['value']

plotChartsFromResults(axisX,
                      arrTemp,
                      arrApiTemp,
                      arrHumid,
                      arrApiHumid,
                      arrOfHeatFlow,
                      maxTempSensorTime,
                      maxTempSensor,
                      minTempSensorTime,
                      minTempSensor,
                      maxTempApiTime,
                      maxTempApi,
                      minTempApiTime,
                      minTempApi,
                      maxHumidSensorTime,
                      maxHumidSensor,
                      minHumidSensorTime,
                      minHumidSensor,
                      maxHumidApiTime,
                      maxHumidApi,
                      minHumidApiTime,
                      minHumidApi)


