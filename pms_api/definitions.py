#!/usr/bin/python3

class Definition:
	# Time Format
	TIME_FORMAT_EPOCH = 0
	TIME_FORMAT_DATE_AND_TIME = 1
	TIME_FORMAT_DATE = 2
	TIME_FORMAT_TIME = 3

	# Day factor
	MONDAY = 	(1<<0)
	TUESDAY =	(1<<1)
	WEDNESDAY =	(1<<2)
	THURSDAY =	(1<<3)
	FRIDAY =	(1<<4)
	SATURDAY =	(1<<5)
	SUNDAY =	(1<<6)
	EVERYDAY =  127

	# Scheduled Event ID Factor
	SE_ID_0 =	(1<<0)
	SE_ID_1 =	(1<<1)
	SE_ID_2 =	(1<<2)
	SE_ID_3 =	(1<<3)
	SE_ID_4 =	(1<<4)
	SE_ID_5 =	(1<<5)
	SE_ID_6 =	(1<<6)
	SE_ID_7 =	(1<<7)
	SE_ID_8 =	(1<<8)
	SE_ID_9 =	(1<<9) 

	# Scheduled Event ID Status
	NULL_ID = 0xFF
	ACTIVE_ID = 0x01


	
	