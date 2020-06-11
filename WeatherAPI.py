import requests
import matplotlib.pyplot as plt

url = "https://community-open-weather-map.p.rapidapi.com/weather"

def getWeather(name):
    #Header for the request
    parameter = {
        'q' : name
    }
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "9fdbcc1e5amshbbc0ebc177d8fdbp16edaajsn3db21dafde28"
        }

    return requests.get( url, headers=headers, params=parameter).json()


name = input("Please enter the name of the city: ")
weather = getWeather(name)
print(weather)
weather = weather['main']
print("{:02d}".format(1))
temp = str(int(weather['temp'])- 273.150).strip("0")
print("Current temperature: "+ temp)
print("Feels like: " + str(int(weather['feels_like']) - 273.150))


# tempList = response["list"]
# temp = []
# feelsLike = []
# for i in tempList:
#     temp.append((i["temp"])["day"])
#     feelsLike.append((i["feels_like"])["day"])
#
#
# plt.plot(temp, color ='red', marker ='x')
# plt
# plt.plot(feelsLike, color ='blue', marker ='o')
#
# plt.ylabel('Temperature(Fahrenheit)')
# plt.xlabel('Day')
#
# plt.plot()
# plt.show()



