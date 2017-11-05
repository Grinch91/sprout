from energenie import switch_off
import time
import logging
import datetime

def light_controller():
	switch_off(0)
	logger = logging.getLogger('plantie')
	hdlr = logging.FileHandler('/home/plantie/scripts/plantie.log')
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr) 
	logger.setLevel(logging.INFO)

	logger.info('Plantie has switched off')
	return

light_controller()
