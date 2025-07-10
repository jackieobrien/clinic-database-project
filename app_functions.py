# Application Interface Functions
import sqlite3
import statistics
import matplotlib.pyplot as plt

# open sqlite database
con = sqlite3.connect("clinicData.db")
cur = con.cursor()

# function to display interface options upon run
def menu():
    print("\n**************************\n")
    print("Welcome to the Burlington Health Center Interface.\n")
    print("1. Add a Record")
    print("2. Remove a Record")
    print("3. Modify a Record")
    print("4. Search for a Record")
    print("5. View the Summary Statistics of Bill Amounts")
    print("6. Build a Graph")
    print("7. Close")

    selection = input("\nChoose an option: ")
    if 1 <= int(selection) <= 7:
        return selection
    else:
        selection = input("Invalid Input. Please choose a menu option (1, 2, 3, 4, 5, 6, 7): ")

# function to return to menu
def menu_return():
    menu_option = input("Enter 'y' to return to the menu, and 'n' to quit the interface. ")
    if menu_option == 'y':
        menu()
    elif menu_option == 'n':
        print("\nThank you for using the Burlington Health Center Interface.")
        exit()

# function to add record
def add(table, row):
    query = f"INSERT INTO {table} VALUES ({', '.join(['?'] * len(row))});"
    cur.execute(query, row)


# function to remove record
def remove(table, row):
    if table == "Patient":
        query = f"DELETE FROM {table} WHERE patient_id = ?;"
        cur.execute(query, (row, ))
    elif table == "Provider":
        query = f"DELETE FROM {table} WHERE provider_id = ?;"
        cur.execute(query, (row, ))
    elif table == "Appointment":
        query = f"DELETE FROM {table} WHERE appt_id = ?;"
        cur.execute(query, (row, ))
    elif table == "Bill":
        query = f"DELETE FROM {table} WHERE bill_id = ?;"
        cur.execute(query, (row, ))

# function to modify record
def modify(table, id, column, value):
    if table == "Patient":
        query = f"UPDATE {table} SET {column} = ? WHERE patient_id = ?;"
        cur.execute(query, (value, id))
    elif table == "Provider":
        query = f"UPDATE {table} SET {column} = ? WHERE provider_id = ?;"
        cur.execute(query, (value, id))
    elif table == "Appointment":
        query = f"UPDATE {table} SET {column} = ? WHERE appt_id = ?;"
        cur.execute(query, (value, id))
    elif table == "Bill":
        query = f"UPDATE {table} SET {column} = ? WHERE bill_id = ?;"
        cur.execute(query, (value, id))
    

# function to search for any record in the database
def search(table, column, value):
    query = f"SELECT * FROM {table} WHERE {column} = ?;"
    cur.execute(query, (value, ))
    display = cur.fetchall()
    if display:
        for i in display:
            print(i)
    else:
        print("\nNo records matching that information were found.")

# function to compute summary statistics of bill totals
def summary_stats(choice):
    # all bills
    if choice == '1':
        cur.execute("SELECT amount FROM Bill;")
        amounts = [row[0] for row in cur.fetchall()]
        print("All bills selected.\nSummary:")
        print(f"Mean: ${(sum(amounts) / len(amounts)):.2f}")
        print(f"Median: ${statistics.median(amounts):.2f}")
        print(f"Minimum: ${min(amounts)}")
        print(f"Maximum: ${max(amounts)}")
        print(f"Mean Standard Deviation: {statistics.stdev(amounts):.2f}")
    
    # bills for specific patient
    elif choice == '2':
        try:
            id = input("Enter the ID number of the patient: ")
            query = f"SELECT amount FROM Bill WHERE patient_id = ?;"
            cur.execute(query, (id, ))
            amounts = [row[0] for row in cur.fetchall()]
            print("Summary:")
            print(f"Mean: ${statistics.mean(amounts):.2f}")
            print(f"Median: ${statistics.median(amounts):.2f}")
            print(f"Minimum: ${min(amounts)}")
            print(f"Maximum: ${max(amounts)}")
            print(f"Mean Standard Deviation: {statistics.stdev(amounts):.2f}")

        except ValueError:
            print("No bills found.")
    
    # input validation
    else:
        choice = input("Invalid Input.\nPlease enter 1, 2, or 3: ")
    con.commit()

    
# function to plot the distribution of bill amounts
def plot_amounts():
    print("\n**************************\n")
    # fetch bill amounts
    cur.execute("SELECT amount FROM Bill;")
    amounts = [row[0] for row in cur.fetchall()]

    # plot amounts
    plt.figure()
    plt.hist(amounts, bins = 20, color = 'mediumorchid', edgecolor = 'black')
    plt.title("Distribution of Bill Amounts")
    plt.xlabel("Amount ($)")
    plt.ylabel("Frequency")
    plt.show()

# function to plot the number of appointments per provider
def plot_provider_appts():
    print("\n**************************\n")
    # select
    cur.execute('''
        SELECT Provider.name, COUNT(Appointment.appt_id) FROM Appointment
        JOIN Provider ON Appointment.provider_id = Provider.provider_id
        GROUP BY Provider.provider_id
    ;''')
    df = cur.fetchall()
    providers = [row[0].split()[-1] for row in df]
    counts = [row[1] for row in df]
    plt.figure()
    plt.bar(providers, counts, color = "firebrick")
    plt.title("Appointment Counts by Provider")
    plt.xlabel("# of Appointments")
    plt.xticks(fontsize = 10, rotation = 45)
    plt.show()
