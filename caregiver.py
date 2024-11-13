from datetime import datetime, timedelta
from typing import List, Dict

class Caregiver:
    def __init__(self, name: str, phone: str, email: str, pay_rate: float):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours_worked = 0
        self.schedule = {}  # Dictionary with date keys and shift times as values
    
    def update_contact_info(self, phone: str = None, email: str = None):
        if phone:
            self.phone = phone
        if email:
            self.email = email
        print(f"Updated contact info for {self.name}")
    
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
        else:
            print(f"Caregiver {name} not found.")
    
    def assign_shift(self, caregiver_name: str, date: datetime, shift_type: str):
        if caregiver_name in self.caregivers and shift_type in self.shifts:
            hours = self.shifts[shift_type][1] - self.shifts[shift_type][0]
            self.caregivers[caregiver_name].log_hours(date, shift_type, hours)
        else:
            print(f"Invalid caregiver or shift type.")
    
    def display_schedule(self):
        for name, caregiver in self.caregivers.items():
            print(f"\nSchedule for {name}:")
            for date, shift in caregiver.schedule.items():
                print(f" - {date}: {shift}")
    
    def get_total_hours(self, name: str):
        if name in self.caregivers:
            print(f"{name} has worked {self.caregivers[name].hours_worked} hours.")
        else:
            print(f"Caregiver {name} not found.")
    
    def get_daily_caregivers(self, date: datetime):
        caregivers_on_shift = {shift: [] for shift in self.shifts}
        for caregiver in self.caregivers.values():
            shift = caregiver.schedule.get(date.strftime('%Y-%m-%d'))
            if shift:
                caregivers_on_shift[shift].append(caregiver.name)
        print(f"\nCaregivers on duty for {date.strftime('%Y-%m-%d')}:")
        for shift, caregivers in caregivers_on_shift.items():
            print(f" - {shift.capitalize()}: {', '.join(caregivers) if caregivers else 'None'}")
