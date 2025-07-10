# Application Interface: Main function
from app_functions import menu, menu_return, add, remove, modify, search, summary_stats, plot_amounts, plot_provider_appts

def main():
    while True:
        # define chosen menu item
        choice = menu()

        # add row
        if choice == '1': 
            try:
                print("\n**************************\n")
                print("You have chosen to add a row.")
                table = input("Specify whether the new record is a Patient, Provider, Appointment, or Bill: ")

                if table == "Patient":
                    print("\nPlease enter the patient's information in the specified format below:")
                    print("ID number, name, date of birth (YYYY-MM-DD), phone number, address (no commas)")
                    val = input("List of values to add: ").split(',')
                    add(table, val)

                elif table == "Provider":
                    print("\nPlease enter the provider's information in the specified format below:")
                    print("ID number, name, phone, email, specialty")
                    val = input("List of values to add: ").split(',')
                    add(table, val)

                elif table == "Appointment":
                    print("\nPlease enter the appointment information in the specified format below:")
                    print("ID number, date (YYYY-MM-DD), patient ID number, provider ID number, diagnosis")
                    val = input("List of values to add: ").split(',')
                    add(table, val)

                elif table == "Bill":
                    print("\nPlease enter the bill information in the specified format below:")
                    print("ID number, date (YYYY-MM-DD), patient ID number, amount, status (Unpaid, Paid, or Cancelled)")
                    val = input("List of values to add: ").split(',')
                    add(table, val)

                else: # input validation
                    table = input("Invalid input. Please enter the table name (Patient, Provider, Appointment, or Bill, case sensitive): ")
                
                print("\nYour record was added successfully. Do you wish to continue?")
                menu_return()

            except Exception as e:
                print(f"\nAttempt to add record failed. \n{e}")
                menu_return()

        # delete row
        elif choice == '2':
            try:
                print("\n**************************\n")
                print("You have chosen to delete a row.")
                table = input("Enter the name of the table the record is located in: ")
                id = input("Enter the ID number of the record you wish to delete: ")
                remove(table, id)

                print("\nYour record was deleted successfully. Do you wish to continue?")
                menu_return()

            except Exception as e:
                print(f"\nAttempt to delete record failed. \n{e}")
                menu_return()
        
        # edit row
        elif choice == '3': 
            try:
                print("\n**************************\n")
                print("You have chosen to edit a row.")
                table = input("Enter the name of the table the record is located in: ")
                id = input("Enter the ID number of the record you wish to edit: ")
                if table == "Patient":
                    print("\nColumn options:patient_id, name, dob (birth date), phone, address\n") 
                    col = input("Enter the name of the column you wish to edit: ")

                elif table == "Provider":
                    print("\nColumn options:provider_id, name, phone, email, speciality\n") 
                    col = input("Enter the name of the column you wish to edit: ")

                elif table == "Appointment": 
                    print("\nColumn options:appt_id, appt_date, patient_id, provider_id, diagnosis\n") 
                    col = input("Enter the name of the column you wish to edit: ")
                
                elif table == "Bill":
                    print("\nColumn options:bill_id, date, patient_id, amount, status (Paid, Unpaid, or Cancelled)\n") 
                    col = input("Enter the name of the column you wish to edit: ")

                if col == 'date':
                    new = input("Enter the new date in this format (YYYY-MM-DD): ")
                elif col == 'status':
                    new = input("Enter the new status value (Paid, Unpaid, or Cancelled): ")
                elif col == 'specialty':
                    print("\nSpecialty Options:\nPediatrics, Cardiology, Psychiatry, Dermatology, Neurology, Oncology, General Medicine\n")
                    new = input("Enter the new specialty: ")
                else:
                    new = input("Enter the new value: ")

                modify(table, id, col, new)

                print("\nYour record was changed successfully. Do you wish to continue?")
                menu_return()

            except Exception as e:
                print(f"\nAttempt to edit record failed. \n{e}")
                menu_return()
        
        # search for row
        elif choice == '4':
            try:
                print("\n**************************\n")
                print("You have chosen to search for a row.")
                table = input("Specify whether you're searching for a Patient, Provider, Appointment, or Bill: ")
                if table == "Patient":
                    print("Column options:\npatient_id, name, dob (birth date), phone, address\n") 
                    column = input("Enter the name of the column you wish to search with: ")
                elif table == "Provider":
                    print("Column options:\nprovider_id, name, phone, email, speciality\n") 
                    column = input("Enter the name of the column you wish to search with: ")
                elif table == "Appointment": 
                    print("Column options:\nappt_id, appt_date, patient_id, provider_id, diagnosis\n") 
                    column = input("Enter the name of the column you wish to search with: ")
                elif table == "Bill":
                    print("Column options:\nbill_id, date, patient_id, amount, status (Paid, Unpaid, or Cancelled)\n") 
                    column = input("Enter the name of the column you wish to search with: ")

                if col == 'date':
                    value = input("Enter the desired date in this format (YYYY-MM-DD): ")
                elif col == 'status':
                    value = input("Enter the desired status value (Paid, Unpaid, or Cancelled): ")
                elif col == 'specialty':
                    print("\nSpecialty Options:\nPediatrics, Cardiology, Psychiatry, Dermatology, Neurology, Oncology, General Medicine\n")
                    value = input("Enter the desired specialty: ")
                else:
                    value = input("Enter the row value: ")
                search(table, column, value)

                print("\nDo you wish to continue?")
                menu_return()

            except Exception as e:
                print(f"\nRecord not found. \n{e}")
                menu_return()
        
        # summary statistics
        elif choice == '5':
            try:
                print("\n**************************\n")
                print("You have chosen to find summary statistics.")
                print("\nSummary Options:")
                print("1. Statistics for all bills")
                print("2. Bill Statistics for a specific patient")
                selection = input("\nSelect 1 or 2: ")
                summary_stats(selection)

                print("\nDo you wish to continue?")
                menu_return()

            except Exception as e:
                print(f"\nAttempt failed. \n{e}")
                menu_return()
        
        # figure selection
        elif choice == "6":
            try:
                print("\n**************************\n")
                print("You have chosen to view a graph.")
                print("\nAvailable Figures:")
                print("1. Histogram Distribution of the Amounts of Bills")
                print("2. Bar Graph of the Number of Appointments by Provider")
                graph = input("\nSelect a graph to view (1 or 2): ")
                if graph == '1':
                    plot_amounts()
                elif graph == '2':   
                    plot_provider_appts()

                print("\nDo you wish to continue?")
                menu_return()

            except Exception as e:
                print(f"\nAttempt to show graph failed. \n{e}")
                menu_return()
        
        # exit program
        elif choice == '7':
            print("\nThank you for using the Burlington Health Center Interface.")
            exit()
    
        # input validation
        else:
            print("\nInvalid Input.")
            choice = input ("Please select 1, 2, 3, 4, 5, or 6: ")

if __name__ == "__main__":
    main()