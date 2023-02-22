from machine import ADC, Pin
import time
import random
import utime as tn
import network   
import urequests 


wlan = network.WLAN(network.STA_IF)
wlan.active(True)


ssid = 'ENTER SSID'
password = 'ENTER PASSWORD'
wlan.connect(ssid, password)


potentiometer = ADC(Pin(27))

button1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
onboardLED = Pin(25, Pin.OUT)

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)
reading = 0
finalTime = 0
date = '2022-12-8'
Dtime = '12:12:12'

def off():
    red.value(0)
    amber.value(0)
    green.value(0)
    onboardLED.value(0)
    
def on():
    red.value(1)
    amber.value(1)
    green.value(1)
    onboardLED.value(1)

def flash():
    for x in range(1,-1,-1):
        red.value(x)
        amber.value(x)
        green.value(x)
        onboardLED.value(x)
        time.sleep(0.2)



def easy():
    mode = "easy"
    flash()
    time.sleep(1)
    onboardLED.value(1)
    seedT = random.randint(30,51)
    seedT = seedT/12
    time.sleep(seedT)
    x = 0
    startTime = time.ticks_ms()
    on()
    while x == 0:
        if button1.value() == 1 or button2.value() == 1 or button3.value() == 1:
            x = 1
            onboardLED.value(0)
            endTime = time.ticks_ms()
    time.sleep(0.1)
    finalTime = endTime - startTime
    if finalTime == 0:
        print("Button held \n \n")
    else:
        print("Your time was: ", finalTime, "\n \n")
        finalTime = str(finalTime)
        r = urequests.get('http://ENTERURL/api/rtime.php?date='+date+'&time='+Dtime+'&mode='+mode+'&reaction='+finalTime).text
        print(r)
    time.sleep(0.5)
            


def mid():
    mode = "mid"
    flash()
    time.sleep(1)
    onboardLED.value(1)
    seedL = random.randint(1,3)
    seedT = random.randint(30,51)
    seedT = seedT/12
    print("Next light: ", seedL)
    time.sleep(seedT)
    x = 0
    startTime = time.ticks_ms()
    if seedL == 1:
        red.value(1)
        amber.value(0)
        green.value(0)
        while x == 0:
            if button3.value() == 1:
                x = 1
                onboardLED.value(0)
                endTime = time.ticks_ms()
    elif seedL == 2:
        red.value(0)
        amber.value(1)
        green.value(0)
        while x == 0:
            if button2.value() == 1:
                x = 1
                onboardLED.value(0)
                endTime = time.ticks_ms()
    else:
        red.value(0)
        amber.value(0)
        green.value(1)
        while x == 0:
            if button1.value() == 1:
                x = 1
                onboardLED.value(0)
                endTime = time.ticks_ms()
    time.sleep(0.1)
    finalTime = endTime - startTime
    if finalTime == 0:
        print("Button held \n \n")
    else:
        print("Your time was: ", finalTime, "\n \n")
        finalTime = str(finalTime)
        r = urequests.get('http://ENTERURL/api/rtime.php?date='+date+'&time='+Dtime+'&mode='+mode+'&reaction='+finalTime).text
        print(r)
    time.sleep(0.5)


def hard():
    mode = "Hard"
    flash()
    time.sleep(1)
    onboardLED.value(1)
    seedL = random.randint(1,3)
    seedT = random.randint(30,51)
    seedT = seedT/12
    print("Next light: ", seedL)
    time.sleep(seedT)
    x = 0
    startTime = time.ticks_ms()
    if seedL == 1:
        red.value(0)
        amber.value(1)
        green.value(1)
        time.sleep(0.2)
        off()
        while x == 0:
            if button3.value() == 1:
                x = 1
                onboardLED.value(0)
                endTime = time.ticks_ms()
    elif seedL == 2:
        red.value(1)
        amber.value(0)
        green.value(1)
        time.sleep(0.2)
        off()
        while x == 0:
            if button2.value() == 1:
                x = 1
                onboardLED.value(0)
                endTime = time.ticks_ms()
    else:
        red.value(1)
        amber.value(1)
        green.value(0)
        time.sleep(0.2)
        off()
        while x == 0:
            if button1.value() == 1:
                x = 1
                onboardLED.value(0)
                endTime = time.ticks_ms()
    time.sleep(0.1)
    finalTime = endTime - startTime
    finalTime = finalTime - 0.2
    if finalTime == 0:
        print("Button held \n \n")
    else:
        print("Your time was: ", finalTime, "\n \n")
        finalTime = str(finalTime)
        r = urequests.get('http://ENTERURL/api/rtime.php?date='+date+'&time='+Dtime+'&mode='+mode+'&reaction='+finalTime).text
        print(r)
    time.sleep(0.5)




flash()

while True:
    reading = potentiometer.read_u16()
    time.sleep(0.5)
    
    if reading <= 20000:
        print("Easy mode")
        easy()
    
    elif 20000 < reading < 40000:
        print("Mid Mode")
        mid()

    elif reading >= 40000:
        print("Hard mode")
        hard()


