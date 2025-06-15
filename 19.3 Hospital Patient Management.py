import uuid
from datetime import datetime

class Doctor:
    def __init__(self, name, specialty):
        self.doctor_id = str(uuid.uuid4())[:8]
        self.name = name 
        self.specialty = specialty
        self.schedule = {}

    def is_available(self, datetime_str):
        return datetime_str not in self.schedule
    
    def book_appointment(self, datetime_str, appointment_id):
        self.schedule[datetime_str] = appointment_id

class Patient:
    def __init__(self,name,ailment):
        self.patient_id = str(uuid.uuid4())[:8]
        self.name = name 
        self.ailment = ailment

class Appointment:
    def __init__(self, doctor_id, patient_id, datetime_str):
        self.appointment_id = str(uuid.uuid4())[:8]
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.datetime_str = datetime_str

class Hospital:
    def __init__(self):
        self.doctors = {}
        self.patients = {}
        self.appointments = {}

    def register_doctor(self, name , specialty):
        doc = Doctor(name, specialty)
        self.doctors[doc.doctor_id] = doc
        print(f"Doctor registered: [{doc.doctor_id}] {doc.name} ({doc.specialty})")

    def register_patient(self, name, ailment):
        pat = Patient(name, ailment)
        self.patients[pat.patient_id] = pat
        print(f"Patient registered: [{pat.patient_id}] {pat.name}, Ailment: {pat.ailment}")

    def schedule_appointment(self, doctor_id, patient_id, datetime_str):
        if doctor_id in self.doctors and patient_id in self.patients:
            doctor = self.doctors[doctor_id]
            if doctor.is_available(datetime_str):
                appt = Appointment(doctor_id, patient_id, datetime_str)
                doctor.book_appointment(datetime_str, appt.appointment_id)
                self.appointments[appt.appointment_id] = appt
                print(f"Appointment booked : [{appt.appointment_id}] at {datetime_str}")
            else:
                print("Doctor is not Available at that time")
        else:
            print("Invalid doctor or patient ID")

    def view_appointments(self):
        print("\n All Appointments")
        for appt in self.appointments.values():
            doc = self.doctors[appt.doctor_id]
            pat = self.patients[appt.patient_id]
            print(f"[{appt.appointment_id}] Dr.{doc.name} with {pat.name} on {appt.datetime_str}")

def main():
    hospital = Hospital()

    while True:
        print("\n---Hospital Management System---")
        print("1. Register Doctor")
        print("2. Register Patient")
        print("3. Schedule Appointment")
        print("4. View Appointments")
        print("5. Exit")

        choice = input("Enter Your choice: ")

        if choice == '1':
            name = input("Doctor's Name: ")
            specialty = input("Specialty: ")
            hospital.register_doctor(name, specialty)
        elif choice == '2':
            name = input("Patient Name: ")
            ailment = input("Ailment: ")
            hospital.register_patient(name, ailment)
        elif choice == '3':
            doc_id = input("Doctor ID: ")
            pat_id = input("Patient ID: ")
            dt_str = input("Appointment Datetime (YYYY-MM-DD HH:MM): ")
            try:
                datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
                hospital.schedule_appointment(doc_id, pat_id, dt_str)
            except ValueError:
                print("\n Please enter date and time in correct format.")
        elif choice == '4':
            hospital.view_appointments()

        elif choice == '5':
            print("\nExiting Hospital Management System. Take Care!")
            break
        else:
            print("\n Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()



    