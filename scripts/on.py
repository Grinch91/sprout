from energenie import switch_on
import time
import logging
import datetime

def light_controller():
	switch_on(0)
	logger = logging.getLogger('plantie')
	hdlr = logging.FileHandler('/home/plantie/scripts/plantie.log')
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr) 
	logger.setLevel(logging.INFO)

	logger.info('Plantie has switched on')
	return

light_controller()
