from oop_04.inherit_03.employee import Employee
from oop_04.inherit_03.manager import Manager

# main program
print('----- Create object from Employee ------')
emp_ahmed = Employee(101, 'Ahmed Marey', 7000, 'Designer', 10, 20.0)
print('Emp ahmed monthly net salary = ', emp_ahmed.calc_monthly_net_salary())
print('Emp ahmed annual net salary = ', emp_ahmed.calc_annual_net_salary())

print('------- Create object from Manager --------')
mgr_khalid = Manager(401, 'Khaled Ezat', 15000, 'Pr. Manager', 10)
print('Mgr Khalid monthly net salary = ', mgr_khalid.calc_monthly_net_salary())
company_profit = 1_000_000
print('Mgr Khalid annual net salary = ', mgr_khalid.calc_annual_net_salary(company_profit)) # 162000 + 100000 = 262000

print('---------------- Check for overrding ---------------------')
emp_ahmed.print_person_details()
