
from datetime import datetime, timedelta
from typing import List, Dict

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
        self.schedule[date.strftime('%Y-%m-%d')] = shift
        self.hours_worked += hours
        print(f"{self.name} worked {hours} hours on {date.strftime('%Y-%m-%d')} during {shift}")

class CareManager:
    def __init__(self):
        self.caregivers: Dict[str, Caregiver] = {}
        self.shifts = {
            "morning": (7, 13),
            "afternoon": (13, 19)
        }
        
    def add_caregiver(self, name: str, phone: str, email: str, pay_rate: float):
        caregiver = Caregiver(name, phone, email, pay_rate)
        self.caregivers[name] = caregiver
        print(f"Added caregiver: {name}")
        
    def update_caregiver_info(self, name: str, phone: str = None, email: str = None):
        if name in self.caregivers:
            self.caregivers[name].update_contact_info(phone, email)
    
    def assign_shift(self, caregiver_name: str, date: datetime, shift_type: str):
        if caregiver_name in self.caregivers and shift_type in self.shifts:
            hours = self.shifts[shift_type][1] - self.shifts[shift_type][0]
            self.caregivers[caregiver_name].log_hours(date, shift_type, hours)
    
    def display_schedule(self):
        for name, caregiver in self.caregivers.items():
            print(f"\nSchedule for {name}:")
            for date, shift in caregiver.schedule.items():
                print(f" - {date}: {shift}")
    
    def get_total_hours(self, name: str):
        if name in self.caregivers:
            print(f"{name} has worked {self.caregivers[name].hours_worked} hours.")

    
    def get_daily_caregivers(self, date: datetime):
        caregivers_on_shift = {shift: [] for shift in self.shifts}
        for caregiver in self.caregivers.values():
            shift = caregiver.schedule.get(date.strftime('%Y-%m-%d'))
            if shift:
                caregivers_on_shift[shift].append(caregiver.name)
        print(f"\nCaregivers on duty for {date.strftime('%Y-%m-%d')}:")
        for shift, caregivers in caregivers_on_shift.items():
            print(f" - {shift.capitalize()}: {', '.join(caregivers) if caregivers else 'None'}")


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

class Caregiver:
    def __init__(self, name, pay_rate):
        self.__name = name  
        self.__pay_rate = pay_rate  
        self.__weekly_hours = 0  

    # Method to log hours worked for the week
    def log_hours(self, hours):
        if hours < 0:
            raise ValueError("Hours cannot be negative.")
        self.__weekly_hours = hours

    # Method to calculate weekly pay
    def calculate_weekly_pay(self):
        return self.__weekly_hours * self.__pay_rate

    # Getter to access the caregiver's name 
    def get_name(self):
        return self.__name

# Function to generate a payroll report for a list of caregivers
def generate_payroll_report(caregivers):
    total_pay = 0
    report = []
    for caregiver in caregivers:
        weekly_pay = caregiver.calculate_weekly_pay()
        total_pay += weekly_pay
        report.append(f"{caregiver.get_name()}: ${weekly_pay}")
    report.append(f"Total Weekly Pay: ${total_pay}")
    return report
