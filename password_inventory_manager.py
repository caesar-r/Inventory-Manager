from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, ttk
#import json 

# Sample tool list for draft (remove when done)
tools = [f"Tool {i}" for i in range(1,1001)]
employees = ["Employee 1", "Employee 2", "Employee 3"]

# This function will handle the login to the program
def login():
    username = username_entry.get()
    password = password_entry.get()
    # Add authentication logic here
    if username == "" and password == "":  # Sample logic User and Pass (admin admin123)
        main_menu()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def main_menu():
    login_screen.destroy()
    main_screen = Tk()
    main_screen.title("Main Menu")

    Label(main_screen, text="Welcome to the Inventory Management System").pack()
    Button(main_screen, text="Tool Management", command=tool_management).pack()
    Button(main_screen, text="Employee Management", command=employee_management).pack()
    Button(main_screen, text="Borrow Tool", command=borrow_tool).pack()
    Button(main_screen, text="Return Tool", command=return_tool).pack()
    Button(main_screen, text="Generate Reports", command=generate_reports).pack()

    main_screen.mainloop()

# This Function handles all the tool management such as naming the tools... 
# ...Adding them to the program with the quantity of tools and also being able to remove tools from the system 
def tool_management():
    tool_screen = Tk()
    tool_screen.title("Tool Management")

    Label(tool_screen, text="Add Tool").grid(row=0, column=0, columnspan=2)
    Label(tool_screen, text="Tool Name").grid(row=1, column=0)
    tool_name_entry = Entry(tool_screen)
    tool_name_entry.grid(row=1, column=1)

    Label(tool_screen, text="Quantity").grid(row=2, column=0)
    tool_quantity_entry = Entry(tool_screen)
    tool_quantity_entry.grid(row=2, column=1)

    Button(tool_screen, text="Add Tool", command=lambda: add_tool(tool_name_entry.get(), tool_quantity_entry.get())).grid(row=3, column=0, columnspan=2)

    Label(tool_screen, text="Remove Tool").grid(row=4, column=0, columnspan=2)
    Label(tool_screen, text="Tool ID").grid(row=5, column=0)
    tool_id_entry = Entry(tool_screen)
    tool_id_entry.grid(row=5, column=1)

    Button(tool_screen, text="Remove Tool", command=lambda: remove_tool(tool_id_entry.get())).grid(row=6, column=0, columnspan=2)

    tool_screen.mainloop()

def add_tool(name, quantity):
    # Add logic to add tool to inventory
    messagebox.showinfo("Success", f"Added {name} with quantity {quantity}")

def remove_tool(tool_id):
    # Add logic to remove tool from inventory
    messagebox.showinfo("Success", f"Removed tool with ID {tool_id}")

def employee_management():
    employee_screen = Tk()
    employee_screen.title("Employee Management")

    Label(employee_screen, text="Add Employee").grid(row=0, column=0, columnspan=2)
    Label(employee_screen, text="Employee Name").grid(row=1, column=0)
    employee_name_entry = Entry(employee_screen)
    employee_name_entry.grid(row=1, column=1)

    Label(employee_screen, text="Employee ID").grid(row=2, column=0)
    employee_id_entry = Entry(employee_screen)
    employee_id_entry.grid(row=2, column=1)

    Button(employee_screen, text="Add Employee", command=lambda: add_employee(employee_name_entry.get(), employee_id_entry.get())).grid(row=3, column=0, columnspan=2)

    Label(employee_screen, text="Remove Employee").grid(row=4, column=0, columnspan=2)
    Label(employee_screen, text="Employee ID").grid(row=5, column=0)
    employee_remove_id_entry = Entry(employee_screen)
    employee_remove_id_entry.grid(row=5, column=1)

    Button(employee_screen, text="Remove Employee", command=lambda: remove_employee(employee_remove_id_entry.get())).grid(row=6, column=0, columnspan=2)

    employee_screen.mainloop()

def add_employee(name, emp_id):
    # Add logic to add employee to the list
    messagebox.showinfo("Success", f"Added employee {name} with ID {emp_id}")

def remove_employee(emp_id):
    # Add logic to remove employee from the list
    messagebox.showinfo("Success", f"Removed employee with ID {emp_id}")

# Borrow tool function
def borrow_tool():
    borrow_screen = Tk()
    borrow_screen.title("Borrow Tool")

    Label(borrow_screen, text="Select Tool").grid(row=0, column=0)
    tool_selection = StringVar()
    tool_combobox = ttk.Combobox(borrow_screen, textvariable=tool_selection)
    tool_combobox['values'] = tools
    tool_combobox.grid(row=0, column=1)

    Label(borrow_screen, text="Select Employee").grid(row=1, column=0)
    employee_selection = StringVar()
    employee_combobox = ttk.Combobox(borrow_screen, textvariable=employee_selection)
    employee_combobox['values'] = employees
    employee_combobox.grid(row=1, column=1)

    Label(borrow_screen, text="Date Borrowed").grid(row=2, column=0)
    date_borrowed_entry = Entry(borrow_screen)
    date_borrowed_entry.grid(row=2, column=1)

    Label(borrow_screen, text="Return Date").grid(row=3, column=0)
    return_date_entry = Entry(borrow_screen)
    return_date_entry.grid(row=3, column=1)

    Button(borrow_screen, text="Borrow Tool", command=lambda: borrow_tool_action(tool_selection.get(), employee_selection.get(), date_borrowed_entry.get(), return_date_entry.get())).grid(row=4, column=0, columnspan=2)

    borrow_screen.mainloop()

    def borrow_tool_action(tool, employee, date_borrowed, return_date):
        # Add logic to borrow tool
        messagebox.showinfo(f"Success {employee} borrowed {tool} from {date_borrowed} to {return_date}")

# Return tool function
def return_tool():
    return_screen = Tk()
    return_screen.title("Return Tool")

    Label(return_screen, text="Select Tool").grid(row=0, column=0)
    tool_selection = StringVar()
    tool_combobox = ttk.Combobox(return_screen, textvariable=tool_selection)
    tool_combobox['values'] = tools
    tool_combobox.grid(row=0, column=1)

    Label(return_screen, text="Select Employee").grid(row=1, column=0)
    employee_selection = StringVar()
    employee_combobox = ttk.Combobox(return_screen, textvariable=employee_selection)
    employee_combobox['values'] = employees
    employee_combobox.grid(row=1, column=1)

    Button(return_screen, text="Return Tool", command=lambda: return_tool_action(tool_selection.get(), employee_selection.get())).grid(row=2, column=0, columnspan=2)

    return_screen.mainloop()

def return_tool_action(tool, employee):
    # Add logic to return tool
    messagebox.showinfo(f"Success {employee} returned {tool}")




# Keep this part of the code below everything else
# Main entry point of the code
login_screen = Tk()
login_screen.title("Login")

Label(login_screen, text="Username").pack()
username_entry = Entry(login_screen)
username_entry.pack()

Label(login_screen, text="Password").pack()
password_entry = Entry(login_screen, show='*')
password_entry.pack()

Button(login_screen, text="Login", command=login).pack()

login_screen.mainloop()