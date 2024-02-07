# Employee class
class Employee:
    # Class variable
    emp_counter = 0

    # Initialize class with default values
    def __init__(self, name, salary):
        self.employee_id = Employee.generate_employee_id()
        self.employee_name = name
        self.employee_salary = salary

    # Generate unique employee ID
    @classmethod
    def generate_employee_id(cls):
        Employee.emp_counter += 1
        return Employee.emp_counter

    # Getter for employee_id
    def get_employee_id(self):
        return self.employee_id

    # Getter for employee_name
    def get_employee_name(self):
        return self.employee_name

    # Getter for employee_salary, returns formatted string
    def get_employee_salary(self):
        return "${:,.2f}".format(self.employee_salary)


# Main function
def main():
    # Create an employee
    employee = Employee("Caelius Dathan", 4900.0)

    # Print the employee details
    print(f"Employee ID: {employee.get_employee_id()}")
    print(f"Name: {employee.get_employee_name()}")
    print(f"Salary: {employee.get_employee_salary()}")


if __name__ == "__main__":
    main()