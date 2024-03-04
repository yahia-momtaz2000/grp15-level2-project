class Employee:
    # static attributes
    total_bonus = 20000
    total_no_of_employees = 0

    def __init__(self, emp_id, emp_name, emp_gross_salary, emp_job):
        self.__emp_id = emp_id
        self.__emp_name = emp_name
        self.__emp_gross_salary = emp_gross_salary
        self.__emp_job = emp_job
        self.__emp_wallet = 0.0
        Employee.total_no_of_employees = Employee.total_no_of_employees + 1


    def get_emp_name(self):
        return self.__emp_name

    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name

    def get_emp_wallet(self):
        return self.__emp_wallet

    def set_emp_wallet(self, emp_wallet):
        self.__emp_wallet = emp_wallet


    def get_emp_gross_salary(self):
        return self.__emp_gross_salary

    def set_emp_gross_salary(self, emp_gross_salary):
        self.__emp_gross_salary = emp_gross_salary



  # Extra methods

    def receive_bonus(self, bonus_value):
        self.__emp_wallet = self.__emp_wallet + bonus_value
        Employee.total_bonus = Employee.total_bonus - bonus_value

    def calc_monthly_net_salary(self):
        tax = 10
        return self.__emp_gross_salary - self.__emp_gross_salary * tax / 100

    def calc_annual_net_salary(self):
        return self.calc_monthly_net_salary() * 12