class Payroll:
    def __init__(self):
        """Initialize the payroll system."""
        self.caregivers = []

    def add_caregiver(self, caregiver):
        """Add a caregiver to the payroll system."""
        self.caregivers.append(caregiver)

    def calculate_weekly_pay(self):
        """Calculate weekly pay for each caregiver based on logged hours."""
        report = []
        for caregiver in self.caregivers:
            gross_pay = caregiver.hours_worked * caregiver.pay_rate
            report.append({
                "Name": caregiver.name,
                "Hours Worked": caregiver.hours_worked,
                "Gross Pay": f"${gross_pay:.2f}"
            })
        return report

    def display_weekly_report(self):
        """Display the weekly payroll report."""
        report = self.calculate_weekly_pay()
