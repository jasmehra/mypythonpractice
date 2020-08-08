
birth_year = input("What year were you born?")
#age = 2019 - birth_year #TypeError: unsupported operand type(s) for -: 'int' and 'str'

age = 2019 - int(birth_year)

print(f"You are {age} years old")
