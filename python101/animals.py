import time
zoo = ['dog','cat','goat','rat','cobra','lizard','kangaroo','vulture']
print(f"There are {len(zoo)} animals in the zoo.")

for animal in zoo:
    time.sleep(1)
    if animal in ['rat','lizard','vulture']:
        print(f"I don't like {animal}")
        zoo.remove(animal)
        time.sleep(1)
        print(f"Removing {animal}..")
        time.sleep(1)
    else:
        print(f"I like {animal}")

print(f"There are now {len(zoo)} animals in the zoo..")