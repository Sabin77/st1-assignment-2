class AppointmentRepository:
    def add(self, appointment):
        raise NotImplementedError

    def get_by_id(self, appointment_id):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError


class InMemoryAppointmentRepository(AppointmentRepository):
    def __init__(self):
        self.appointments = []

    def add(self, appointment):
        self.appointments.append(appointment)

    def get_by_id(self, appointment_id):
        for appt in self.appointments:
            if appt.appointment_id == appointment_id:
                return appt
        return None

    def get_all(self):
        return list(self.appointments)