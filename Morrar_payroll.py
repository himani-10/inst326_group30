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





