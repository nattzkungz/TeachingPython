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

file = [i.strip("\n").split(",") for i in open(input("Enter Employee Filename: ")).readlines()]

store = []
for person in file:
    store.append(Employee(person[0],person[1],person[2],person[3],person[4]))

workerDict = {}
for i in store:
    workerDict[i.fullName()] = [i.biWeekly(), i.getJob(), i.getAge(), i.yearlySalary()]

def order(factor):
        orderingDict = {}
        for person in store:
            if factor == "Salary":
                orderingDict[person.fullName()] = person.yearlySalary()
            elif factor == "Age":
                orderingDict[person.fullName()] = person.getAge()
            else:
                orderingDict[person.fullName()] = person.last()

        orderedKey = sorted(orderingDict, key=orderingDict.get)
        return orderedKey

syr, sage, slast = order("Salary"), order("Age"), order("Last")

def putinData(data):
    output = {}
    for i in data:
        output[i] = []
        for j in workerDict[i]:
            output[i].append(j)
    return output

fyr, fage, flast = putinData(syr), putinData(sage), putinData(slast)


def fileOutput(data, t):
    if t == 1:
        file = open("salary.txt", "w")
    elif t== 2:
        file = open("empage.txt", "w")
    elif t == 3:
        file = open("empname.txt", "w")

    for i in data:
        file.write("{0:20}{1:5}   {2:10}{3:5}{4}\n".format(i,data[i][0],data[i][1],data[i][2],data[i][3]))

fileOutput(fyr,1)
fileOutput(fage,2)
fileOutput(flast,3)