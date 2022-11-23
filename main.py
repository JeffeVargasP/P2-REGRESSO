import requests
import urllib
import Adafruit_DHT as dht
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)

verde = 38
vermelho = 40
GPIO.setup(verde, GPIO.OUT)
GPIO.setup(vermelho, GPIO.OUT)

apikey = "MOKFKD5ZDAMEY2IN"

sensor = dht.DHT11
pin = 17

def gerar():
    umid, temp = dht.read_retry(sensor, pin)
    print(f'Umidade: {umid}%')
    print(f'Temperatura: {temp}°C')
    print('- '*50)
    req = "https://api.thingspeak.com/update?api_key="+apikey+"&field1="+str(temp)+"&field2="+str(umid)
    try:
        requests.get(req)
    except:
        print("Error")
    finally:
        if umid >= 40:
            GPIO.output(verde, True)
            GPIO.output(vermelho, False)
        else:
            GPIO.output(verde, False)
            GPIO.output(vermelho, True)
    
    return umid, temp

while True:
    try:
        gerar()
    except:
        print("Erro")