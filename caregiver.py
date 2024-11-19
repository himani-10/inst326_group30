from datetime import datetime

class Caregiver:
    def __init__(self, name: str, phone: str, email: str, pay_rate: float):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours_worked = 0
        self.schedule = {}

    def update_contact_info(self, phone: str = None, email: str = None):
        if phone:
            self.phone = phone
        if email:
            self.email = email

    def log_hours(self, date: datetime, shift: str, hours: float):
        date_str = date.strftime('%Y-%m-%d')
        if date_str in self.schedule:
            print(f"Warning: {self.name} already has a shift on {date_str}.")
        self.schedule[date_str] = shift
        self.hours_worked += hours
        print(f"{self.name} worked {hours} hours on {date_str} during the {shift} shift.")

    def display_schedule(self):
        print(f"\nSchedule for {self.name}:")
        for date, shift in self.schedule.items():
            print(f" - {date}: {shift}")

class CareManager:
    def __init__(self):
        self.caregivers = {}
        self.shifts = {
            "morning": (7, 13),
            "afternoon": (13, 19)
        }

    def add_caregiver(self, name: str, phone: str, email: str, pay_rate: float):
        if name in self.caregivers:
            print(f"Caregiver '{name}' already exists.")
            return
        caregiver = Caregiver(name, phone, email, pay_rate)
        self.caregivers[name] = caregiver
        print(f"Added caregiver: {name}")

    def update_caregiver_info(self, name: str, phone: str = None, email: str = None):
        caregiver = self.caregivers.get(name)
        if caregiver:
            caregiver.update_contact_info(phone, email)
            print(f"Updated contact info for {name}.")
        else:
            print(f"Caregiver '{name}' not found.")

    def assign_shift(self, caregiver_name: str, date: datetime, shift_type: str):
        if caregiver_name not in self.caregivers:
            print(f"Caregiver '{caregiver_name}' not found.")
            return
        if shift_type not in self.shifts:
            print(f"Invalid shift type '{shift_type}'. Use 'morning' or 'afternoon'.")
            return
        hours = self.shifts[shift_type][1] - self.shifts[shift_type][0]
        self.caregivers[caregiver_name].log_hours(date, shift_type, hours)

    def display_schedule(self):
        for caregiver in self.caregivers.values():
            caregiver.display_schedule()

    def get_total_hours(self, name: str):
        caregiver = self.caregivers.get(name)
        if caregiver:
            print(f"{name} has worked {caregiver.hours_worked} hours.")
        else:
            print(f"Caregiver '{name}' not found.")

    def get_daily_caregivers(self, date: datetime):
        date_str = date.strftime('%Y-%m-%d')
        print(f"\nCaregivers on duty for {date_str}:")
        for caregiver in self.caregivers.values():
            shift = caregiver.schedule.get(date_str)
            if shift:
                print(f" - {caregiver.name}: {shift}")

# Example test
manager = CareManager()
manager.add_caregiver("Alice", "123-456-7890", "alice@example.com", 20.0)
manager.add_caregiver("Bob", "987-654-3210", "bob@example.com", 22.0)

date = datetime.now()
manager.assign_shift("Alice", date, "morning")
manager.assign_shift("Bob", date, "afternoon")

manager.display_schedule()
manager.get_daily_caregivers(date)
