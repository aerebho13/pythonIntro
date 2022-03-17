# Im a comment, not code


# variables & strings
name = "Aaron"
last = "Erebholo"
age = 101
found = False
price = 19.2333


print(name + " " + last)

print(age + 1)
print(age * 1)
print("Hi Im " + name + ", and my age is " + str(age))

print(f"Hi Im {name}, and my age is: {age}")


if age < 100:
    print("Dont worry, you are still young")
    print("Im, inside the if")
    print("me too")

elif age == 100:
    print("Congrats you mad it to a century!!!")

else:
    print("Sorry, you are getting old!!")

print("Im not in the IF")


# functions
def say_hello():
    print("hello from a function")
    print("Im inside a function")

say_hello()