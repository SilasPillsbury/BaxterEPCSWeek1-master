from random import randint
def main():
  students = [
    Student("Larsson","Halsted", 37),
    Student("BonJovi","Jon", 55),
    Student("Billy","McBillyBob",22),
  ]
  printHeader()
  selection = getUserSelection()
  list_of_functions = [
    printStudentsByAge,
    printStudentsByLName,
    printStudentsByFName,
    printAvgAge,
    ageRange
    ]
  if selection >= len(list_of_functions):
    print("SELECTION NOT RECOGNIZED")
  else:
    list_of_functions[selection](students)

class Student:
  
  def __init__(self, lastName, firstName, age):
    self.lastName = lastName
    self.age = age
    self.firstName = firstName
    
  def assignRandomFirstName():
      pass

  def assignRandomLastName():
    pass
  
  def assignRandomAge():
    self.age = random.randint(0,100)

  def assignRandomWeight(self, isMetric):
    pass

  def assignRandomHeight(self, isMetric):
    pass

inputQuestions = [
  "For STUDENTS BY AGE, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 2",
  "For AVERAGE of STUDENT AGES type 3",
  "For RANGE of STUDENT AGES type 4",
]

def getUserSelection():
  for inputQuestion in inputQuestions:
    print(inputQuestion)
  return int(input("Type selection and press enter:"))

def printHeader():
    print("Generic Academy Student Registry")

def printStudentsByAge(students):
  print ("----Students By Age-----")
  sortStudents = sorted(students, key=lambda student: student.age)
  for student in sortStudents:
    print(student.lastName + ", " + student.firstName + ", " + str(student.age))

def printStudentsByLName(students):
  print ("----Students By Last Name-----")
  sortStudents = sorted(students, key=lambda student: student.lastName)
  for student in sortStudents:
    print(student.lastName + ", " + student.firstName + ", " + str(student.age))

def printStudentsByFName(students):
  print ("----Students By First Name-----")
  sortStudents = sorted(students, key=lambda student: student.firstName)
  for student in sortStudents:
    print(student.firstName + ", " + student.lastName + ", " + str(student.age))
def printSumAge(students):
  print ("Answer:")

def printAvgAge(students):
  k = 0
  for student in students:
    k += student.age
  k = k/len(students)
  print ("Answer: " + str(k))

def ageRange(students):
  ages = []
  for student in students:
    ages.append(student.age)
  studentA , studentB = min(ages) , max(ages)
  print (abs(studentA - studentB))

main()
