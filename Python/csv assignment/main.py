from os import system, name
from statistics import mean

class Employee:

    # Init variables

    __id: str
    __name: str
    __pos: str
    __salary: int

    employees = []

    def __init__(self, id: str, name: str, pos: str, salary: int):
        self.__id = id
        self.__name = name
        self.__pos = pos
        self.__salary = salary

    # Getter

    def getId(self) -> str: return self.__id
    def getName(self) -> str: return self.__name
    def getPos(self) -> str: return self.__pos
    def getSalary(self) -> int: return self.__salary

    # Setter

    def setId(self, id: str): self.__id = id
    def setName(self, name: str): self.__name = name
    def setPos(self, pos: str): self.__pos = pos
    def setSalary(self, salary: int): self.__salary = salary

    # Funcs
    
    def __str__(self):
        return "ID: {}, Name: {}, Position: {}, Salary: {}".format(self.getId(), self.getName(), self.getPos(), self.getSalary())

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def fillRightWith(amount: int, string: str, filler: str) -> str:
    return ( string + filler * (amount - len(string)) ) if amount > len(string) else string

def showEmployees():
    print("|ID    |Name                 |Position       |Salary               |")
    for i in Employee.employees:
        dispId = fillRightWith(6, i.getId(), " ")
        dispName = fillRightWith(21, i.getName(), " ")
        dispPos = fillRightWith(15, i.getPos(), " ")
        dispSalary = fillRightWith(21, str(i.getSalary()), " ")
        print( "|{id}|{name}|{pos}|{salary}|".format(id=dispId, name=dispName, pos=dispPos, salary=dispSalary) )

def prompt() -> str:
    print("1. New Staff")
    print("2. Delete Staff")
    print("3. View Summary Data")
    print("4. Save & Exit")
    print()
    return input("Input choice(numeric): ")

with open("data.txt", "r", encoding="utf-8") as file:
    rawData = file.readlines()
    for i in range(len(rawData)):
        rawData[i] = rawData[i].replace("\n", "").split("#")
        person = rawData[i]
        Employee.employees.append( Employee(person[0], person[1], person[2], int(person[3])) )

while True:
    clear()
    showEmployees()
    print()
    answer = prompt()
    if answer == "1":
        print()
        print("New Staff:")
        while True:
            newId = input("Input ID[SXXXX]: ")
            if newId[0] != "S":
                continue
            for i in Employee.employees:
                if i.getId() == newId:
                    continue
            try:
                int(newId[1:])
            except:
                continue

            newName = input("Input Name[0..20]: ")
            if not (len(newName) > 0 and len(newName) < 21):
                continue
            
            allPos = ["Staff", "Officer", "Manager"]
            newPos = input("Input Position[Staff|Officer|Manager]: ").capitalize()
            if newPos not in allPos:
                continue

            newSalary = int(input("Input salary for " + newPos + ": "))
            if newPos == "Staff":
                if newSalary < 3500000 or newSalary > 7000000:
                    continue
            elif newPos == "Officer":
                if newSalary < 7000001 or newSalary > 10000000:
                    continue
            else:
                if newSalary < 10000001:
                    continue
            
            Employee.employees.append( Employee(newId, newName, newPos, newSalary) )
            print("Add employee success !")
            input("Press [ENTER] to continue..")
            break
    elif answer == "2":
        print()
        delete = input("Input ID: ")
        found = False
        for i in range(len(Employee.employees)):
            if Employee.employees[i].getId() == delete:
                Employee.employees.pop(i)
                print("Delete successful !")
                input("Press [ENTER] to continue..")
                found = True
                break
        if not found:
            print("Invalid input !")
            input("Press [ENTER] to continue..")
    elif answer == "3":
        salaries = {
            "Staff": [],
            "Officer": [],
            "Manager": []
        } # salaries: {staff: [int]}

        for i in Employee.employees:
            if i.getPos() == "Staff":
                salaries["Staff"].append(i.getSalary())
            elif i.getPos() == "Officer":
                salaries["Officer"].append(i.getSalary())
            else:
                salaries["Manager"].append(i.getSalary())
        clear()
        inc = 1
        for posi in salaries:
            print("{}. {}".format(inc, posi))
            print("Minimum Salary: " + str(min(salaries[posi])))
            print("Maximum Salary: " + str(max(salaries[posi])))
            print("Average Salary: " + str(mean(salaries[posi])))
            print()
            inc += 1
        
        input("Press [ENTER] to continue..")     
    elif answer == "4":
        with open("data.txt", "w", encoding="utf-8") as file:    
            for i in Employee.employees:
                file.write("{}#{}#{}#{}\n".format(i.getId(), i.getName(), i.getPos(), str(i.getSalary())))
        print("Save successful !")
        input("Press [ENTER] to continue..")
        exit()
    else:
        print("Invalid input.")
        input("Press [ENTER] to continue..")
