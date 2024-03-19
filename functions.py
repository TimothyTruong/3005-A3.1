import psycopg2

#username - postgres
#password - admin


#Connect to database
def initDb():
    try:
        conn = psycopg2.connect(
            dbname="Assignment 3",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        return conn

        print("Database connected successfully")
    except:
        print("I am unable to connect to the database")

#Select all students and print them by row
def getStudents():
    conn = initDb()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    

#Adds new student
def addStudent(firstName, lastName, email, enrollmentDate):
    conn = initDb()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{firstName}', '{lastName}', '{email}', '{enrollmentDate}')")
    conn.commit()
    cursor.close()

#Updates student info
def updateStudent(studentId, newEmail):
    conn = initDb()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE students SET email = '{newEmail}' WHERE student_id = {studentId}")
    conn.commit()
    cursor.close()

#Delete student by ID
def deleteStudent(studentId):
    conn = initDb()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM students WHERE student_id = {studentId}")
    conn.commit()
    cursor.close()

initDb()

#Main loop
def main():
    while(True):
        userInput = input("Enter 1 to get all students, 2 to add a student, 3 to update a student, 4 to delete a student, and 5 to exit: ")

        if userInput == "1":
            getStudents()
        elif userInput == "2":
            fName = input("Enter the first name: ")
            lName = input("Enter the last name: ")
            email = input("Enter the email: ")
            enrollmentDate = input("Enter the enrollment date (YYYY-MM-DD): ")

            addStudent(fName, lName, email, enrollmentDate)
            print("Student added successfully")
        elif userInput == "3":
            studentId = input("Enter the student id to update: ")
            newEmail = input("Enter the new email: ")

            updateStudent(studentId, newEmail)
            print("Student updated successfully")

        elif userInput == "4":
            studentId = input("Enter the student id to delete: ")
            deleteStudent(studentId)
            print("Student deleted successfully")

        elif userInput == "5":
            break

main()