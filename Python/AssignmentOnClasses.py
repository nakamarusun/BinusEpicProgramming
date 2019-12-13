class Employee():

    __id: int
    __firstName: str
    __lastName: str
    __salary: int

    def __init__(self, id: int, firstName: str, lastName: str, salary: int):
        self.__id = id
        self.__firstName = firstName
        self.__lastName = lastName
        self.__salary = salary

        #Getter

    def getID(self) -> int: return self.__id
    def getFirstName(self) -> str: return self.__firstName
    def getLastName(self) -> str: return self.__lastName
    def getSalary(self) -> str: return self.__salary
    def getName(self) -> str: return self.getFirstName() + " " + self.getLastName()

        #Setter

    def setSalary(self, num: int):  self.__salary = num

        #Func

    def getAnnualSalary(self) -> int:
        return self.__salary * 12

    def raiseSalary(self, percentage: int) -> int:
        __salary *= round(((100 + int)/100))
        return __salary

    def __str__(self):
        return "Employee[id = {0}, name = {1} {2}, salary = {3}]".format(self.__salary, self.__firstName, self.__lastName, self.__salary)

class InvoiceItem():

    __id: str
    __desc: str
    __qty: int
    __unitPrice: float

    def __init__(self, id: str, desc: str, qty: int, unitPrice: float):
        self.__id = id
        self.__desc = desc
        self.__qty = qty
        self.__unitPrice = unitPrice

        #Getter
    
    def getID(self) -> str: return self.__id
    def getDesc(self) -> str: return self.__desc
    def getQty(self) -> int: return self.__qty
    def getUnitPrice(self) -> float: return self.__unitPrice

        #Setter

    def setQty(self, qty: int): self.__qty = qty
    def setUnitPrice(self, price): self.__unitPrice = price
    
        #Func

    def getTotal(self) -> float:
        return self.__unitPrice * self.__qty

    def __str__(self):
        return "Invoice Item[id = {0}, desc = {1}, qty = {2}, unitPrice = {3}]".format(self.__id, self.__desc, self.__qty, self.__unitPrice)

class Account():

    __id: str
    __name: str
    __balance: int

    def __init__(self, id: str, name: str, balance: int = 0):
        self.__id = id
        self.__name = name
        self.__balance = balance

    #Getter

    def getID(self) -> str: return self.__id
    def getName(self) -> str: return self.__name
    def getBalance(self) -> int: return self.__balance

    #Setter

    pass

    #Func

    def credit(self, amount: int) -> int:
        self.__balance += amount
        return self.__balance

    def debit(self, amount: int) -> int:
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Amount exceeded balance !")
        return self.__balance

    def transferTo(self, another, amount: int) -> int:
        if amount <= self.__balance:
            self.__balance -= amount
            another.credit(amount)
        else:
            print("Amount exceeded balance !")
        return self.__balance

    def __str__(self):
        return "Account[id = {0}, name = {1}, balance = {2}]".format(self.__id, self.__name, self.__balance)

class Date():

    __day: int
    __month: int
    __year: int

    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

        #Getter

    def getDay(self) -> int: return self.__day
    def getMonth(self) -> int: return self.__month
    def getYear(self) -> int: return self.__year

        #Setter

    def setDay(self, day: int): self.__day = day
    def setMonth(self, month: int): self.__month = month
    def setYear(self, year: int): self.__year = year
    def setDate(self, day: int, month: int, year: int): 
        self.__day = day
        self.__month = month
        self.__year = year

      #Func
    
    def __str__(self):
        return str(self.__day).zfill(2) + "/" + str(self.__month).zfill(2) + "/" + self.__year

class Time():

    __hour: int
    __minute: int
    __second: int

    def __init__(self, hour: int, minute: int, second: int):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

        #Getter

    def gethour(self) -> int: return self.__hour
    def getminute(self) -> int: return self.__minute
    def getsecond(self) -> int: return self.__second

        #Setter

    def sethour(self, hour: int): self.__hour = hour
    def setminute(self, minute: int): self.__minute = minute
    def setsecond(self, second: int): self.__second = second
    def setTime(self, hour: int, minute: int, second: int): 
        self.__hour = hour
        self.__minute = minute
        self.__second = second

        #Func

    def __str__(self):
        return str(self.__hour).zfill(2) + ":" + str(self.__minute).zfill(2) + ":" + str(self.__second).zfill(2)

    def nextSecond(self):
        self.__second += 1
        if self.__second > 59:
            self.__second -= 59
            self.__minute += 1
        if self.__minute > 59:
            self.__minute -= 59
            self.__hour += 1
        if self.__hour > 23:
            self.__hour -= 23
        
        return self

    def previousSecond(self):
        self.__second -= 1
        if self.__second < 0:
            self.__second += 59
            self.__minute -= 1
        if self.__minute < 0:
            self.__minute += 59
            self.__hour -= 1
        if self.__hour > 0:
            self.__hour += 23
        
        return self

ajoi = Account("asdas", "dasdsa", 32)
ahoi = Account("jojoi", "popoi", 5)
ohoi = Time(6,32,33)
a = 5
print(ajoi.transferTo(ahoi, 15))
print(ahoi.getBalance())

print(ohoi.__str__())