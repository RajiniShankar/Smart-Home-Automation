import RPi.GPIO as GPIO
import requests, json, signal, sys

LDR_OUT = 4

def setupPin(gpioPin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpioPin, GPIO.OUT)
    GPIO.setup(LDR_OUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(LDR_OUT, GPIO.BOTH, callback=sensorCallback, bouncetime=3000)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def setPinStatus(gpioPin, status):
    try:
        if status:
            GPIO.output(gpioPin, GPIO.LOW)
        else:
            GPIO.output(gpioPin, GPIO.HIGH)
    except Error:
        resetPinStatus(gpioPin)

def resetPinStatus(gpioPin):
    GPIO.setup(gpioPin, GPIO.OUT)
    GPIO.output(gpioPin, GPIO.HIGH)

    GPIO.cleanup()

def getDevicesList():
    url = "http://127.0.0.1:8000/devices"
    headers = {
        'content-type': "application/json"
    }
    data = {}    
    payload = json.dumps(data)
    response = requests.request("GET", url, headers=headers, params=data)
    return json.loads(response.text)

def sensorCallback(channel):
    devices = getDevicesList()

    for device in devices:
        if GPIO.input(LDR_OUT):
            GPIO.output(int(device['id']), GPIO.LOW)
        else:
            GPIO.output(int(device['id']), GPIO.HIGH)