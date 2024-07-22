class Hospital:
    def __init__(self):
        self.doctors = {}
        self.patients = {}
        self.appointments = []

    def add_doctor(self, doctor_id, name, specialty):
        self.doctors[doctor_id] = {"name": name, "specialty": specialty}

    def add_patient(self, patient_id, name, age):
        self.patients[patient_id] = {"name": name, "age": age}

    def book_appointment(self, appointment_id, doctor_id, patient_id, time):
        if doctor_id not in self.doctors:
            print(f"Doctor with ID {doctor_id} does not exist.")
            return
        if patient_id not in self.patients:
            print(f"Patient with ID {patient_id} does not exist.")
            return
        
        self.appointments.append({
            "appointment_id": appointment_id,
            "doctor_id": doctor_id,
            "patient_id": patient_id,
            "time": time
        })
        print(f"Appointment {appointment_id} booked successfully.")

    def view_appointments(self):
        for appointment in self.appointments:
            doctor = self.doctors[appointment["doctor_id"]]
            patient = self.patients[appointment["patient_id"]]
            print(f"Appointment ID: {appointment['appointment_id']}")
            print(f"Doctor: {doctor['name']} (Specialty: {doctor['specialty']})")
            print(f"Patient: {patient['name']} (Age: {patient['age']})")
            print(f"Time: {appointment['time']}")
            print("-" * 20)

# Example usage
hospital = Hospital()

# Adding doctors
hospital.add_doctor(1, "Dr. Smith", "Cardiologist")
hospital.add_doctor(2, "Dr. Jones", "Neurologist")

# Adding patients
hospital.add_patient(1, "John Doe", 30)
hospital.add_patient(2, "Jane Roe", 25)

# Booking appointments
hospital.book_appointment(1, 1, 1, "2024-07-21 10:00")
hospital.book_appointment(2, 2, 2, "2024-07-21 11:00")

# Viewing appointments
hospital.view_appointments()
