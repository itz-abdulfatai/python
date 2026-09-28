students = [
    {
        "name": "brad pitt",
        "id": "stu1",
        "age": 62,
        "math_score": 75.0,
        "english_score": 87.0,
        "science_score": 54.0
    },
    {
        "name": "Donald Trump",
        "id": "presido1",
        "age": 88,
        "math_score": 76.0,
        "english_score": 33.0,
        "science_score": 84.0
    },
    {
        "name": "kavin hart",
        "id": "tall",
        "age": 2,
        "math_score": 43.0,
        "english_score": 75.0,
        "science_score": 11.0
    },
    {
        "name": "Rick Ross",
        "id": "best",
        "age": 66,
        "math_score": 100.0,
        "english_score": 100.0,
        "science_score": 100.0
    }
]

def average(math, english, science):
    ave = (math+english+science)/3
    return round(ave, 2)


def grade(math, english, science):
    ave = average(math, english, science)
    if ave >= 90: return "A+"
    elif ave >= 80: return "A"
    elif ave >= 70: return "B"
    elif ave >= 60: return "C" 
    elif ave >= 50: return "D" 
    else: return "F" 

def class_average(scores):
    
    total = 0
    for score in scores:
        total+=score
    try:
        return total/len(scores)
    except:
        return total


def get_class_average():
    total = 0
    count=0

    for student in students:
        total+=student['math_score']
        total+=student['english_score']
        total+=student['science_score']
        count+=3

    try:
            return total/count
    except:
            return total

def get_highest_score():
    highest = 0

    for student in students:
        ave = average(student["math_score"], student['english_score'], student['science_score'])
        if (ave > highest): highest = ave
    return highest

def get_lowest_score():
    if len(students) == 0: return 0
    lowest = (students[0]["math_score"] + students[0]['english_score'] + students[0]['science_score'])/3
    
    for student in students:
        ave = average(student["math_score"], student['english_score'], student['science_score'])
        if (ave < lowest): lowest = ave
    return lowest

def get_passed():
    count = 0
    for student in students:
        if average(student["math_score"], student['english_score'], student['science_score']) >= 50: count+=1
    return count

def get_failed():
    count = 0
    for student in students:
        if average(student["math_score"], student['english_score'], student['science_score']) < 50: count+=1
    return count

def find_top_student():
    highest_ave = 0
    top_student = {}
    for student in students:
        student_ave = average(student["math_score"], student['english_score'], student['science_score'])
        if student_ave > highest_ave: 
            top_student = student
            highest_ave = student_ave
    return top_student    

# def get_ranking(): 
    



def prompt():
    while True: 
        print("""
===== STUDENT GRADE MANAGER =====

1. Add student
2. View all students
3. Search for a student
4. View class statistics
5. Find top student
6. Remove a student
7. Exit
    """)

    
        choice = input("> ")
        try:
            choice = int(choice)
        except: 
            print("invalid input")
            continue 
            
        


        if (choice == 1):
            print("input student information")
            name = input("Name: ")
            if name == '': 
                print("invalid name")
                continue
            age = input("Age: ")

            try: 
                age = int(age)
            except:
                print("invalid age")
                continue
            id = input("Student id: ")
            math_score = input("Math score: ")
            english_score = input("English score: ")
            science_score = input("Science score: ")

            try:
                math_score = float(math_score)
                english_score = float(english_score)
                science_score = float(science_score)
            except:
                print("invalid score input")
                continue

            if math_score > 100: 
                print("score cannot be greater than 100")
                continue
            if english_score > 100: 
                print("score cannot be greater than 100")
                continue
            if science_score > 100: 
                print("score cannot be greater than 100")
                continue
            if math_score < 0: 
                print("score cannot be less than 0")
                continue
            if english_score < 0: 
                print("score cannot be less than 0")
                continue
            if science_score < 0: 
                print("score cannot be less than 0")
                continue
            


            for student in students:
                if ( id == student['id']):
                    print(f"student with id {id} already exists")
                    break
            else:
                students.append({
                    "name": name,
                    "age": age,
                    "id": id,
                    "math_score": math_score,
                    "english_score": english_score,
                    "science_score": science_score
                })
                print("student added successfully")

        elif (choice == 2):
            if len(students) == 0: print("No Students found")
            for student in students:
                # name, age, id, math_score, english_score, science_score =student
                # why does deconstruction not work

                print(f"""
ID: {student['id']}
Name: {student['name']}
Age: {student['age']}
Math: {student['math_score']}
English: {student['english_score']}
Science: {student['science_score']}
Average: {average(student['math_score'], student['english_score'], student['science_score'])}
Grade: {grade(student['math_score'], student['english_score'], student['science_score'])}
-------------------------
""")
        elif choice == 3:
            search = input("Input students name or ID: ").lower()

            for student in students:
                if (student['name'].lower() == search or student['id'].lower() == search):
                    print(f"""
ID: {student['id']}
Name: {student['name']}
Age: {student['age']}
Math: {student['math_score']}
English: {student['english_score']}
Science: {student['science_score']}
Average: {average(student['math_score'], student['english_score'], student['science_score'])}
Grade: {grade(student['math_score'], student['english_score'], student['science_score'])}
-------------------------
                    """)
                    break
            else:
                print("student not found")


        elif choice == 4: 
            if len(students) == 0:
                print("not enough information")
                continue
            print(f"""
===== CLASS STATISTICS =====

Number of students: {len(students)}
Class average: {get_class_average()}
Highest average: {get_highest_score()}
Lowest average: {get_lowest_score()}
Students who passed: {get_passed()}
Students who failed: {get_failed()}
""")
        elif choice == 5:
            if len(students) == 0: 
                print("No students to display")
                continue
            top = find_top_student()

            print(f"""
===== TOP STUDENT =====

Name: {top['name']}
Student ID: {top['id']}
Average: {average(top['math_score'], top['english_score'], top['science_score'])}
Grade: {grade(top['math_score'], top['english_score'], top['science_score'])}
""")    
        elif (choice == 6):
            id = input("Input student Id: ")
            for student in students:
                if (student["id"] == id):
                    confirm = input(f'Are you sure you want to remove {id}? (yes/no):').lower()

                    if confirm == 'yes':
                        for student in students:
                            if student["id"] == id:
                                students.remove(student)
                                print(f'{student['name']} deleted')
                                break
                    elif confirm == 'no':
                        break
                    else:
                        print("invalid input ")
                        break
            # else:
            #     print("student not found")
        elif (choice == 7):
            break
        else:
            print("i dont understand")




prompt()