class Person:
    def __init__(self, initialAge):
        # If initial age is negative, set to 0 and print a warning
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge
        
    def amIOld(self):
        # Print age category based on current age
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increase age by 1
        self.age += 1


# Read number of test cases
t = int(input())

# Loop through each test case
for i in range(t):
    # Read person's age
    age = int(input())         
    # Create Person object
    p = Person(age)  
    # Print initial age category
    p.amIOld()
    # Simulate 3 years passing
    for j in range(3):
        p.yearPasses()       
    # Print age category after 3 years
    p.amIOld()
    # Print blank line between test cases
    print("")
