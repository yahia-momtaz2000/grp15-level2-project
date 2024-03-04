import sys


class Emp:
    # Constructor : initialize object attributes with initial values
    # Object attributes [ instance attributes ] : emp_id, emp_name, emp_gross_salary, emp_job
    def __init__(self, new_emp_id, new_emp_name, new_emp_gross_salary, new_emp_job):
        self.__emp_id = new_emp_id
        self.__emp_name = new_emp_name
        if new_emp_gross_salary > 0:
            self.__emp_gross_salary = new_emp_gross_salary
        else:
            print('Salary cannot be -ve')
            sys.exit()
        self.__emp_job = new_emp_job

    # Make attributes private to the class [ Deny direct access to the attributes from outside the class ]
    # 2 Methods for each attribute : Read | Edit        =    get    |   set     [ Accessors ]
    def get_emp_name(self):
        return self.__emp_name

    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name

    def get_emp_gross_salary(self):
        return self.__emp_gross_salary

    def set_emp_gross_salary(self, emp_gross_salary):
        if emp_gross_salary > 0:
            self.__emp_gross_salary = emp_gross_salary
        else:
            print('Salary cannot be -ve')
            sys.exit()


    # Extra methods
    def calc_monthly_net_salary(self):
        tax = 10
        return self.__emp_gross_salary - self.__emp_gross_salary * tax / 100

    def calc_annual_net_salary(self):
        return self.calc_monthly_net_salary() * 12