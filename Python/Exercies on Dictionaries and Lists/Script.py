#1
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
} 

inventory['pocket'] = ['seashells', 'strange berry', 'lint']

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')

inventory['gold'] += 50

#2
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3 
}
stock = {
    "banana": 3,
    "apple": 0,
    "orange": 4,
    "pear": 5
}

for i in prices:
    print(i)
    print("price:", prices[i])
    print("stonks:", stock[i])

total = 0
for i in prices:
    total += prices[i] * stock[i]
print(total)

#3
groceries = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
} 
 
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def computeBill(food: [str]):
    total = 0
    for i in food:
        if stock[i] > 0:
            stock[i] -= 1
            total += prices[i]
    return total


print(computeBill(groceries))

#4
eren = {
    "name": "Eren",
    "homework": [90.0,97.0,75.0,92.0],
    "quizzes": [70.0,40.0,94.0],
    "tests": [20.0,60.0]
}
    
mikasa = {
    "name": "Mikasa",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
} 
 
armin = {
    "name": "Armin",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [eren, mikasa, armin]

for i in students:
    for j in i:
        print("   ", j, ": ", i[j])
    print("")

def average(numbers: [float]):
    return float(sum(numbers) / len(numbers))

def getAverage(student: dict):
    hw = average(student["homework"]) * 0.1
    qz = average(student["quizzes"]) * 0.3
    ts = average(student["tests"]) * 0.6

    return hw + qz + ts

def getLetterGrade(score: float):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

print(getLetterGrade(getAverage(eren)))

def getClassAverage(student: list):
    results = []
    for i in student:
        results.append(getAverage(i))
    return average(results)

classAverage = getClassAverage(students)

print( classAverage )

print( getLetterGrade(classAverage) )