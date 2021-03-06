import scoreByCapes

def scheduleDay(meetings):
    last_end = -1
    for end,start in sorted( (end,start) for start,end in meetings ):
        if start >= last_end:
            last_end = end
        elif start < last_end:
        	return False

    return True

def schedule(must_haves, want_to_haves, scoreByDays, scoreByTime, scoreByGaps):
	schedules = []
	days = []
	earlyTimes = []
	lateTimes = []
	totalGaps = []

	for section1 in must_haves[0]:
		for section2 in must_haves[1]:
			for section3 in must_haves[2]:
				for section4 in must_haves[3]:
					for section5 in must_haves[4]:
						for section6 in must_haves[5]:
							for section7 in must_haves[6]:
								for section8 in must_haves[7]:
									monday = []
									tuesday = []
									wednesday = []
									thursday = []
									friday = []
									saturday = []
									sunday = []
									finalMonday = []
									finalTuesday = []
									finalWednesday = []
									finalThursday = []
									finalFriday = []
									finalSaturday = []
									finalSunday = []
									if(section1 != None):
										for meetings in section1['meetings']:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
										if(len(section1['finals']) == 3):
											if(section1['finals'][0] == 'MO'):
												finalMonday.append(section1['finals'][1:])
											elif(section1['finals'][0] == 'TU'):
												finalTuesday.append(section1['finals'][1:])
											elif(section1['finals'][0] == 'WE'):
												finalWednesday.append(section1['finals'][1:])
											elif(section1['finals'][0] == 'TH'):
												finalThursday.append(section1['finals'][1:])
											elif(section1['finals'][0] == 'FR'):
												finalFriday.append(section1['finals'][1:])
											elif(section1['finals'][0] == 'SA'):
												finalSaturday.append(section1['finals'][1:])
											elif(section1['finals'][0] == 'SU'):
												finalSunday.append(section1['finals'][1:])
									if(section2 != None):
										for meetings in section2['meetings']:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
										if(len(section2['finals']) == 3):
											if(section2['finals'][0] == 'MO'):
												finalMonday.append(section2['finals'][1:])
											elif(section2['finals'][0] == 'TU'):
												finalTuesday.append(section2['finals'][1:])
											elif(section2['finals'][0] == 'WE'):
												finalWednesday.append(section2['finals'][1:])
											elif(section2['finals'][0] == 'TH'):
												finalThursday.append(section2['finals'][1:])
											elif(section2['finals'][0] == 'FR'):
												finalFriday.append(section2['finals'][1:])
											elif(section2['finals'][0] == 'SA'):
												finalSaturday.append(section2['finals'][1:])
											elif(section2['finals'][0] == 'SU'):
												finalSunday.append(section2['finals'][1:])
									if(section3 != None):
										for meetings in section3["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
										if(len(section3['finals']) == 3):
											if(section3['finals'][0] == 'MO'):
												finalMonday.append(section3['finals'][1:])
											elif(section3['finals'][0] == 'TU'):
												finalTuesday.append(section3['finals'][1:])
											elif(section3['finals'][0] == 'WE'):
												finalWednesday.append(section3['finals'][1:])
											elif(section3['finals'][0] == 'TH'):
												finalThursday.append(section3['finals'][1:])
											elif(section3['finals'][0] == 'FR'):
												finalFriday.append(section3['finals'][1:])
											elif(section3['finals'][0] == 'SA'):
												finalSaturday.append(section3['finals'][1:])
											elif(section3['finals'][0] == 'SU'):
												finalSunday.append(section3['finals'][1:])
									if(section4 != None):
										for meetings in section4["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
										if(len(section4['finals']) == 3):
											if(section4['finals'][0] == 'MO'):
												finalMonday.append(section4['finals'][1:])
											elif(section4['finals'][0] == 'TU'):
												finalTuesday.append(section4['finals'][1:])
											elif(section4['finals'][0] == 'WE'):
												finalWednesday.append(section4['finals'][1:])
											elif(section4['finals'][0] == 'TH'):
												finalThursday.append(section4['finals'][1:])
											elif(section4['finals'][0] == 'FR'):
												finalFriday.append(section4['finals'][1:])
											elif(section4['finals'][0] == 'SA'):
												finalSaturday.append(section4['finals'][1:])
											elif(section4['finals'][0] == 'SU'):
												finalSunday.append(section4['finals'][1:])
									if(section5 != None):
										for meetings in section5["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
										if(len(section5['finals']) == 3):
											if(section5['finals'][0] == 'MO'):
												finalMonday.append(section5['finals'][1:])
											elif(section5['finals'][0] == 'TU'):
												finalTuesday.append(section5['finals'][1:])
											elif(section5['finals'][0] == 'WE'):
												finalWednesday.append(section5['finals'][1:])
											elif(section5['finals'][0] == 'TH'):
												finalThursday.append(section5['finals'][1:])
											elif(section5['finals'][0] == 'FR'):
												finalFriday.append(section5['finals'][1:])
											elif(section5['finals'][0] == 'SA'):
												finalSaturday.append(section5['finals'][1:])
											elif(section5['finals'][0] == 'SU'):
												finalSunday.append(section5['finals'][1:])
									if(section6 != None):
										for meetings in section6["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
										if(len(section6['finals']) == 3):
											if(section6['finals'][0] == 'MO'):
												finalMonday.append(section6['finals'][1:])
											elif(section6['finals'][0] == 'TU'):
												finalTuesday.append(section6['finals'][1:])
											elif(section6['finals'][0] == 'WE'):
												finalWednesday.append(section6['finals'][1:])
											elif(section6['finals'][0] == 'TH'):
												finalThursday.append(section6['finals'][1:])
											elif(section6['finals'][0] == 'FR'):
												finalFriday.append(section6['finals'][1:])
											elif(section6['finals'][0] == 'SA'):
												finalSaturday.append(section6['finals'][1:])
											elif(section6['finals'][0] == 'SU'):
												finalSunday.append(section6['finals'][1:])
									if(section7 != None):
										for meetings in section7["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
										if(len(section7['finals']) == 3):
											if(section7['finals'][0] == 'MO'):
												finalMonday.append(section7['finals'][1:])
											elif(section7['finals'][0] == 'TU'):
												finalTuesday.append(section7['finals'][1:])
											elif(section7['finals'][0] == 'WE'):
												finalWednesday.append(section7['finals'][1:])
											elif(section7['finals'][0] == 'TH'):
												finalThursday.append(section7['finals'][1:])
											elif(section7['finals'][0] == 'FR'):
												finalFriday.append(section7['finals'][1:])
											elif(section7['finals'][0] == 'SA'):
												finalSaturday.append(section7['finals'][1:])
											elif(section7['finals'][0] == 'SU'):
												finalSunday.append(section7['finals'][1:])
									if(section8 != None):
										for meetings in section8["meetings"]:
											if(meetings[0] == 'MO'):
												monday.append(meetings[1:])
											elif(meetings[0] == 'TU'):
												tuesday.append(meetings[1:])
											elif(meetings[0] == 'WE'):
												wednesday.append(meetings[1:])
											elif(meetings[0] == 'TH'):
												thursday.append(meetings[1:])
											elif(meetings[0] == 'FR'):
												friday.append(meetings[1:])
											elif(meetings[0] == 'SA'):
												saturday.append(meetings[1:])
											elif(meetings[0] == 'SU'):
												sunday.append(meetings[1:])
										if(len(section8['finals']) == 3):
											if(section8['finals'][0] == 'MO'):
												finalMonday.append(section8['finals'][1:])
											elif(section8['finals'][0] == 'TU'):
												finalTuesday.append(section8['finals'][1:])
											elif(section8['finals'][0] == 'WE'):
												finalWednesday.append(section8['finals'][1:])
											elif(section8['finals'][0] == 'TH'):
												finalThursday.append(section8['finals'][1:])
											elif(section8['finals'][0] == 'FR'):
												finalFriday.append(section8['finals'][1:])
											elif(section8['finals'][0] == 'SA'):
												finalSaturday.append(section8['finals'][1:])
											elif(section8['finals'][0] == 'SU'):
												finalSunday.append(section8['finals'][1:])

									if(scheduleDay(monday) == True and scheduleDay(tuesday) == True and scheduleDay(wednesday) == True and scheduleDay(thursday) == True and scheduleDay(friday) == True and scheduleDay(saturday) == True and scheduleDay(sunday) == True and 
									   scheduleDay(finalMonday) == True and scheduleDay(finalTuesday) == True and scheduleDay(finalWednesday) == True and scheduleDay(finalThursday) == True and scheduleDay(finalFriday) == True and scheduleDay(finalSaturday) == True and scheduleDay(finalSunday) == True):

										for optional1 in want_to_haves[0]:
											for optional2 in want_to_haves[1]:
												for optional3 in want_to_haves[2]:
													for optional4 in want_to_haves[3]:
														for optional5 in want_to_haves[4]:
															for optional6 in want_to_haves[5]:
																for optional7 in want_to_haves[6]:
																	optionalMonday = []
																	optionalTuesday = []
																	optionalWednesday = []
																	optionalThursday = []
																	optionalFriday = []
																	optionalSaturday = []
																	optionalSunday = []
																	optionalFinalMonday = []
																	optionalFinalTuesday = []
																	optionalFinalWednesday = []
																	optionalFinalThursday = []
																	optionalFinalFriday = []
																	optionalFinalSaturday = []
																	optionalFinalSunday = []

																	if(optional1 != None):
																		for optMeetings in optional1["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])
																		if(len(optional1['finals']) == 3):
																			if(optional1['finals'][0] == 'MO'):
																				optionalFinalMonday.append(optional1['finals'][1:])
																			elif(optional1['finals'][0] == 'TU'):
																				optionalFinalTuesday.append(optional1['finals'][1:])
																			elif(optional1['finals'][0] == 'WE'):
																				optionalFinalWednesday.append(optional1['finals'][1:])
																			elif(optional1['finals'][0] == 'TH'):
																				optionalFinalThursday.append(optional1['finals'][1:])
																			elif(optional1['finals'][0] == 'FR'):
																				optionalFinalFriday.append(optional1['finals'][1:])
																			elif(optional1['finals'][0] == 'SA'):
																				optionalFinalSaturday.append(optional1['finals'][1:])
																			elif(optional1['finals'][0] == 'SU'):
																				optionalFinalSunday.append(optional1['finals'][1:])
																	
																	if(optional2 != None):
																		for optMeetings in optional2["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])
																		if(len(optional2['finals']) == 3):
																			if(optional2['finals'][0] == 'MO'):
																				optionalFinalMonday.append(optional2['finals'][1:])
																			elif(optional2['finals'][0] == 'TU'):
																				optionalFinalTuesday.append(optional2['finals'][1:])
																			elif(optional2['finals'][0] == 'WE'):
																				optionalFinalWednesday.append(optional2['finals'][1:])
																			elif(optional2['finals'][0] == 'TH'):
																				optionalFinalThursday.append(optional2['finals'][1:])
																			elif(optional2['finals'][0] == 'FR'):
																				optionalFinalFriday.append(optional2['finals'][1:])
																			elif(optional2['finals'][0] == 'SA'):
																				optionalFinalSaturday.append(optional2['finals'][1:])
																			elif(optional2['finals'][0] == 'SU'):
																				optionalFinalSunday.append(optional2['finals'][1:])

																	if(optional3 != None):
																		for optMeetings in optional3["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])
																		if(len(optional3['finals']) == 3):
																			if(optional3['finals'][0] == 'MO'):
																				optionalFinalMonday.append(optional3['finals'][1:])
																			elif(optional3['finals'][0] == 'TU'):
																				optionalFinalTuesday.append(optional3['finals'][1:])
																			elif(optional3['finals'][0] == 'WE'):
																				optionalFinalWednesday.append(optional3['finals'][1:])
																			elif(optional3['finals'][0] == 'TH'):
																				optionalFinalThursday.append(optional3['finals'][1:])
																			elif(optional3['finals'][0] == 'FR'):
																				optionalFinalFriday.append(optional3['finals'][1:])
																			elif(optional3['finals'][0] == 'SA'):
																				optionalFinalSaturday.append(optional3['finals'][1:])
																			elif(optional3['finals'][0] == 'SU'):
																				optionalFinalSunday.append(optional3['finals'][1:])

																	if(optional4 != None):
																		for optMeetings in optional4["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])
																		if(len(optional4['finals']) == 3):
																			if(optional4['finals'][0] == 'MO'):
																				optionalFinalMonday.append(optional4['finals'][1:])
																			elif(optional4['finals'][0] == 'TU'):
																				optionalFinalTuesday.append(optional4['finals'][1:])
																			elif(optional4['finals'][0] == 'WE'):
																				optionalFinalWednesday.append(optional4['finals'][1:])
																			elif(optional4['finals'][0] == 'TH'):
																				optionalFinalThursday.append(optional4['finals'][1:])
																			elif(optional4['finals'][0] == 'FR'):
																				optionalFinalFriday.append(optional4['finals'][1:])
																			elif(optional4['finals'][0] == 'SA'):
																				optionalFinalSaturday.append(optional4['finals'][1:])
																			elif(optional4['finals'][0] == 'SU'):
																				optionalFinalSunday.append(optional4['finals'][1:])

																	if(optional5 != None):
																		for optMeetings in optional5["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])
																		if(len(optional5['finals']) == 3):
																			if(optional5['finals'][0] == 'MO'):
																				optionalFinalMonday.append(optional5['finals'][1:])
																			elif(optional5['finals'][0] == 'TU'):
																				optionalFinalTuesday.append(optional5['finals'][1:])
																			elif(optional5['finals'][0] == 'WE'):
																				optionalFinalWednesday.append(optional5['finals'][1:])
																			elif(optional5['finals'][0] == 'TH'):
																				optionalFinalThursday.append(optional5['finals'][1:])
																			elif(optional5['finals'][0] == 'FR'):
																				optionalFinalFriday.append(optional5['finals'][1:])
																			elif(optional5['finals'][0] == 'SA'):
																				optionalFinalSaturday.append(optional5['finals'][1:])
																			elif(optional5['finals'][0] == 'SU'):
																				optionalFinalSunday.append(optional5['finals'][1:])

																	if(optional6 != None):
																		for optMeetings in optional6["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])
																		if(len(optional6['finals']) == 3):
																			if(optional6['finals'][0] == 'MO'):
																				optionalFinalMonday.append(optional6['finals'][1:])
																			elif(optional6['finals'][0] == 'TU'):
																				optionalFinalTuesday.append(optional6['finals'][1:])
																			elif(optional6['finals'][0] == 'WE'):
																				optionalFinalWednesday.append(optional6['finals'][1:])
																			elif(optional6['finals'][0] == 'TH'):
																				optionalFinalThursday.append(optional6['finals'][1:])
																			elif(optional6['finals'][0] == 'FR'):
																				optionalFinalFriday.append(optional6['finals'][1:])
																			elif(optional6['finals'][0] == 'SA'):
																				optionalFinalSaturday.append(optional6['finals'][1:])
																			elif(optional6['finals'][0] == 'SU'):
																				optionalFinalSunday.append(optional6['finals'][1:])

																	if(optional7 != None):
																		for optMeetings in optional7["meetings"]:
																			if(optMeetings[0] == 'MO'):
																				optionalMonday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TU'):
																				optionalTuesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'WE'):
																				optionalWednesday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'TH'):
																				optionalThursday.append(optMeetings[1:])
																			elif(optMeetings[0] == 'FR'):
																				optionalFriday.append(optMeetings[1:])
																			elif(meetings1[0] == 'SA'):
																				optionalSaturday.append(optMeetings[1:])
																			elif(meetings1[0] == 'SU'):
																				optionalSaturday.append(optMeetings[1:])
																		if(len(optional7['finals']) == 3):
																			if(optional7['finals'][0] == 'MO'):
																				optionalFinalMonday.append(optional7['finals'][1:])
																			elif(optional7['finals'][0] == 'TU'):
																				optionalFinalTuesday.append(optional7['finals'][1:])
																			elif(optional7['finals'][0] == 'WE'):
																				optionalFinalWednesday.append(optional7['finals'][1:])
																			elif(optional7['finals'][0] == 'TH'):
																				optionalFinalThursday.append(optional7['finals'][1:])
																			elif(optional7['finals'][0] == 'FR'):
																				optionalFinalFriday.append(optional7['finals'][1:])
																			elif(optional7['finals'][0] == 'SA'):
																				optionalFinalSaturday.append(optional7['finals'][1:])
																			elif(optional7['finals'][0] == 'SU'):
																				optionalFinalSunday.append(optional7['finals'][1:])

																	jointMonday = monday + optionalMonday
																	jointTuesday = tuesday + optionalTuesday
																	jointWednesday = wednesday + optionalWednesday
																	jointThursday = thursday + optionalThursday
																	jointFriday = friday + optionalFriday
																	jointSaturday = saturday + optionalSaturday
																	jointSunday = sunday + optionalSunday

																	if(scheduleDay(jointMonday) == True and scheduleDay(jointTuesday) == True and scheduleDay(jointWednesday) == True and scheduleDay(jointThursday) == True and scheduleDay(jointFriday) == True and scheduleDay(jointSaturday) == True and scheduleDay(jointSunday) == True and
																	   scheduleDay(finalMonday+optionalFinalMonday) == True and scheduleDay(finalTuesday+optionalFinalTuesday) == True and scheduleDay(finalWednesday+optionalFinalWednesday) == True and scheduleDay(finalThursday+optionalFinalThursday) == True and scheduleDay(finalFriday+optionalFinalFriday) == True and scheduleDay(finalSaturday+optionalFinalSaturday) == True and scheduleDay(finalSunday+optionalFinalSunday) == True):
																		schedule = []
																		if(section1 != None):
																			schedule.append(section1)
																		if(section2 != None):
																			schedule.append(section2)
																		if(section3 != None):
																			schedule.append(section3)
																		if(section4 != None):
																			schedule.append(section4)
																		if(section5 != None):
																			schedule.append(section5)
																		if(section6 != None):
																			schedule.append(section6)
																		if(section7 != None):
																			schedule.append(section7)
																		if(section8 != None):
																			schedule.append(section8)
																		if(optional1 != None):
																			schedule.append(optional1)
																		if(optional2 != None):
																			schedule.append(optional2)
																		if(optional3 != None):
																			schedule.append(optional3)
																		if(optional4 != None):
																			schedule.append(optional4)
																		if(optional5 != None):
																			schedule.append(optional5)
																		if(optional6 != None):
																			schedule.append(optional6)
																		if(optional7 != None):
																			schedule.append(optional7)
																		schedules.append(schedule)
																		
																		if(scoreByDays == True):
																			days.append(scoreDays([jointMonday,jointTuesday,jointWednesday,jointThursday,jointFriday,jointSaturday,jointSunday]))
																		if(scoreByTime == True):
																			earliestTime, latestTime = scoreTime([jointMonday,jointTuesday,jointWednesday,jointThursday,jointFriday,jointSaturday,jointSunday])
																			earlyTimes.append(earliestTime)
																			lateTimes.append(latestTime)
																		if(scoreByGaps == True):
																			totalGaps.append(scoreGaps([jointMonday,jointTuesday,jointWednesday,jointThursday,jointFriday,jointSaturday,jointSunday]))


	
	return schedules, days, earlyTimes, lateTimes, totalGaps

def scoreDays(days):
	numDays = 0
	for day in days:
		if(len(day) != 0):
			numDays += 1
	return numDays

def scoreTime(days):
	earliestTime = 2400
	latestTime = 0
	for day in days:
		for meeting in day:
			if(meeting[0] < earliestTime):
				earliestTime = meeting[0]
			if(meeting[1] > latestTime):
				latestTime = meeting[1]

	return earliestTime, latestTime

def scoreGaps(days):
	totalGaps = 0
	for day in days:
		lastEnd = None
		for end,start in sorted( (end,start) for start,end in day ):
			if(lastEnd == None):
				lastEnd = end
			else:
				totalGaps += (start - lastEnd)
				
	return totalGaps
			


def generateSchedule(must_haves,want_to_haves,preferences):
	tempMustHaves = must_haves
	tempWantHaves = want_to_haves
	while(len(tempMustHaves) < 8):
		tempMustHaves.append([None])
	for i in want_to_haves:
		i.append(None)
	while(len(tempWantHaves) < 7):
		tempWantHaves.append([None])
	
	scoreByDays = False
	scoreByTime = False
	scoreByGaps = False
	if(preferences['class_Days'] == 'false' or preferences['class_Days'] == 'true'):
		scoreByDays = True
	if(preferences['time_Ref'] == 'false' or preferences['time_Ref'] == 'true'):
		scoreByTime = True
	if(preferences['gap'] == 'false' or preferences['gap'] == 'true'):
		scoreByGaps = True

	schedules, days, earlyTimes, lateTimes, totalGaps = schedule(tempMustHaves, tempWantHaves, scoreByDays, scoreByTime, scoreByGaps)
	capes = []

	if(len(schedules) == 0):
		return []
	elif(len(schedules) == 1):
		return schedules[0]
	else:
		maxSections = 0
		maxLength = 0
		maxSchedules = []
		scores = {}

		for tempSchedule in schedules:
			if(len(tempSchedule) > maxLength):
				maxLength= len(tempSchedule)
		counter = -1
		for tempSchedule in schedules:
			counter += 1
			if(len(tempSchedule) == maxLength):
				maxSchedules.append(counter)
				scores[counter]=0

		
		if(len(maxSchedules) == 1):
			return schedules[maxSchedules[0]]
		else:
			for i in maxSchedules:
				if(preferences['prof_Rating'] == 'true' or preferences['avg_GPA'] == 'true' or preferences['avg_Time'] == 'true'):
					sectionID = parseSchedule(schedules[i])
					capeScores = scoreByCapes.score_by_capes(sectionID)
					gradeTotal = 0
					timeTotal = 0
					ratingTotal = 0
					for i in capeScores:
						gradeTotal += i['grade']
						timeTotal += i['time spent']
						ratingTotal += i['rating']
					capes.append({'grade':gradeTotal,'rating':ratingTotal,'time spent':timeTotal})
			
			if(preferences['prof_Rating'] == "true"):
				ranking = []
				index = -1
				for i in capes:
					index += 1
					ranking.append([maxSchedules[index],i['rating']])
				sorted_ranking = sorted(ranking, key=take_second, reverse=True)
				index = 0
				for i in sorted_ranking:
					index += 1
					scores[i[0]] += index
				

			if(preferences['avg_GPA'] == "true"):
				ranking = []
				index = -1
				for i in capes:
					index += 1
					ranking.append([maxSchedules[index],i['grade']])
				sorted_ranking = sorted(ranking, key=take_second, reverse=True)
				index = 0
				for i in sorted_ranking:
					index += 1
					scores[i[0]] += index


			if(preferences['avg_Time'] == "true"):
				ranking = []
				index = -1
				for i in capes:
					index += 1
					ranking.append([maxSchedules[index],i['time spent']])
				sorted_ranking = sorted(ranking, key=take_second)
				index = 0
				for i in sorted_ranking:
					index += 1
					scores[i[0]] += index

			if(preferences['class_Days'] == "false"):
				ranking = []
				index = -1
				for i in maxSchedules:
					index += 1
					ranking.append([i,days[i]])
				sorted_ranking = sorted(ranking, key=take_second)
				index = 0
				for i in sorted_ranking:
					index += 1
					scores[i[0]] += index
			elif(preferences['class_Days'] == 'true'):
				ranking = []
				index = -1
				for i in maxSchedules:
					index += 1
					ranking.append([i,days[i]])
				sorted_ranking = sorted(ranking, key=take_second, reverse=True)
				index = 0
				for i in sorted_ranking:
					index += 1
					scores[i[0]] += index

			if(preferences['time_Ref'] == "false"):
				ranking = []
				index = -1
				for i in maxSchedules:
					index += 1
					ranking.append([i,lateTimes[i]])
				sorted_ranking = sorted(ranking, key=take_second)
				index = 0
				for i in sorted_ranking:
					index += 1
					scores[i[0]] += index
			elif(preferences['time_Ref'] == 'true'):
				ranking = []
				index = -1
				for i in maxSchedules:
					index += 1
					ranking.append([i,earlyTimes[i]])
				sorted_ranking = sorted(ranking, key=take_second, reverse=True)
				index = 0
				for i in sorted_ranking:
					index += 1
					scores[i[0]] += index


			if(preferences['gap'] == "false"):
				ranking = []
				index = -1
				for i in maxSchedules:
					index += 1
					ranking.append([i,totalGaps[i]])
				sorted_ranking = sorted(ranking, key=take_second)
				index = 0
				for i in sorted_ranking:
					index += 1
					scores[i[0]] += index
			elif(preferences['gap'] == 'true'):
				ranking = []
				index = -1
				for i in maxSchedules:
					index += 1
					ranking.append([i,totalGaps[i]])
				sorted_ranking = sorted(ranking, key=take_second, reverse=True)
				index = 0
				for i in sorted_ranking:
					index += 1
					scores[i[0]] += index

			minRank = 10000
			minIndex = -1
			for x in scores:
				if(scores[x] < minRank):
					minRank = scores[x]
					minIndex = x
			return schedules[minIndex]


def parseSchedule(schedule):
	sectionIDs = []
	for i in schedule:
		if(i['id'] != 'personal event'):
			sectionIDs.append(i['id'])
	return sectionIDs

def take_second(elem):
	return elem[1]

def main():
	# Must-takes/Personal Events
	# 1.CSE 120 TUTH 8:00-9:20 TH 10:00-10:50 @@@
	# 2.CSE 141 MWF 10:00-10:50 W 11:00-11:50 @@@
	# 3.CSE 141 TUTH 3:30-4:50 TU 2:00-2:50
	# 4.CSE 141L M 3:00-3:50 W 3:00-3:50 @@@
	# 5.CSE 141L M 4:00-4:50 W 4:00-4:50 @@@
	# 6.CSE 110 TUTH 2:00-3:20 W 9:00-11:50
	# 7.CSE 110 TUTH 2:00-3:20 W 9:00-11:50
	# 8.CSE 110 TUTH 2:00-3:20 W 9:00-11:50
	# 9.CSE 110 TUTH 2:00-3:20 W 12:00-2:50 @@@
	# 10.CSE 110 TUTH 2:00-3:20 W 12:00-2:50 @@

	# Want-to-takes
	# 11. ECE 107 TUTH 8:00-9:20 F 11:00-11:50
	# 12. CSE 130 MWF 4:00-4:50 TH 5:00-5:50 @@@
	# 13. CSE 111 MWF 4:00-4:50 TH 5:00-5:50


	#Start time, end time, index
	must_takes=[[{'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['MO', 1200, 1250]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 830, 1020, '2020-10-24'], ['SA', 830, 1020, '2020-11-21']], 'LE id': '018852', 'id': '020992', 'waitlist': False}, {'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['MO', 1300, 1350]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 830, 1020, '2020-10-24'], ['SA', 830, 1020, '2020-11-21']], 'LE id': '018852', 'id': '020993', 'waitlist': False}, {'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['WE', 1900, 1950]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 830, 1020, '2020-10-24'], ['SA', 830, 1020, '2020-11-21']], 'LE id': '018852', 'id': '020994', 'waitlist': False}, {'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['WE', 2000, 2050]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 830, 1020, '2020-10-24'], ['SA', 830, 1020, '2020-11-21']], 'LE id': '018852', 'id': '020995', 'waitlist': False}, {'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['WE', 2100, 2150]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 830, 1020, '2020-10-24'], ['SA', 830, 1020, '2020-11-21']], 'LE id': '018852', 'id': '020996', 'waitlist': False}, {'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['FR', 900, 950]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 830, 1020, '2020-10-24'], ['SA', 830, 1020, '2020-11-21']], 'LE id': '018852', 'id': '020997', 'waitlist': False}, {'meetings': [['TU', 800, 920], ['TH', 800, 920], ['MO', 900, 950]], 'finals': ['TU', 800, 1059], 'midterms': [], 'LE id': '018853', 'id': '021116', 'waitlist': False}, {'meetings': [['TU', 800, 920], ['TH', 800, 920], ['MO', 1000, 1050]], 'finals': ['TU', 800, 1059], 'midterms': [], 'LE id': '018853', 'id': '021117', 'waitlist': False}, {'meetings': [['TU', 800, 920], ['TH', 800, 920], ['MO', 1200, 1250]], 'finals': ['TU', 800, 1059], 'midterms': [], 'LE id': '018853', 'id': '021118', 'waitlist': False}, {'meetings': [['TU', 800, 920], ['TH', 800, 920], ['WE', 1200, 1250]], 'finals': ['TU', 800, 1059], 'midterms': [], 'LE id': '018853', 'id': '021119', 'waitlist': False}, {'meetings': [['TU', 800, 920], ['TH', 800, 920], ['WE', 1400, 1450]], 'finals': ['TU', 800, 1059], 'midterms': [], 'LE id': '018853', 'id': '021120', 'waitlist': False}, {'meetings': [['TU', 800, 920], ['TH', 800, 920], ['FR', 1500, 1550]], 'finals': ['TU', 800, 1059], 'midterms': [], 'LE id': '018853', 'id': '021121', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 800, 850]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018854', 'id': '020706', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 900, 950]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018854', 'id': '020707', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 1200, 1250]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018854', 'id': '020708', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 1400, 1450]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018854', 'id': '020709', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 1500, 1550]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018854', 'id': '020710', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 1600, 1650]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018854', 'id': '020711', 'waitlist': False}, {'meetings': [['MO', 1300, 1350], ['WE', 1300, 1350], ['FR', 1300, 1350], ['WE', 1000, 1050]], 'finals': ['MO', 1130, 1429], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018855', 'id': '021177', 'waitlist': False}, {'meetings': [['MO', 1300, 1350], ['WE', 1300, 1350], ['FR', 1300, 1350], ['WE', 1200, 1250]], 'finals': ['MO', 1130, 1429], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018855', 'id': '021178', 'waitlist': False}, {'meetings': [['MO', 1300, 1350], ['WE', 1300, 1350], ['FR', 1300, 1350], ['TH', 2000, 2050]], 'finals': ['MO', 1130, 1429], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018855', 'id': '021179', 'waitlist': False}, {'meetings': [['MO', 1300, 1350], ['WE', 1300, 1350], ['FR', 1300, 1350], ['TH', 2100, 2150]], 'finals': ['MO', 1130, 1429], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018855', 'id': '021180', 'waitlist': False}, {'meetings': [['MO', 1300, 1350], ['WE', 1300, 1350], ['FR', 1300, 1350], ['FR', 900, 950]], 'finals': ['MO', 1130, 1429], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018855', 'id': '021181', 'waitlist': False}, {'meetings': [['MO', 1300, 1350], ['WE', 1300, 1350], ['FR', 1300, 1350], ['FR', 1400, 1450]], 'finals': ['MO', 1130, 1429], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018855', 'id': '021182', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 800, 850]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018856', 'id': '020726', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 1000, 1050]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018856', 'id': '020727', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 900, 950]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018856', 'id': '020728', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 1300, 1350]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018856', 'id': '020729', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 1600, 1650]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018856', 'id': '020730', 'waitlist': False}, {'meetings': [['MO', 1100, 1150], ['WE', 1100, 1150], ['FR', 1100, 1150], ['FR', 1700, 1750]], 'finals': ['TU', 1130, 1429], 'midterms': [], 'LE id': '018856', 'id': '020731', 'waitlist': False}, {'meetings': [['TU', 930, 1050], ['TH', 930, 1050], ['MO', 1600, 1650]], 'finals': ['TH', 800, 1059], 'midterms': [], 'LE id': '018857', 'id': '020716', 'waitlist': False}, {'meetings': [['TU', 930, 1050], ['TH', 930, 1050], ['MO', 1700, 1750]], 'finals': ['TH', 800, 1059], 'midterms': [], 'LE id': '018857', 'id': '020717', 'waitlist': False}, {'meetings': [['TU', 930, 1050], ['TH', 930, 1050], ['MO', 1800, 1850]], 'finals': ['TH', 800, 1059], 'midterms': [], 'LE id': '018857', 'id': '020718', 'waitlist': False}, {'meetings': [['TU', 930, 1050], ['TH', 930, 1050], ['MO', 1900, 1950]], 'finals': ['TH', 800, 1059], 'midterms': [], 'LE id': '018857', 'id': '020719', 'waitlist': False}, {'meetings': [['TU', 930, 1050], ['TH', 930, 1050], ['MO', 2000, 2050]], 'finals': ['TH', 800, 1059], 'midterms': [], 'LE id': '018857', 'id': '020720', 'waitlist': False}, {'meetings': [['TU', 930, 1050], ['TH', 930, 1050], ['MO', 2100, 2150]], 'finals': ['TH', 800, 1059], 'midterms': [], 'LE id': '018857', 'id': '020721', 'waitlist': False}, {'meetings': [['MO', 1400, 1450], ['WE', 1400, 1450], ['FR', 1400, 1450], ['MO', 800, 850]], 'finals': ['WE', 1500, 1759], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018858', 'id': '021960', 'waitlist': False}, {'meetings': [['MO', 1400, 1450], ['WE', 1400, 1450], ['FR', 1400, 1450], ['MO', 1200, 1250]], 'finals': ['WE', 1500, 1759], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018858', 'id': '021961', 'waitlist': False}, {'meetings': [['MO', 1400, 1450], ['WE', 1400, 1450], ['FR', 1400, 1450], ['MO', 2100, 2150]], 'finals': ['WE', 1500, 1759], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018858', 'id': '021962', 'waitlist': False}, {'meetings': [['MO', 1400, 1450], ['WE', 1400, 1450], ['FR', 1400, 1450], ['WE', 2000, 2050]], 'finals': ['WE', 1500, 1759], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018858', 'id': '021963', 'waitlist': False}, {'meetings': [['MO', 1400, 1450], ['WE', 1400, 1450], ['FR', 1400, 1450], ['WE', 2100, 2150]], 'finals': ['WE', 1500, 1759], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018858', 'id': '021964', 'waitlist': False}, {'meetings': [['MO', 1400, 1450], ['WE', 1400, 1450], ['FR', 1400, 1450], ['FR', 1500, 1550]], 'finals': ['WE', 1500, 1759], 'midterms': [['TU', 1800, 1950, '2020-10-27'], ['TU', 1800, 1950, '2020-12-01']], 'LE id': '018858', 'id': '021965', 'waitlist': False}, {'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['MO', 900, 950]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 1530, 1650, '2020-10-31'], ['SA', 1530, 1650, '2020-12-05']], 'LE id': '018859', 'id': '022009', 'waitlist': False}, {'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['MO', 1000, 1050]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 1530, 1650, '2020-10-31'], ['SA', 1530, 1650, '2020-12-05']], 'LE id': '018859', 'id': '022010', 'waitlist': False}, {'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['MO', 1100, 1150]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 1530, 1650, '2020-10-31'], ['SA', 1530, 1650, '2020-12-05']], 'LE id': '018859', 'id': '022011', 'waitlist': False}, {'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['MO', 1200, 1250]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 1530, 1650, '2020-10-31'], ['SA', 1530, 1650, '2020-12-05']], 'LE id': '018859', 'id': '022012', 'waitlist': False}, {'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['MO', 1300, 1350]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 1530, 1650, '2020-10-31'], ['SA', 1530, 1650, '2020-12-05']], 'LE id': '018859', 'id': '022013', 'waitlist': False}, {'meetings': [['MO', 800, 850], ['WE', 800, 850], ['FR', 800, 850], ['MO', 1400, 1450]], 'finals': ['MO', 800, 1059], 'midterms': [['SA', 1530, 1650, '2020-10-31'], ['SA', 1530, 1650, '2020-12-05']], 'LE id': '018859', 'id': '022014', 'waitlist': False}, {'meetings': [['MO', 1000, 1050], ['WE', 1000, 1050], ['FR', 1000, 1050], ['FR', 800, 850]], 'finals': ['FR', 800, 1059], 'midterms': [['SA', 1000, 1150, '2020-10-24'], ['SA', 1000, 1150, '2020-11-21']], 'LE id': '018860', 'id': '021209', 'waitlist': False}, {'meetings': [['MO', 1000, 1050], ['WE', 1000, 1050], ['FR', 1000, 1050], ['FR', 900, 950]], 'finals': ['FR', 800, 1059], 'midterms': [['SA', 1000, 1150, '2020-10-24'], ['SA', 1000, 1150, '2020-11-21']], 'LE id': '018860', 'id': '021210', 'waitlist': False}, {'meetings': [['MO', 1000, 1050], ['WE', 1000, 1050], ['FR', 1000, 1050], ['FR', 1500, 1550]], 'finals': ['FR', 800, 1059], 'midterms': [['SA', 1000, 1150, '2020-10-24'], ['SA', 1000, 1150, '2020-11-21']], 'LE id': '018860', 'id': '021211', 'waitlist': False}, {'meetings': [['MO', 1000, 1050], ['WE', 1000, 1050], ['FR', 1000, 1050], ['FR', 1600, 1650]], 'finals': ['FR', 800, 1059], 'midterms': [['SA', 1000, 1150, '2020-10-24'], ['SA', 1000, 1150, '2020-11-21']], 'LE id': '018860', 'id': '021212', 'waitlist': False}, {'meetings': [['MO', 1000, 1050], ['WE', 1000, 1050], ['FR', 1000, 1050], ['FR', 1700, 1750]], 'finals': ['FR', 800, 1059], 'midterms': [['SA', 1000, 1150, '2020-10-24'], ['SA', 1000, 1150, '2020-11-21']], 'LE id': '018860', 'id': '021214', 'waitlist': False}]] 
	want_to_takes=[]
	preference = {'prof_Rating': 'false', 'avg_GPA': 'false', 'avg_Time': 'false', 'gap': 'none', 'class_Days': 'none', 'time_Ref': 'false'}
	schedules = generateSchedule(must_takes,want_to_takes,preference)
	print(schedules)
	#max = 0
	#for i in schedules:
#		if len(i) > max:
#			max = len(i)
#
#	final_schedules = []
#	for i in schedules:
#		if len(i) == max:
#			final_schedules.append(i)

#	print(final_schedules)

if __name__ == '__main__':
	main()
