from datetime import datetime
from caregiver import CareManager, Caregiver
from scheduler import Schedule
from payroll import Payroll

def main():
    print("Welcome to the Caregiver Management System")

    # Initialize systems
    care_manager = CareManager()
    payroll_system = Payroll()
    month = int(input("Enter month (as a number 1-12) for scheduling: "))
    year = int(input("Enter year for scheduling: "))
    schedule = Schedule(month, year)

    # Add example caregivers (you can modify or prompt for real input)
    care_manager.add_caregiver("Alice", "123-456-7890", "alice@example.com", 20.0)
    care_manager.add_caregiver("Bob", "987-654-3210", "bob@example.com", 22.0)

    # Add caregivers to payroll
    for caregiver in care_manager.caregivers.values():
        payroll_system.add_caregiver(caregiver)

    while True:
        print("\nOptions:")
        print("1. View Caregiver Info")
        print("2. Update Caregiver Info")
        print("3. Assign Shift to Caregiver")
        print("4. View Monthly Schedule")
        print("5. Log Hours for Caregiver")
        print("6. Display Weekly Payroll Report")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            for caregiver in care_manager.caregivers.values():
                print(f"Name: {caregiver.name}, Phone: {caregiver.phone}, Email: {caregiver.email}, Pay Rate: ${caregiver.pay_rate}/hr")

        elif choice == '2':
            name = input("Enter caregiver's name to update: ")
            phone = input("Enter new phone (press enter to skip): ")
            email = input("Enter new email (press enter to skip): ")
            care_manager.update_caregiver_info(name, phone, email)

        elif choice == '3':
            name = input("Enter caregiver's name: ")
            date_input = input("Enter date (YYYY-MM-DD): ")
            shift_type = input("Enter shift type ('morning' or 'afternoon'): ")
            try:
                date = datetime.strptime(date_input, "%Y-%m-%d")
                care_manager.assign_shift(name, date, shift_type)
                schedule.set_availability(care_manager.caregivers[name], date.day, "AM" if shift_type == "morning" else "PM", "assigned")
            except ValueError:
                print("Invalid date format. Please enter as YYYY-MM-DD.")

        elif choice == '4':
            schedule.display_schedule()

        elif choice == '5':
            name = input("Enter caregiver's name: ")
            hours = float(input("Enter hours worked: "))
            caregiver = care_manager.caregivers.get(name)
            if caregiver:
                date = datetime.now()  # Assuming current date; you can prompt for specific dates
                caregiver.log_hours(date, "custom shift", hours)
            else:
                print("Caregiver not found.")

        elif choice == '6':
            payroll_system.display_weekly_report()

        elif choice == '7':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
