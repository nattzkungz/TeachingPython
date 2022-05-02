class Employee:

    def __init__(self, firstname, lastname, salary, jobtitle, age):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = float(salary)
        self.jobtitle = jobtitle
        self.age = int(age)

    def yearlySalary(self):
        return format(self.salary * 26, ".2f")

    def fullName(self):
        return str(self.firstname + " " + self.lastname)

    def getAge(self):
        return self.age

    def getJob(self):
        return self.jobtitle

    def biWeekly(self):
        return self.salary

    def last(self):
        return self.lastname


def main():
    filename = input("Enter Employee Filename: ")
    file = [line.strip("\n").split(",") for line in open(filename, "r").readlines()]
    store = []
    for person in file:
        worker = Employee(person[0],person[1],person[2],person[3],person[4])
        store.append(worker)

    def order(factor):
        orderingDict = {}
        for person in store:
            if factor == "Salary":
                orderingDict[person.fullName()] = [person.yearlySalary(), person.biWeekly()]
            elif factor == "Age":
                orderingDict[person.fullName()] = [person.getAge(), person.getJob()]
             
        orderedKey = sorted(orderingDict, key=orderingDict.get, reverse=True)
        
        store1 = []
        for person in orderedKey:
            store1.append([person, orderingDict[person]])

        return store1

    richest = order("Salary")
    oldest = order("Age")
    
    print(f"The oldest employee is: {oldest[0][0]}")
    print(f"Their job title is: {oldest[0][1][1]}")
    print(f"AGE: {oldest[0][1][0]}")
    print(f"The richest employee is: {richest[0][0]}")
    print(f"Their bi-weekly salary is: ${richest[0][1][1]}")
    print(f"Yearly salary: ${richest[0][1][0]}")

main()