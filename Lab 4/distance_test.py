"""
	Reading distance from the laser based VL53L1X
	This example prints the distance to an object. If you are getting weird
	readings, be sure the vacuum tape has been removed from the sensor.
"""

import qwiic
import time
import requests

print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
	print("Sensor online!\n")

while True:
	try:
		ToF.start_ranging()						 # Write configuration bytes to initiate measurement
		time.sleep(.005)
		distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
		time.sleep(.005)
		ToF.stop_ranging()

		distanceInches = distance / 25.4
		distanceFeet = distanceInches / 12.0
		r = requests.get(url="https://lighting-backend.herokuapp.com/dtoc/" + "{:.2f}".format(distance / 100))
		print(r.json())
		print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))

	except Exception as e:
		print(e)
