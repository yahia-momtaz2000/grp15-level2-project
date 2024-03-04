from oop_04.static02.static_methods01.calculator import Calculator

calculator_sony = Calculator('Sony', 'grey', 10, 15)
calculator_casio = Calculator('Casio', 'white', 12, 17)

print('---- test instance methods ------')
print(calculator_sony.calc_area()) # 10 * 15 = 150
print(calculator_casio.calc_area()) # 12 * 17 = 204

print('------- test static methods ---------')
print(calculator_sony.add(5, 9))  # 14
print(calculator_casio.add(5, 9))  # 14
print(Calculator.add(5, 9)) # 14

