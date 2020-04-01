import schedule as s
import time
import pytz
from datetime import datetime as dt




tz_IN = pytz.timezone('Asia/Kolkata')
dt_IN = dt.now(tz_IN)

t = dt_IN.hour

state = 0 
# 0 - "alarm"
# 1 - "bottle picked"
# 2 - "bottle placed"

def drink():

	playSound()
	print("Drink water")

	while state != 1:
		time.sleep(5)
		playSound()
	# time.sleep(150)
	while state != 2:

	if bottleEmpty:
		refillBott()		
	


def refillBott():
	print("Refill Bottle")
	playSound()
	while state != 1:
		time.sleep(1)
		playSound()
	while state != 2:

	if not bottleFull:
		refillBott()


def job():
	
	return

def startHourly():
	s.every().hours.tag("hourly").do(job)

def stopHourly():
	s.clear("hourly")

# if t > 5:
# 	s.every().day.at(str(t+1)+":00").do(startHourly)	


# s.every().day.at("05:00").do(startHourly)
# s.every().day.at("21:00").do(stopHourly)


# while True:
# 	s.run_pending()
# 	time.sleep(1)

