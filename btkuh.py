import schedule as s
import time
import pytz
from datetime import datetime as dt
from playsound import playsound as ps
from threading import Thread
from time import sleep
import signal
from random import randint


tz_IN = pytz.timezone('Asia/Kolkata')
dt_IN = dt.now(tz_IN)

t = dt_IN.hour
interrupted = False
state = 0
# 1 - "bottle picked"
# 2 - "bottle placed"

def signal_handler(signal, frame):
    # example.stop()
    print("interrupted")
    global interrupted
    interrupted = True

def sensorDataRead():
	print("data read")
	# time.sleep(5)
	print("data read complete")

def playAudio(s):
	r1 = randint(0, 9)

	if s == "drink":
		ps(str(r1)+".mp3")
	elif s == "refill":
		ps(str(r1)+".mp3")
	elif s == "place":
		ps(str(r1)+".mp3")

def drink():

	playAudio("drink")
	print("Drink water")

	while state != 1:
		time.sleep(5)
		playAudio("drink")
	time.sleep(150)
	while state != 2:
		time.sleep(5)
		playAudio("place")

	if bottleEmpty:
		refillBott()


def refillBott():
	print("Refill Bottle")
	playAudio("refill")
	while state != 1:
		time.sleep(5)
		playAudio("refill")
	time.sleep(500)
	while state != 2:
		time.sleep(5)
		playAudio("place")

	if bottleEmpty:
		refillBott()


def job():
	drink()
	return

def startHourly():
    print("hourly started")
	# s.every().hours.tag("hourly").do(job)
    s.every(10).seconds.tag("hourly").do(job)

def stopHourly():
	s.clear("hourly")


signal.signal(signal.SIGINT, signal_handler)

# th = Thread(target = sensorDataRead, args = ())
# th.start()


# capture SIGINT signal, e.g., Ctrl+C

# if t > 5:
# 	s.every().day.at(str(t+1)+":00").do(startHourly)


s.every().day.at("00:28").do(startHourly)

# s.every().day.at("05:00").do(startHourly)
# s.every().day.at("21:00").do(stopHourly)



while not interrupted:
	# sensorDataRead()
	s.run_pending()
	time.sleep(1)
