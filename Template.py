from string import Template

def UseTemplate():

    students = []
    students.append(dict(name='Raju',marks1=10, marks2=15, marks3=16))
    students.append(dict(name='Kaju',marks1=15, marks2=18, marks3=19))

    t = Template("Student $name has scored marks $marks1, $marks2, $marks3 in this semester")
    for student in students:
        print(t.substitute(student))

UseTemplate()