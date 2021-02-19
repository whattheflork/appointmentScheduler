#!/usr/bin/env python3

import datetime

from appointment import Appointment
from exceptions.alreadyBookedException import AlreadyBookedException


class Patient:
    def __init__(self, patient_id):
        self.appointments_by_day = {}
        self.patient_id = patient_id

    ## If the patient already has an appointment for the day, throw an exception
    ## Otherwise, add that day to the patient's appointment dictionary
    def makeAppointment(self, startTime):
        dateString = startTime.strftime("%m/%d/%Y")
        if dateString in self.appointments_by_day:
            raise AlreadyBookedException('Patient already has an appointment on ' + dateString)
        else:
            self.appointments_by_day[dateString] = Appointment(startTime, startTime + datetime.timedelta(minutes=30))
            return self.appointments_by_day[dateString]
