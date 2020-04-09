import schedule as s
import time
import pytz
from datetime import datetime as dt
from playsound import playsound as ps
from threading import Thread
from time import sleep
import signal
from random import randint
from datetime import timedelta
import os
import serial

tz_IN = pytz.timezone('Asia/Kolkata')
serial = serial.Serial("/dev/ttyS0",9600)

serial1 = [0,1]
dt_IN = dt.now()
now_plus_1 = dt_IN + timedelta(minutes = 1)
bottleEmpty = False
bottleFull = False
interrupted = False
state = 0
# 1 - "bottle picked"
# 2 - "bottle placed"

def signal_handler(signal, frame):
    # example.stop()
    print("interrupted")
    global interrupted
    interrupted = True
    s.clear()

def sensorDataRead():
    while not interrupted:
        global state
        read_serial=serial.readline()
        forcedata = int(serial.readline(),16)
        serial1[0] = str(forcedata)
        print(serial1[0])
        if forcedata < 10:
            bottleEmpty = True
            bottleFull = False
            print("picjed up")
            state = 1
        elif forcedata > 874:
            bottleFull = True
            bottleEmpty = False

        if forcedata > 100 :
            print("places")
            state = 2
            bottleEmpty = False

def playAudio(s):
    r1 = randint(1, 8)
    os.system("aplay -d 5 " + str(r1) + ".wav")
	# if s == "drink":
	# elif s == "refill":
	# 	os.system('aplay -d 10 '+ str(r1)+'.wav')
	# elif s == "place":
	# 	os.system('aplay -d 10 '+ str(r1)+'.wav')

def drink():
    # playAudio("drink")
    print("Drink water")
    while state != 1 and not interrupted:
        print("state"+str(state))
        time.sleep(5)
        playAudio("drink")
    time.sleep(60)
    while state != 2 and not interrupted:
        time.sleep(5)
        playAudio("place")
    if bottleEmpty:
        refillBott()


def refillBott():
	print("Refill Bottle")
	playAudio("refill")
	while state != 1 and not interrupted:
		time.sleep(5)
		playAudio("refill")
	time.sleep(500)
	while state != 2 and not interrupted:
		time.sleep(5)
		playAudio("place")

	if bottleEmpty:
		refillBott()


def job():
	drink()
	return

def startHourly():
    print("hourly started")
    s.every().hours.tag("hourly").do(job)
    # s.every(10).minutes.tag("hourly").do(job)

def stopHourly():
	s.clear("hourly")


signal.signal(signal.SIGINT, signal_handler)

th = Thread(target = sensorDataRead, args = ())
th.start()


# capture SIGINT signal, e.g., Ctrl+C

# if t > 5:
# 	s.every().day.at(str(t+1)+":00").do(startHourly)


# s.every().day.at(now_plus_1.strftime("%H:%M")).do(startHourly)
startHourly()
# s.every().day.at("05:00").do(startHourly)
# s.every().day.at("21:00").do(stopHourly)



while not interrupted:
	# sensorDataRead()
	s.run_pending()
	time.sleep(1)
