def main():
    print("Welcome to the Caregiver Management System")

    # Initialize CareManager, Payroll, and Schedule
    care_manager = CareManager()
    payroll_system = Payroll()
    month = int(input("Enter month (1-12) for scheduling: "))  # Prompt for month input
    year = int(input("Enter year for scheduling: "))  # Prompt for year input
    schedule = Schedule(month, year)

    # Adding example caregivers (modify as needed)
    care_manager.add_caregiver("Alice", "123-456-7890", "alice@example.com", 20.0)
    care_manager.add_caregiver("Bob", "987-654-3210", "bob@example.com", 22.0)

    # Add caregivers to the payroll system
    for caregiver in care_manager.caregivers.values():
        payroll_system.add_caregiver(caregiver)

    # Main loop for menu interaction
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
            # Display all caregivers' information
            for caregiver in care_manager.caregivers.values():
                print(f"Name: {caregiver.name}, Phone: {caregiver.phone}, Email: {caregiver.email}, Pay Rate: ${caregiver.pay_rate}/hr")

        elif choice == '2':
            # Update caregiver contact information
            name = input("Enter caregiver's name to update: ")
            phone = input("Enter new phone (press enter to skip): ")
            email = input("Enter new email (press enter to skip): ")
            care_manager.update_caregiver_info(name, phone, email)

        elif choice == '3':
            # Assign a shift to a caregiver
            name = input("Enter caregiver's name: ")
            date_input = input("Enter date (YYYY-MM-DD): ")
            shift_type = input("Enter shift type ('morning' or 'afternoon'): ")
            try:
                date = datetime.strptime(date_input, "%Y-%m-%d")
                care_manager.assign_shift(name, date, shift_type)
                shift_code = "AM" if shift_type == "morning" else "PM"
                if name in care_manager.caregivers:
                    schedule.set_availability(care_manager.caregivers[name], date.day, shift_code, "assigned")
                else:
                    print(f"Caregiver '{name}' not found.")
            except ValueError:
                print("Invalid date format. Please enter as YYYY-MM-DD.")

        elif choice == '4':
            # View the monthly schedule
            schedule.display_schedule()

        elif choice == '5':
            # Log hours worked for a caregiver
            name = input("Enter caregiver's name: ")
            hours = float(input("Enter hours worked: "))
            caregiver = care_manager.caregivers.get(name)
            if caregiver:
                date = datetime.now()  # Use current date for logging hours
                caregiver.log_hours(date, "custom shift", hours)
            else:
                print("Caregiver not found.")

        elif choice == '6':
            # Display the weekly payroll report
            payroll_system.display_weekly_report()

        elif choice == '7':
            # Exit the program
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main function
main()
