# Open STUDENT-FILE
student_file = open("student_records.txt", "w")

while True:
    
    # Accept STUDENT-ID
    student_id = input("Enter STUDENT-ID (or 0 to exit): ")

    if student_id == "0":

        student_file.close()
        print("File closed.")
        
        break

    # Accept STUDENT-NAME, COURSE-NAME, COURSE-FEE, FEES-PAID
    student_name = input("Enter STUDENT-NAME: ")
    course_name = input("Enter COURSE-NAME: ")
    course_fee = input("Enter COURSE-FEE: ")
    fees_paid = input("Enter FEES-PAID: ")

    student_record = f"{student_id}, {student_name}, {course_name}, {course_fee}, {fees_paid}\n"
    student_file.write(student_record)

