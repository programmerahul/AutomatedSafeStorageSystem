import Adafruit_DHT
import requests
import socket
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
sensor = Adafruit_DHT.DHT11
pin = 4

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(ip_address)
endpoint_url = f'http://{ip_address}/device/'
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # true means nothing detected
    gases=GPIO.input(21)
    gases= not gases
    print(f"temp={temperature}, Humidity={humidity}, gases={gases}")
    status=1
    if(gases or humidity>90 or humidity<60 or temperature<0 or temperature>35)
        status=0
    data = {
    'name': 'Device 1',
    'temperature': temperature,
    'humidity': humidity,
    'toxicGases': gases,
    'status': status
    }
    requests.post(endpoint_url, json=data)
    sleep(10)




