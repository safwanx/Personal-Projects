previousGPA = float(input("Enter current GPA: "))
previousCredits = int(input("Enter previously earned credits: "))
creditPoints5 = float(previousGPA * previousCredits)

grade = ['A+','A' ,'B+','B','C+','C','D+','D', 'F']
gradePoints5 = [5, 4.75, 4.5, 4, 3.5, 3, 2.5, 2, 0]
classesNumbers = int(input("Enter no. of classes being taken: "))
classes = []
grades = []
credits = []
#input the classes, grades, and credits
for i in range(classesNumbers):
    classes.append(input("Enter class name: "))
    grades.append(input("Enter grade: ").capitalize())
    credits.append(int(input("Enter credits: ")))


#calculating credit points for gpa 
creditPoints = 0
for i in range(len(grades)):
    creditPoints += gradePoints5[grade.index(grades[i])] * credits[i]


#calculate the credit points for cgpa
for i in range(len(grades)):
    creditPoints5 += gradePoints5[grade.index(grades[i])] * credits[i]


#calculate the gpa and cgpa for 5.0 scale
gpa = round(creditPoints / sum(credits), 3)
cgpa = round(creditPoints5 / (previousCredits + sum(credits)), 3)


#printing all info in table format and remove extra spaces to adjust the table
print("\n")
print("Class".ljust(20) + "Grade".ljust(20) + "Credits".ljust(20))
for i in range(len(grades)):
    print("\n" + classes[i].ljust(20) + grades[i].ljust(20) + str(credits[i]).ljust(20))

print("\nGPA: " + str(gpa) + "\n" + "CGPA: " + str(cgpa) + "\n")
