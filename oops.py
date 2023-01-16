# python file to explain OOPs constructs in Python

# Classes

class Human(object):
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def display_details(self):
        print("Name: {}".format(self.name))
        print("gender: {}".format(self.gender))
        print("address: {}".format(self.address))


# inheritance

class Employee(Human):
    _Employee_count = 0
    def __init__(self, name, gender, address, designation, salary):
        super().__init__(name, gender, address)
        self.designation = designation
        self._salary = salary
        Employee._Employee_count += 1

    #polymorphism
    def display_details(self):
        super().display_details()
        print("designation: {}".format(self.designation))
        print("salary: {}".format(self._salary))

    @staticmethod
    def employees_count():
        print("total employees: {}".format(Employee._Employee_count))

    # getter
    @property
    def salary(self):
        return self._salary

    # setter 
    @salary.setter
    def salary(self, new_salary):
        if new_salary > self._salary:
            self._salary = new_salary
        else:
            print("new salary is less than older salary, can not be set.")

    
if __name__ == "__main__":
    # instantiation
    human1 = Human("Shubham Pandey", "Male", "Allahabad")
    human1.display_details()
    human2 = Human("Xyz Def", "Female", "London")
    human2.display_details()

    # inherited class instantiation
    emp1 = Employee("Ankit Sahu", "Male", "Ald", "SE", 1)
    emp1.display_details()
    emp1.employees_count()
    emp2 = Employee("Rakesh Dixit", "Male", "Ghaziabad", "Manager", 10000000000)
    emp2.display_details()
    emp2.employees_count()
    print("salary of emp2: ", emp2.salary)
    emp2.salary = 10000
    print("salary of emp2: ", emp2.salary)
    emp2.salary = 3338382882828282828
    print("salary of emp2: ", emp2.salary)
    