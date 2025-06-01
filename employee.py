class Employee:
    def __init__(self,emp_id,emp_name,emp_hourly_wage):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_hourly_wage=emp_hourly_wage
    def details(self):
        print("ID :",self.emp_id)
        print("Name :",self.emp_name)
        print("emp_hourly_wage :",self.emp_hourly_wage,"$")
        print("-------------------------")
# Emp1=Employee("EMP1","Nani",300)
# Emp1.details()


# employees are saved into a dict of employee with the emp_id as the key and the information of employee is saved the value
employees={}
def create_employee(emp_id,emp_name,emp_hourly_wage):
    # chech if the employee is already created.
    # make sure it is not created before.
    # if it is created just say the employee is already existing
    if emp_id not in employees:
        new_employee=Employee(emp_id,emp_name,emp_hourly_wage)
        employees[emp_id]=new_employee
        print("Saved",emp_name,"as new employee")
    else:
        print("Employee",emp_id,"is already existing")
def show_employees():
    for emp_id in employees:
        Employee=employees[emp_id]
        Employee.details()
def update_employee(emp_id,new_name,new_hourly_wage=0):
    if emp_id in employees:
        employee=employees[emp_id]
        if new_name and new_hourly_wage:
            employee.emp_name=new_name
            employee.emp_hourly_wage=new_hourly_wage
        else:
            print("invalid arguments")
    else:
        print("Employee with",emp_id,"doesn't exist")
def delete_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
        print("Successfully deleted the employee")
    else:
        print("employee id: ",emp_id,"is not found in the register")
# days 25 per each day 8 hrs.
def emp_salary(emp_id):
    if emp_id in employees:
        Employee=employees[emp_id]
        salary=(25*8)*Employee.emp_hourly_wage
        return salary
    else:
        raise Exception("Employee is not found")

# using the function for managing the employee.
create_employee("Emp1","Jyo",300)
create_employee("Emp2","Tinnu",300)
create_employee("Emp3","Niki",300)

update_employee("Emp2","Tarun",500)

delete_employee("Emp3")

emp_salary("Emp3")
show_employees()