import calendar

class Schedule:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.schedule = {}
        self.create_empty_schedule()

    def create_empty_schedule(self):
        days_in_month = calendar.monthrange(self.year, self.month)[1]
        for day in range(1, days_in_month + 1):
            self.schedule[day] = {"AM": None, "PM": None}

    def set_availability(self, caregiver: Caregiver, day: int, shift: str, availability: str):
        if not (1 <= day <= calendar.monthrange(self.year, self.month)[1]):
            print(f"Invalid day: {day}. Must be between 1 and {calendar.monthrange(self.year, self.month)[1]}.")
            return
        if shift not in ["AM", "PM"]:
            print("Invalid shift. Options are 'AM' or 'PM'.")
            return
        if self.schedule[day][shift] is not None:
            print(f"Warning: {shift} shift on day {day} is already assigned. Overwriting existing entry.")
        self.schedule[day][shift] = {"caregiver": caregiver, "availability": availability}
        print(f"Set {caregiver.name}'s availability on day {day} ({shift}): {availability}")

    def display_schedule(self):
        print(f"\nSchedule for {calendar.month_name[self.month]} {self.year}:")
        for day, shifts in self.schedule.items():
            print(f"Day {day}:")
            for shift, details in shifts.items():
                if details:
                    caregiver = details["caregiver"]
                    availability = details["availability"]
                    print(f"  {shift} - Caregiver: {caregiver.name} | Availability: {availability}")
                else:
                    print(f"  {shift} - No caregiver assigned")

# Example test
scheduler = Schedule(11, 2023)
caregiver1 = Caregiver("John Doe", "555-1234", "johndoe@example.com", 20)
scheduler.set_availability(caregiver1, 1, "AM", "available")
scheduler.display_schedule()
