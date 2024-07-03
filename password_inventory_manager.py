from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    # Add authentication logic here
    if username == "admin" and password == "admin123":  # Sample logic User and Pass
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
