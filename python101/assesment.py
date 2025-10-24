attempts = 0
remaining_attempts = 3

while True:
    name = input("Enter your name: ")
    pass1 = input("Enter password: ")
    pass2 = input("Confirm password: ")

    if pass1 == pass2:
        print("Password created sucessfully!")
        break
    else:
        attempts +=1
        remaining_attempts -=1
        print(f"Passwords do not match! Try again, {remaining_attempts} attempts left")
        
    if attempts == 3:
        print(f"Too many attempts! Try again later.")
        break
if pass1 == pass2:
    print(f"Welcome! {name}")
else:
    print(f"Oops! {name}, Your password was not created successfully!")