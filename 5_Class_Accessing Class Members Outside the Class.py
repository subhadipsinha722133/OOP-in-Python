class my:
    def __init__(self, sal, ag):
        self.salary = sal
        self.age = ag

    def display(self):
        print(f"salary is {self.salary} and age is {self.age}")


e = my(24000, 21)
# e2 = Employee(26000, 26)

print(e.salary)
a = my(52345, 23)
print(a.age)

e.salary = 99999
a.display()
