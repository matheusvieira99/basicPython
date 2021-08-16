name = "Matheus"
age = 21
is_male = True
name = input("Enter your name: ")
age = input("Enter your age: ")
is_male = input("Are you a male? (y/n)")
if (is_male == "y" or is_male == "Y"):
    is_male = True
else:
    is_male = False
print("I'm called " + name + " and I'm a male", is_male)
print("I'm", age, "years old")
print("I really like to be named " + name)
print("But I actually don't like being", age, "years old")
