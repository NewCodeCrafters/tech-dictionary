import time

name = input("What is your name:? ").title()
repeat = int(input(f"{name}, how many times can i say your name?: "))
for i in range(repeat):
    print(f"Your name is {name}.")
    time.sleep(1)
print(f"I just called your name {repeat} times.") 