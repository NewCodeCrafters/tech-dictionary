name = input("What is your name: ")
age = int(input("Enter your age: "))
if age >= 60 :
    print(f"Welcome😊 {name}, you are a senior")

elif age >= 18 :
    print(f"Welcome😊 {name}, you are a adult")

elif age >= 12 :
    print(f"Welcome😊 {name}, you are an teen")

elif age >= 3 :
    print(f"Welcome😊 {name}, you are a child")

else:
    print(f"Welcome😊 {name}, you are a toddler")