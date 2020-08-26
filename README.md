# API Engineer Technical Exercise

Seatmap Availability Exercise:

Write a python script that parses the example seatmap response (OTA_AirSeatMapRS.xml) and return a JSON object 
that lists the seats with the next properties:

	- Type (Seat, Kitchen, Bathroom, etc)
	- Seat id (17A, 18A)
	- Seat price
	- Cabin class
	- Availability

And any other properties you might find interesting or useful.

The output json format is not defined, so feel free to choose whatever you think best represents the information.

# Ryan's Solution Notes

Make sure you've pip installed xmltodict before running this code.

I've included [seats_info.json](https://github.com/Zernach/APIEngineer_TechnicalExercise/blob/master/seats_info.json) within this repo. That file is the JSON output for the code I've written to perform the tasks in this coding assessment for an API Engineer with Gordian Software!

The info for each seat in the JSON file has the following data-points:

* seat_id
* type_of
* cabin_class
* availability
* price