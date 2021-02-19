# Appointment Scheduler

## Runbook

To install dependencies:

    pip install -r requirements.txt

To run the server:

    python server.py

## API Specs

GET localhost:5050/appointments/<patient_id>

Sample Response:

    {
        "02/22/2021": {
            "end_time": "Mon, 22 Feb 2021 12:30:00 GMT",
            "start_time": "Mon, 22 Feb 2021 12:00:00 GMT"
        }
    }

Error Responses:

404 - Patient not found

POST localhost:5050/appointments

Sample Request:

    {
    	"patient_id": "85671c18-8749-40ac-b909-137f50e66064",
    	"start_time": "2021-02-22 12:00:00.000000"
    }

Sample Response:

    {
        "end_time": "Mon, 22 Feb 2021 12:30:00 GMT",
        "start_time": "Mon, 22 Feb 2021 12:00:00 GMT"
    }

Error Responses:

400 - Patient already has an appointment for the specified day

## Future Work

- Custom Error Response Objects
    - The server currently just returns a response code with an error message when it hits a validation error or a not found error. Returning a custom object would give the client more information about the failed request
- Time Validation
    - One of the prompt constraints is that appointments will begin at the top of the hour or at the half hour mark. The current code takes this for granted and doesn't throw an error if the client provides a start time between those constraints.
- Persistence
    - The server stores all the appointments in local memory, so if you restart the server it loses all the scheduling. Adding database support would allow the server to persist appointments between sessions.
