# main program
from oop_04.static02.static_attriubtes02.employee import Employee

emp_marwa = Employee(101, 'Marwa Aly', 7000, 'Java Developer')
emp_hesham = Employee(102, 'Hesham Mostafa', 12000, 'Data Scientist')

print('Marwa wallet = ', emp_marwa.get_emp_wallet())
print('Hesham wallet = ', emp_hesham.get_emp_wallet())
print('Total bonus = ', Employee.total_bonus)

emp_marwa.receive_bonus(3000)
emp_hesham.receive_bonus(1500)
emp_marwa.receive_bonus(2500)

print('Marwa wallet = ', emp_marwa.get_emp_wallet())        # 5500
print('Hesham wallet = ', emp_hesham.get_emp_wallet())      # 1500
print('Total bonus = ', Employee.total_bonus)               # 13000

print('Total no. of employees objects = ', Employee.total_no_of_employees)