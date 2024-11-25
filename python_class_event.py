class Event:
    def __init__(self, name, location, date):
        self.name = name
        self.location = location
        self.date = date

    def info(self):
        return f"Event: {self.name}, Location: {self.location}, Date: {self.date}"


class Meeting(Event):
    def __init__(self, name, location, date, attendants):
        super().__init__(name, location, date)
        self.attendants = attendants

    def meeting_info(self):
        return (f"{self.info()}, Attendants: {', '.join(self.attendants)}"
                if self.attendants else f"{self.info()}, No attendants yet")


class Appointment(Event):
    def __init__(self, name, location, date, time):
        super().__init__(name, location, date)
        self.time = time

    def appointment_info(self):
        return f"{self.info()}, Time: {self.time}"



def get_event_from_user():
    print("Enter event details:")
    name = input("Event Name: ")
    location = input("Location: ")
    date = input("Date: ")
    event_type = input("Event Type meeting or appointment: ").strip().lower()

    if event_type == "meeting":
        attendants = input("Enter attendants (comma-separated): ").split(',')
        attendants = [attendant.strip() for attendant in attendants if attendant.strip()]
        meeting = Meeting(name, location, date, attendants)
        print("\nMeeting Info:")
        print(meeting.meeting_info())
    elif event_type == "appointment":
        time = input("Time: ")
        appointment = Appointment(name, location, date, time)
        print("\nAppointment Info:")
        print(appointment.appointment_info())
    else:
        print("Invalid event type. Please enter meeting or appointment.")

get_event_from_user()