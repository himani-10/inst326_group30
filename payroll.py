class Payroll:
    def __init__(self):
        self.caregivers = []

    def add_caregiver(self, caregiver):
        self.caregivers.append(caregiver)

    def calculate_weekly_pay(self):
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
        report = self.calculate_weekly_pay()
        print("\nWeekly Payroll Report")
        print("=====================")
        total_pay = 0
        for entry in report:
            total_pay += float(entry["Gross Pay"].strip('$'))
            print(f"{entry['Name']}: Hours Worked - {entry['Hours Worked']}, Gross Pay - {entry['Gross Pay']}")
        print(f"Total Weekly Payroll: ${total_pay:.2f}")

# Example test
caregiver1 = Caregiver("Alice", "123-456-7890", "alice@example.com", 20.0)
caregiver2 = Caregiver("Bob", "987-654-3210", "bob@example.com", 22.0)

caregiver1.hours_worked = 35
caregiver2.hours_worked = 40

payroll = Payroll()
payroll.add_caregiver(caregiver1)
payroll.add_caregiver(caregiver2)

payroll.display_weekly_report()
