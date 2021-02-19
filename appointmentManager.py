#!/usr/bin/env python3

from patient import Patient
from exceptions.patientNotFoundException import PatientNotFoundException

class AppointmentManager:
    def __init__(self):
        self.patients = []

    # If we've processed an appointment for the patient before, add it to that patient's schedule
    # Otherwise, create a new patient
    def makeAppointment(self, patient_id, startTime):
        foundPatient = None
        for patient in self.patients:
            if str(patient.patient_id) == str(patient_id):
                foundPatient = patient
                break
        if foundPatient != None:
            return foundPatient.makeAppointment(startTime)
        else:
            newPatient = Patient(patient_id)
            self.patients.append(newPatient)
            return newPatient.makeAppointment(startTime)

    def getAppointmentsForPatient(self, patient_id):
        for patient in self.patients:
            if (str(patient.patient_id) == str(patient_id)):
                return patient.appointments_by_day
        raise PatientNotFoundException("Patient not found")
