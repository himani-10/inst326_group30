import calendar

class Schedule:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.schedule = {}
        # Initialize empty schedule for each day and shift
        self.create_empty_schedule()

    def create_empty_schedule(self):
        """Create an empty schedule for AM and PM shifts for each day of the month"""
        days_in_month = calendar.monthrange(self.year, self.month)[1]
        for day in range(1, days_in_month + 1):
            self.schedule[day] = {"AM": None, "PM": None}

    def set_availability(self, caregiver, day, shift, availability):
        """Set availability for a caregiver on a specific day and shift"""
        if day in self.schedule:
            if shift in ["AM", "PM"]:
                self.schedule[day][shift] = {"caregiver": caregiver, "availability": availability}

    def display_schedule(self):
        """Display the schedule in a readable format"""
        for day, shifts in self.schedule.items():
            print(f"Day {day}:")
            for shift, details in shifts.items():
                if details:
                    caregiver = details["caregiver"]
                    availability = details["availability"]
                    print(f"  {shift} - Caregiver: {caregiver.name} | Availability: {availability}")
                else:
                    print(f"  {shift} - No caregiver assigned")

# Example of using the Schedule class
if __name__ == "__main__":
    scheduler = Schedule(11, 2023)
    caregiver1 = Caregiver("John Doe", "555-1234", "johndoe@example.com", 20)
    scheduler.set_availability(caregiver1, 1, "AM", "available")
    scheduler.display_schedule()
