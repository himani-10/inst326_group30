from datetime import datetime

class Caregiver:
    def __init__(self, name: str, phone: str, email: str, pay_rate: float):
        """
        Initialize a caregiver with essential details.
        :param name: Caregiver's name.
        :param phone: Caregiver's phone number.
        :param email: Caregiver's email address.
        :param pay_rate: Caregiver's hourly pay rate.
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours_worked = 0  # Tracks total hours worked
        self.schedule = {}  # Dictionary to store shifts {date: shift}

    def update_contact_info(self, phone: str = None, email: str = None):
        """Update caregiver's contact information if provided."""
        if phone:
            self.phone = phone
        if email:
            self.email = email

    def log_hours(self, date: datetime, shift: str, hours: float):
        """
        Log hours worked by the caregiver on a specific date and shift.
        :param date: The date of the work shift.
        :param shift: The type of shift (e.g., 'AM' or 'PM').
        :param hours: Number of hours worked.
        """
        date_str = date.strftime('%Y-%m-%d')
        # Check if the caregiver already has a shift on the given date
        if date_str in self.schedule:
            print(f"Warning: {self.name} already has a shift on {date_str}.")
        self.schedule[date_str] = shift  # Record the shift
        self.hours_worked += hours  # Add hours to total
        print(f"{self.name} logged {hours} hours on {date_str} for {shift} shift.")

    def display_schedule(self):
        """Display the caregiver's scheduled shifts."""
        print(f"\nSchedule for {self.name}:")
        for date, shift in self.schedule.items():
            print(f" - {date}: {shift}")


class CareManager:
    def __init__(self):
        """Manage a collection of caregivers."""
        self.caregivers = {}  # Dictionary of caregivers {name: Caregiver}
        self.shifts = {
            "morning": (7, 13),  # Morning shift from 7 AM to 1 PM
            "afternoon": (13, 19)  # Afternoon shift from 1 PM to 7 PM
        }

    def add_caregiver(self, name: str, phone: str, email: str, pay_rate: float):
        """Add a new caregiver to the system."""
        if name in self.caregivers:
            print(f"Caregiver '{name}' already exists.")
            return
        caregiver = Caregiver(name, phone, email, pay_rate)
        self.caregivers[name] = caregiver
        print(f"Added caregiver: {name}")

    def update_caregiver_info(self, name: str, phone: str = None, email: str = None):
        """Update the contact information of a caregiver."""
        caregiver = self.caregivers.get(name)
        if caregiver:
            caregiver.update_contact_info(phone, email)
            print(f"Updated contact info for {name}.")
        else:
            print(f"Caregiver '{name}' not found.")

    def assign_shift(self, caregiver_name: str, date: datetime, shift_type: str):
        """
        Assign a shift to a caregiver on a given date.
        :param caregiver_name: Name of the caregiver.
        :param date: Date of the shift.
        :param shift_type: Shift type ('morning' or 'afternoon').
        """
        if caregiver_name not in self.caregivers:
            print(f"Caregiver '{caregiver_name}' not found.")
            return
        if shift_type not in self.shifts:
            print(f"Invalid shift type '{shift_type}'. Options: 'morning', 'afternoon'.")
            return
        # Calculate hours for the shift
        hours = self.shifts[shift_type][1] - self.shifts[shift_type][0]
        self.caregivers[caregiver_name].log_hours(date, shift_type, hours)

    def display_schedule(self):
        """Display schedules for all caregivers."""
        for caregiver in self.caregivers.values():
            caregiver.display_schedule()

    def get_total_hours(self, name: str):
        """Display total hours worked by a caregiver."""
        caregiver = self.caregivers.get(name)
        if caregiver:
            print(f"{name} has worked {caregiver.hours_worked} hours.")
        else:
            print(f"Caregiver '{name}' not found.")

    def get_daily_caregivers(self, date: datetime):
        """
        Display caregivers working on a specific date.
        :param date: Date to check.
        """
        date_str = date.strftime('%Y-%m-%d')
        print(f"\nCaregivers on duty for {date_str}:")
        for caregiver in self.caregivers.values():
            shift = caregiver.schedule.get(date_str)
            if shift:
                print(f" - {caregiver.name}: {shift}")

# Example usage
if __name__ == "__main__":
    manager = CareManager()
    manager.add_caregiver("Alice", "123-456-7890", "alice@example.com", 20.0)
    manager.add_caregiver("Bob", "987-654-3210", "bob@example.com", 22.0)

    date = datetime.now()
    manager.assign_shift("Alice", date, "morning")
    manager.assign_shift("Bob", date, "afternoon")

    manager.display_schedule()
    manager.get_daily_caregivers(date)
