# Appointment Booking API

This is a minimal Flask backend to demonstrate appointment booking functionality for a telehealth app like MediConnect.

## Base URL (After Deploying)
e.g. `https://mediconnect-booking.onrender.com`

---

## 🔹 Endpoint 1: Book Appointment

**POST** `/api/appointments/book`

### Request Body
```json
{
  "doctorId": "doc001",
  "patientId": "pat001",
  "date": "2025-07-05",
  "time": "09:00"
}
