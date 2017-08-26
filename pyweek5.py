import sys

data = sys.stdin.readlines()

for i in range(len(data)):
    data[i]=data[i].replace("\n","")

course = []
student = []
grade = []
temp2 = []
temp3 = []
gpoint = {"A": 10, "AB": 9, "B": 8, "BC": 7, "C": 6, "CD": 5, "D": 4}

i = 1
while data[i] != 'Students':
    course.append(data[i].split('~'))	# can be skipped as I ended up doing it without course section.
    i += 1                           	# but the loop is needed to point i to students.
i += 1
while data[i] != 'Grades':
    student.append(data[i].split('~'))
    i += 1
i += 1
while data[i] != 'EndOfInput':
    grade.append(data[i].split('~'))
    i += 1

for s in range(len(student)):
    (sum, avg, scount) = (0, 0, 0)

    for g in range(len(grade)):
        if student[s][0] in grade[g][3]:
            student[s].append(gpoint[grade[g][4]])

    for s1 in range(2, len(student[s])):
        sum = sum + student[s][s1]
        scount += 1
    try:
        avg = sum / scount
    except ZeroDivisionError:
        avg = 0
    avg = round(avg, 2)
    student[s].append(avg)
    temp1 = student[s][:2]
    temp1.append(student[s][-1])
    temp2.append(temp1)
    temp3.append(temp2[s][0])

temp3.sort()
temp4 = []
for i in range(len(temp3)):
    for j in range(len(temp2)):
        if temp2[j][0] == temp3[i]:
            temp4.append(temp2[j])

for i in range(len(temp4)):
    print(temp4[i][0], "~", temp4[i][1], "~", temp4[i][2], sep="")