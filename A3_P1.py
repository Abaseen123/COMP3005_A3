import psycopg2

#connects to the specific database I have which is named Assignment3 with that password in postgres
conn = psycopg2.connect(host="localhost", database="Assignment3", user="postgres",
                        password="Abaseen1", port=5432)


#connection
cur = conn.cursor()


def getAllStudents():
    cur.execute("SELECT * FROM students;") #executes this in the database
    print (cur.fetchall()) #prints the entire table

def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute('''INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)''', 
                (first_name, last_name, email, enrollment_date)) #adds student based on parameters

def updateStudentEmail(student_id, new_email):
    cur.execute('''UPDATE students SET email = %s WHERE student_id = %s''', (new_email, student_id) ) #updates student based on id with an email they decide

def deleteStudent(student_id):
    cur.execute('''DELETE FROM students WHERE student_id=%s''', (student_id,)) #deletes student from table based on id

#for TESTING PURPOSES
#getAllStudents()
#addStudent("Meghan", "Fox", "meghanF@email.com", "2024-03-03")
#addStudent("Timothee", "Chamalet", "Dune2@email.com", "2024-12-12")
#getAllStudents()
#updateStudentEmail(2, "janeTheDaneSmith@email.com")
#getAllStudents()
#deleteStudent(8)
#getAllStudents()









conn.commit()
conn.close()