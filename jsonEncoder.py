#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask.json import JSONEncoder
from appointment import Appointment

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Appointment):
            return {
                'start_time': obj.startTime,
                'end_time': obj.endTime,
            }
        return super(MyJSONEncoder, self).default(obj)
