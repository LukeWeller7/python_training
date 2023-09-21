grade_dictionary = {
    "lweller": {
        "Maths": "B",
        "English": "D",
        "Science": "A",
        "Art": "B",
        "Computer Science": "C"
    },
    "jsmith": {
        "Maths": "A",
        "English": "B",
        "Science": "A",
        "Art": "B",
        "Computer Science": "A"

    },
    "ltaylor": {
        "Maths": "D",
        "English": "D",
        "Science": "C",
        "Art": "A",
        "Computer Science": "C"

    },
    "jbishop": {
        "Maths": "B",
        "English": "A",
        "Science": "A",
        "Art": "F",
        "Computer Science": "B"

    },
    "scole": {
        "Maths": "B",
        "English": "B",
        "Science": "B",
        "Art": "B",
        "Computer Science": "A"

    },

}


print("Hello Ms. Bates, please insert below which student's grade you want to add: ")
student = input()
print(f"Please insert the subject you wish to add for {student}:")
subject = input()
print(f"Please tell me what grade did {student} get in {subject}:")
grade = input()

grade_dictionary[student.lower()][subject.lower().capitalize()] = [grade.upper()]

print(f"Here are the updated grades for {student}: {grade_dictionary[student.lower()]}")
