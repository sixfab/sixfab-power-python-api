#!/usr/bin/python3

class Definition:
	TIME_FORMAT_EPOCH = 0
	TIME_FORMAT_DATE_AND_TIME = 1
	TIME_FORMAT_DATE = 2
	TIME_FORMAT_TIME = 3

class DayFactors:
	MONDAY = 	(1<<6)
	TUESDAY =	(1<<5)
	WEDNESDAY =	(1<<4)
	THURSDAY =	(1<<3)
	FRIDAY =	(1<<2)
	SATURDAY =	(1<<1)
	SUNDAY =	(1<<0) 