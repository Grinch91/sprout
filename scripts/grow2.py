from energenie import switch_on, switch_off
import time
import schedule
import datetime
 
def light_controller(timeOff):
	switch_on(0)
	print "Turning on light now and going to sleep"
	print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
	time.sleep(timeOff)
	print "Good morning, turning off the light"
	print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
	switch_off(0)
	print "I have finished running"
	return
		
timeOff = 10
#timeOff = 25200
schedule.every().day.at("22:06").do(light_controller,timeOff)
schedule.every().day.at("22:07").do(light_controller,timeOff)

print "Starting Program"
while True:
	schedule.run_pending()
