#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask.json import JSONEncoder
from urllib.parse import urlparse, parse_qs
import datetime

from jsonEncoder import MyJSONEncoder
from appointment import Appointment
from appointmentManager import AppointmentManager
from patient import Patient
from exceptions.alreadyBookedException import AlreadyBookedException
from exceptions.patientNotFoundException import PatientNotFoundException

app = Flask(__name__)
app.json_encoder = MyJSONEncoder
appointment_manager = AppointmentManager()


@app.route('/appointments/<uuid:patient_id>', methods=['GET'])
def get_appointments(patient_id):
    try:
        appointments = appointment_manager.getAppointmentsForPatient(patient_id)
        return jsonify(appointments)
    except PatientNotFoundException:
        return "Patient not found", 404

@app.route('/appointments/', methods=['POST'])
def make_appointment():
    try:
        patient_id = request.json['patient_id']
        start_time = datetime.datetime.strptime(request.json['start_time'], '%Y-%m-%d %H:%M:%S.%f')
        created_appointment = appointment_manager.makeAppointment(patient_id, start_time)
    except AlreadyBookedException:
        return "Patient already booked", 400
    return jsonify(created_appointment)



if __name__ == '__main__':
    app.run()
