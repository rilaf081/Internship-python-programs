name = input("Name: ")
years = input("Birth year: ")

common =["123", "1234","@123","13579","admin","qwerty"]
chars = "!@#$%^&*(){}[],./?"

for c in common:
    print(name + years + c)
    print(name + chars + years)
    print(name.capitalize() + c)