class Payroll:
    def __init__(self):
        """
        Initialize the Payroll system with an empty list to store caregivers.
        """
        self.caregivers = []  # List to store caregivers for payroll processing

    def add_caregiver(self, caregiver):
        """
        Add a caregiver to the payroll system.
        :param caregiver: An instance of the Caregiver class.
        """
        self.caregivers.append(caregiver)

    def calculate_weekly_pay(self):
        """
        Calculate the weekly pay for each caregiver based on their logged hours.
        :return: A list of dictionaries containing the caregiver's name, hours worked, and gross pay.
        """
        report = []
        for caregiver in self.caregivers:
            # Calculate gross pay by multiplying hours worked by the pay rate
            gross_pay = caregiver.hours_worked * caregiver.pay_rate
            report.append({
                "Name": caregiver.name,
                "Hours Worked": caregiver.hours_worked,
                "Gross Pay": f"${gross_pay:.2f}"  # Format gross pay as a string with two decimal places
            })
        return report

    def display_weekly_report(self):
        """
        Display the weekly payroll report for all caregivers.
        """
        report = self.calculate_weekly_pay()  # Generate the payroll report
        print("\nWeekly Payroll Report")
        print("=====================")
        total_pay = 0  # Variable to track the total payroll amount
        for entry in report:
            total_pay += float(entry["Gross Pay"].strip('$'))  # Sum up the total gross pay
            print(f"{entry['Name']}: Hours Worked - {entry['Hours Worked']}, Gross Pay - {entry['Gross Pay']}")
        print(f"Total Weekly Payroll: ${total_pay:.2f}")  # Display the total payroll amount

# Example test
caregiver1 = Caregiver("Alice", "123-456-7890", "alice@example.com", 20.0)  # Create a caregiver instance
caregiver2 = Caregiver("Bob", "987-654-3210", "bob@example.com", 22.0)  # Create another caregiver instance

caregiver1.hours_worked = 35  # Set hours worked for the first caregiver
caregiver2.hours_worked = 40  # Set hours worked for the second caregiver

payroll = Payroll()  # Create a Payroll instance
payroll.add_caregiver(caregiver1)  # Add the first caregiver to the payroll
payroll.add_caregiver(caregiver2)  # Add the second caregiver to the payroll

payroll.display_weekly_report()  # Display the weekly payroll report
