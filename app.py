from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import os


app = Flask(__name__)
CORS(app)

appointments = []  # in-memory appointment store

@app.route('/api/appointments/book', methods=['POST'])
def book_appointment():
    data = request.get_json()
    required = ['doctorId', 'patientId', 'date', 'time']
    if not all(key in data for key in required):
        return jsonify({'error': 'Missing fields'}), 400

    for appt in appointments:
        if appt['doctorId'] == data['doctorId'] and appt['date'] == data['date'] and appt['time'] == data['time']:
            return jsonify({'error': 'Slot already booked'}), 400

    appointment = {
        'appointmentId': str(uuid.uuid4())[:8],
        **data,
        'status': 'confirmed'
    }
    appointments.append(appointment)
    return jsonify({'message': 'Appointment booked successfully', 'appointmentId': appointment['appointmentId']}), 201

@app.route('/api/appointments/doctor', methods=['GET'])
def get_doctor_appointments():
    doctor_id = request.args.get('doctorId')
    if not doctor_id:
        return jsonify({'error': 'Missing doctorId'}), 400
    doctor_appointments = [a for a in appointments if a['doctorId'] == doctor_id]
    return jsonify({'appointments': doctor_appointments}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

