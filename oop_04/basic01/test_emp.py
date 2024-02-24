from oop_04.basic01.emp import Emp

# main program
print('-------- Take object emp_marwa from class Emp in module emp -------------')
emp_marwa = Emp(101, 'Marwa Aly', 7000, 'Java Developer')
# emp_marwa.emp_gross_salary = -8000 # Direct access the attribute
emp_marwa.set_emp_gross_salary(8000)
print('Marwa full name = ', emp_marwa.get_emp_name())
print('Marwa Monthly net salary = ', emp_marwa.calc_monthly_net_salary())
print('Marwa annual net salary = ', emp_marwa.calc_annual_net_salary())

print('--------- Take object emp_hesham from class Emp in module emp ---------------')
emp_hesham = Emp(102, 'Hesham Mostafa', 12000, 'Data Scientist')
print('Hesham monthly net salary = ', emp_hesham.calc_monthly_net_salary())
print('Hesham annual net salary = ', emp_hesham.calc_annual_net_salary())

emp_ahmed = Emp(103, 'Ahmed Omran', 5000, 'Mobile developer')
emp_hend = Emp(104, 'Hend Hany', 6000, 'Sw Tester')

print('------------------- List of Objects ( Employees ) ---------------------')
emps_list = [emp_marwa, emp_hesham, emp_ahmed, emp_hend]
emps_list.append( Emp(105, 'Amir Ahmed', 3000, 'Office boy')  )

sum_gross = 0
for employee in emps_list:
    new_gross_salary = employee.get_emp_gross_salary() * 1.1
    employee.emp_gross_salary = new_gross_salary
    print('employee name = ', employee.get_emp_name(),' employee gross salary = ', round(employee.get_emp_gross_salary(), 2) )
    sum_gross = sum_gross + employee.get_emp_gross_salary()

print('Sum of all salaries = ', sum_gross)

