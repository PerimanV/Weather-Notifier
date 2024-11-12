import requests 
from bs4 import BeautifulSoup 
from win10toast import ToastNotifier 

notif = ToastNotifier()

# Function to extract weather details
def getdata(url):
    req = requests.get(url)
    return req.text

htmldata = getdata("https://weather.com/en-IN/weather/today/l/0c0cd1894621dea8970a34f1357a8034195642c40915b82b936c2a08988f353c")

soup = BeautifulSoup(htmldata, 'html.parser') 

print(soup.prettify()) 

# Extract temperature and rain chance text
temp_element = soup.find("span", class_="CurrentConditions--tempValue--zUBSz")
rain_element = soup.find("span", class_="Column--precip--YkErk")


#Check for errors 
if temp_element.text:
    current_temp = temp_element.text
else:
    current_temp = "N/A"

if rain_element.text:
    chances_rain = rain_element.text
else:
    chances_rain = "N/A"


#Result string
result = f"current temp {current_temp} in Athens\n{chances_rain}"

#Toast Notification
notif.show_toast("Weather Update", result, duration=10)
