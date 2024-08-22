from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, ttk
import json
import datetime

# This is the main class for the system
# This contains the main screen function along with the... 
# ...password screen that will need to be completed before the user can enter the program 
class InventoryManagementSystem:
    def __init__(self):
        self.load_data()
        self.borrowed_tools = []
        self.login_screen = None
        self.main_screen = None
        self.font = ("Calibri", 11)
        self.bg_color = "#FFFFFF"
        self.text_color = "#231F20"
        self.button_color = "#00B1EF"
        self.start_login_screen()

    def load_data(self):
        # Load tools data
        try:
            with open("tools.json", "r") as tools_file:
                self.tools = json.load(tools_file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tools = {}
            messagebox.showerror("File Not Found", "tools.json not found or is empty. Starting with an empty tool list.")

        # Load employees data
        try:
            with open("employees.json", "r") as employees_file:
                self.employees = json.load(employees_file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.employees = {}
            messagebox.showerror("File Not Found", "employees.json not found or is empty. Starting with an empty employee list.")

    def save_tools_data(self):
        with open("tools.json", "w") as tools_file:
            json.dump(self.tools, tools_file, indent=4)

    def save_employees_data(self):
        with open("employees.json", "w") as employees_file:
            json.dump(self.employees, employees_file, indent=4)

    def start_login_screen(self):
        self.login_screen = Tk()
        self.login_screen.title("Login")
        self.login_screen.configure(bg=self.bg_color)

        Label(self.login_screen, text="Username", font=self.font, bg=self.bg_color, fg=self.text_color).pack()
        self.username_entry = Entry(self.login_screen, font=self.font)
        self.username_entry.pack()

        Label(self.login_screen, text="Password", font=self.font, bg=self.bg_color, fg=self.text_color).pack()
        self.password_entry = Entry(self.login_screen, show='*', font=self.font)
        self.password_entry.pack()

        Button(self.login_screen, text="Login", command=self.login, font=self.font, bg=self.button_color, fg=self.text_color).pack()
        self.login_screen.mainloop()
    # This function will handle the login to the code
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "" and password == "": # CHANGE TO A PASSWORD WHEN DONE
            self.start_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def start_main_menu(self):
        self.login_screen.destroy()
        self.main_screen = Tk()
        self.main_screen.title("Main Menu")
        self.main_screen.configure(bg=self.bg_color)

        Label(self.main_screen, text="Welcome to the Inventory Management System", font=self.font, bg=self.bg_color, fg=self.text_color).pack()
        Button(self.main_screen, text="Tool Management", command=self.start_tool_management, font=self.font, bg=self.button_color, fg=self.text_color).pack()
        Button(self.main_screen, text="Employee Management", command=self.start_employee_management, font=self.font, bg=self.button_color, fg=self.text_color).pack()
        Button(self.main_screen, text="Borrow Tool", command=self.start_borrow_tool, font=self.font, bg=self.button_color, fg=self.text_color).pack()
        Button(self.main_screen, text="Return Tool", command=self.start_return_tool, font=self.font, bg=self.button_color, fg=self.text_color).pack()
        Button(self.main_screen, text="Generate Reports", command=self.start_generate_reports, font=self.font, bg=self.button_color, fg=self.text_color).pack()

        self.main_screen.mainloop()

    def start_tool_management(self):
        tool_screen = ToolManagement(self.tools, self.save_tools_data, self.font, self.bg_color, self.text_color, self.button_color)
        tool_screen.show_screen()

    def start_employee_management(self):
        employee_screen = EmployeeManagement(self.employees, self.save_employees_data, self.font, self.bg_color, self.text_color, self.button_color)
        employee_screen.show_screen()

    def start_borrow_tool(self):
        borrow_screen = BorrowTool(self.tools, self.employees, self.borrowed_tools, self.save_tools_data, self.font, self.bg_color, self.text_color, self.button_color)
        borrow_screen.show_screen()

    def start_return_tool(self):
        return_screen = ReturnTool(self.tools, self.employees, self.borrowed_tools, self.save_tools_data, self.font, self.bg_color, self.text_color, self.button_color)
        return_screen.show_screen()

    def start_generate_reports(self):
        report_screen = ReportGeneration(self.tools, self.borrowed_tools, self.font, self.bg_color, self.text_color, self.button_color)
        report_screen.show_screen()

# This Function/class handles all the tool management such as naming the tools... 
# ...Adding them to the program with the quantity of tools and also being able to...
# ...remove tools from the system
class ToolManagement:
    def __init__(self, tools, save_data_callback, font, bg_color, text_color, button_color):
        self.tools = tools
        self.save_data_callback = save_data_callback
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.button_color = button_color
        self.tool_screen = None

    def show_screen(self):
        self.tool_screen = Tk()
        self.tool_screen.title("Tool Management")
        self.tool_screen.configure(bg=self.bg_color)

        Label(self.tool_screen, text="Add Tool", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, columnspan=2)
        Label(self.tool_screen, text="Tool Name", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=1, column=0)
        self.tool_name_entry = Entry(self.tool_screen, font=self.font)
        self.tool_name_entry.grid(row=1, column=1)

        Label(self.tool_screen, text="Quantity", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=2, column=0)
        self.tool_quantity_entry = Entry(self.tool_screen, font=self.font)
        self.tool_quantity_entry.grid(row=2, column=1)

        Button(self.tool_screen, text="Add Tool", command=self.add_tool, font=self.font, bg=self.button_color, fg=self.text_color).grid(row=3, column=0, columnspan=2)

        Label(self.tool_screen, text="Remove Tool", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=4, column=0, columnspan=2)
        Label(self.tool_screen, text="Tool ID", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=5, column=0)
        self.tool_id_entry = Entry(self.tool_screen, font=self.font)
        self.tool_id_entry.grid(row=5, column=1)

        Button(self.tool_screen, text="Remove Tool", command=self.remove_tool, font=self.font, bg=self.button_color, fg=self.text_color).grid(row=6, column=0, columnspan=2)

        self.tool_screen.mainloop()
# This function will add tools to the program when entered
    def add_tool(self):
        name = self.tool_name_entry.get()
        quantity = int(self.tool_quantity_entry.get())
        tool_id = len(self.tools) + 1
        self.tools[tool_id] = {"name": name, "quantity": quantity}
        self.save_data_callback()  # Save updated tools to JSON
        messagebox.showinfo("Success", f"Added {name} with quantity {quantity}")
# This program will remove tools from the system
    def remove_tool(self):
        tool_id = int(self.tool_id_entry.get())
        if tool_id in self.tools:
            del self.tools[tool_id]
            self.save_data_callback()  # Save updated tools to JSON
            messagebox.showinfo("Success", f"Removed tool with ID {tool_id}")
        else:
            messagebox.showerror("Error", f"No tool found with ID {tool_id}")


class EmployeeManagement:
    def __init__(self, employees, save_data_callback, font, bg_color, text_color, button_color):
        self.employees = employees
        self.save_data_callback = save_data_callback
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.button_color = button_color
        self.employee_screen = None

    def show_screen(self):
        self.employee_screen = Tk()
        self.employee_screen.title("Employee Management")
        self.employee_screen.configure(bg=self.bg_color)

        Label(self.employee_screen, text="Add Employee", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, columnspan=2)
        Label(self.employee_screen, text="Employee Name", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=1, column=0)
        self.employee_name_entry = Entry(self.employee_screen, font=self.font)
        self.employee_name_entry.grid(row=1, column=1)

        Label(self.employee_screen, text="Employee ID", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=2, column=0)
        self.employee_id_entry = Entry(self.employee_screen, font=self.font)
        self.employee_id_entry.grid(row=2, column=1)

        Button(self.employee_screen, text="Add Employee", command=self.add_employee, font=self.font, bg=self.button_color, fg=self.text_color).grid(row=3, column=0, columnspan=2)

        Label(self.employee_screen, text="Remove Employee", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=4, column=0, columnspan=2)
        Label(self.employee_screen, text="Employee ID", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=5, column=0)
        self.employee_remove_id_entry = Entry(self.employee_screen, font=self.font)
        self.employee_remove_id_entry.grid(row=5, column=1)

        Button(self.employee_screen, text="Remove Employee", command=self.remove_employee, font=self.font, bg=self.button_color, fg=self.text_color).grid(row=6, column=0, columnspan=2)

        self.employee_screen.mainloop()

    def add_employee(self):
        name = self.employee_name_entry.get()
        emp_id = len(self.employees) + 1
        self.employees[emp_id] = name
        self.save_data_callback()  # Save updated employees to JSON
        messagebox.showinfo("Success", f"Added employee {name} with ID {emp_id}")

    def remove_employee(self):
        emp_id = int(self.employee_remove_id_entry.get())
        if emp_id in self.employees:
            del self.employees[emp_id]
            self.save_data_callback()  # Save updated employees to JSON
            messagebox.showinfo("Success", f"Removed employee with ID {emp_id}")
        else:
            messagebox.showerror("Error", f"No employee found with ID {emp_id}")


class BorrowTool:
    def __init__(self, tools, employees, borrowed_tools, save_data_callback, font, bg_color, text_color, button_color):
        self.tools = tools
        self.employees = employees
        self.borrowed_tools = borrowed_tools
        self.save_data_callback = save_data_callback
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.button_color = button_color
        self.borrow_screen = None

    def show_screen(self):
        self.borrow_screen = Tk()
        self.borrow_screen.title("Borrow Tool")
        self.borrow_screen.configure(bg=self.bg_color)

        Label(self.borrow_screen, text="Select Tool", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=0, column=0)
        self.tool_selection = StringVar()
        self.tool_combobox = ttk.Combobox(self.borrow_screen, textvariable=self.tool_selection, font=self.font)
        self.tool_combobox['values'] = [self.tools[tool_id]['name'] for tool_id in self.tools]
        self.tool_combobox.grid(row=0, column=1)

        Label(self.borrow_screen, text="Select Employee", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=1, column=0)
        self.employee_selection = StringVar()
        self.employee_combobox = ttk.Combobox(self.borrow_screen, textvariable=self.employee_selection, font=self.font)
        self.employee_combobox['values'] = [self.employees[emp_id] for emp_id in self.employees]
        self.employee_combobox.grid(row=1, column=1)

        Label(self.borrow_screen, text="Date Borrowed", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=2, column=0)
        self.date_borrowed_entry = Entry(self.borrow_screen, font=self.font)
        self.date_borrowed_entry.grid(row=2, column=1)

        Label(self.borrow_screen, text="Return Date", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=3, column=0)
        self.return_date_entry = Entry(self.borrow_screen, font=self.font)
        self.return_date_entry.grid(row=3, column=1)

        Button(self.borrow_screen, text="Borrow Tool", command=self.borrow_tool_action, font=self.font, bg=self.button_color, fg=self.text_color).grid(row=4, column=0, columnspan=2)

        self.borrow_screen.mainloop()

    def borrow_tool_action(self):
        tool_name = self.tool_selection.get()
        employee_name = self.employee_selection.get()
        date_borrowed = self.date_borrowed_entry.get()
        return_date = self.return_date_entry.get()
        # Find the tool ID and reduce its quantity
        for tool_id, tool_info in self.tools.items():
            if tool_info['name'] == tool_name and tool_info['quantity'] > 0:
                self.tools[tool_id]['quantity'] -= 1
                self.borrowed_tools.append({
                    "tool_id": tool_id,
                    "employee": employee_name,
                    "date_borrowed": date_borrowed,
                    "return_date": return_date
                })
                self.save_data_callback()  # Save updated tools to JSON
                messagebox.showinfo("Success", f"{employee_name} borrowed {tool_name} from {date_borrowed} to {return_date}")
                return

        messagebox.showerror("Error", f"No available quantity for {tool_name}")


class ReturnTool:
    def __init__(self, tools, employees, borrowed_tools, save_data_callback, font, bg_color, text_color, button_color):
        self.tools = tools
        self.employees = employees
        self.borrowed_tools = borrowed_tools
        self.save_data_callback = save_data_callback
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.button_color = button_color
        self.return_screen = None

    def show_screen(self):
        self.return_screen = Tk()
        self.return_screen.title("Return Tool")
        self.return_screen.configure(bg=self.bg_color)

        Label(self.return_screen, text="Select Tool", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=0, column=0)
        self.tool_selection = StringVar()
        self.tool_combobox = ttk.Combobox(self.return_screen, textvariable=self.tool_selection, font=self.font)
        self.tool_combobox['values'] = [self.tools[tool_id]['name'] for tool_id in self.tools]
        self.tool_combobox.grid(row=0, column=1)

        Label(self.return_screen, text="Select Employee", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=1, column=0)
        self.employee_selection = StringVar()
        self.employee_combobox = ttk.Combobox(self.return_screen, textvariable=self.employee_selection, font=self.font)
        self.employee_combobox['values'] = [self.employees[emp_id] for emp_id in self.employees]
        self.employee_combobox.grid(row=1, column=1)

        Button(self.return_screen, text="Return Tool", command=self.return_tool_action, font=self.font, bg=self.button_color, fg=self.text_color).grid(row=2, column=0, columnspan=2)

        self.return_screen.mainloop()

    def return_tool_action(self):
        tool_name = self.tool_selection.get()
        employee_name = self.employee_selection.get()
        # Find the borrowed tool and return it
        for borrowed_tool in self.borrowed_tools:
            if borrowed_tool['tool_id'] in self.tools and borrowed_tool['employee'] == employee_name:
                self.tools[borrowed_tool['tool_id']]['quantity'] += 1
                self.borrowed_tools.remove(borrowed_tool)
                self.save_data_callback()  # Save updated tools to JSON
                messagebox.showinfo("Success", f"{employee_name} returned {tool_name}")
                return

        messagebox.showerror("Error", f"No record found for {employee_name} borrowing {tool_name}")


class ReportGeneration:
    def __init__(self, tools, borrowed_tools, font, bg_color, text_color, button_color):
        self.tools = tools
        self.borrowed_tools = borrowed_tools
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.button_color = button_color
        self.report_screen = None

    def show_screen(self):
        self.report_screen = Tk()
        self.report_screen.title("Generate Reports")
        self.report_screen.configure(bg=self.bg_color)

        Button(self.report_screen, text="Inventory Report", command=self.generate_inventory_report, font=self.font, bg=self.button_color, fg=self.text_color).pack()
        Button(self.report_screen, text="Borrowing History Report", command=self.generate_borrowing_report, font=self.font, bg=self.button_color, fg=self.text_color).pack()
        Button(self.report_screen, text="Overdue Tools Report", command=self.generate_overdue_report, font=self.font, bg=self.button_color, fg=self.text_color).pack()

        self.report_screen.mainloop()

    def generate_inventory_report(self):
        report = "Inventory Report\n\n"
        for tool_id, tool_info in self.tools.items():
            report += f"Tool ID: {tool_id}, Name: {tool_info['name']}, Quantity: {tool_info['quantity']}\n"
        messagebox.showinfo("Inventory Report", report)

    def generate_borrowing_report(self):
        report = "Borrowing History Report\n\n"
        for entry in self.borrowed_tools:
            report += (f"Tool ID: {entry['tool_id']}, Employee: {entry['employee']}, "
                       f"Borrowed: {entry['date_borrowed']}, Return: {entry['return_date']}\n")
        messagebox.showinfo("Borrowing History Report", report)

    def generate_overdue_report(self):
        report = "Overdue Tools Report\n\n"
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        for entry in self.borrowed_tools:
            if entry['return_date'] < today:
                report += (f"Tool ID: {entry['tool_id']}, Employee: {entry['employee']}, "
                           f"Borrowed: {entry['date_borrowed']}, Return: {entry['return_date']} (OVERDUE)\n")
        messagebox.showinfo("Overdue Tools Report", report)


if __name__ == "__main__":
    InventoryManagementSystem()