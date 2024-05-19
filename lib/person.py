#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="General Management"):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = ''

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
            self._job = ''

# Example 
if __name__ == "__main__":
    # Creating a person with a valid name and job
    person1 = Person(name="Alice", job="Finance")
    print(f"Person1 Name: {person1.name}, Job: {person1.job}")

    # Creating a person with an invalid name (empty string)
    person2 = Person(name="", job="Finance")
    print(f"Person2 Name: {person2.name}, Job: {person2.job}")

    # Creating a person with an invalid name (too long)
    person3 = Person(name="A very very long name that is invalid", job="Finance")
    print(f"Person3 Name: {person3.name}, Job: {person3.job}")

    # Creating a person with an invalid job
    person4 = Person(name="Bob", job="Astronaut")
    print(f"Person4 Name: {person4.name}, Job: {person4.job}")

    # Creating a person with a valid name and default job
    person5 = Person(name="Charlie")
    print(f"Person5 Name: {person5.name}, Job: {person5.job}")

    # Creating a person with default name and job
    person6 = Person()
    print(f"Person6 Name: {person6.name}, Job: {person6.job}")
