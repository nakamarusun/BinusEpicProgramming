class Person:

    __name: str
    __address: str

    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address

    def getName(self) -> str:
        return self.__name

    def getAddress(self) -> str:
        return self.__address

    def setAddress(self, address: str):
        self.__address = address
    
    def toString(self) -> str:
        return self.__name + "(" + self.__address + ")"

class Student(Person):

    __numCourses: int = 0
    __courses: [str] = []
    __grades: [int] = []

    def __init__(self, name: str, address: str):
        super().__init__(name, address)

    def addCourseGrade(self, course: str, grade: int):
        self.__courses.append(course)
        self.__grades.append(grade)

    def printGrades(self):
        for i in range(len(self.__courses)):
            print("Your score in", self.__courses[i], "is", self.__grades[i])

    def getAverageGrade(self) -> float:
        return sum(self.__grades) / len(self.__grades)

    def toString(self) -> str:
        return "Student: " + super().toString()

class Teacher(Person):

    __numCourses: int = 0
    __courses: [str] = []

    def __init__(self, name: str, address: str):
        super().__init__(name, address)

    def addCourse(self, course: str) -> bool:
        if (course in self.__courses) == False:
            self.__courses.append(course)
            self.__numCourses += 1
            return True
        return False

    def removeCourse(self, course: str) -> bool:
        if (course in self.__courses):
            self.__courses.remove(course)
            self.__numCourses -= 1
            return True
        return False

    def toString(self) -> str:
        return "Teacher: " + super().toString()


newStudent = Student("Gardyan", "Jalan oke")

print(newStudent.toString())

newStudent.addCourseGrade("Math", 87)
newStudent.addCourseGrade("Biology", 97)

newStudent.printGrades()

print(newStudent.getAverageGrade())

newTeacher = Teacher("Sir Bagus", "Jalan Bisun")

print(newTeacher.toString())

print(newTeacher.addCourse("Math"))
print(newTeacher.addCourse("Programming"))
print(newTeacher.addCourse("Programming"))

print(newTeacher.removeCourse("Math"))
print(newTeacher.removeCourse("Math"))