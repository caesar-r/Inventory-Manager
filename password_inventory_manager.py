from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    # Add authentication logic here
    if username == "admin" and password == "admin123":  # Sample logic
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
